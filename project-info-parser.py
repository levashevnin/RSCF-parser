import time
import os
import pandas as pd
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# === НАСТРОЙКИ ===
INPUT_FILE = "rscf_projects_2024.xlsx"
OUTPUT_FILE = "rscf_projects_2024_enriched_test.xlsx"
BASE_URL = "https://rscf.ru/project/"


# === Настройки Selenium ===
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 20)

# === Удаляем недопустимые для Excel символы ===
def clean_excel_string(value):
    if not isinstance(value, str):
        return value
    # Удаляем управляющие символы кроме табуляции и переноса строки
    return re.sub(r"[\x00-\x08\x0B\x0C\x0E-\x1F]", "", value)

# === Парсинг одной страницы проекта ===
def parse_project_info(project_id):
    url = BASE_URL + project_id + '/'
    try:
        driver.get(url)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "fld_title")))
        time.sleep(1)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        keywords = ""
        grnti = ""
        area = ""

        for p in soup.find_all("p"):
            label = p.find("span", class_="fld_title")
            if not label:
                continue
            label_text = label.get_text(strip=True)
            value = p.get_text(strip=True).replace(label_text, "").strip()

            if label_text == "Ключевые слова":
                keywords = value
            elif label_text == "Код ГРНТИ":
                grnti = value
            elif "Область знания" in label_text:
                area = value

        if not keywords and not grnti and not area:
            print(f"⚠️ Пустой результат у {project_id}")
            print(f"   Страница: {url}")

        return keywords, grnti, area

    except Exception as e:
        print(f"❌ Ошибка при обработке {project_id}: {e}")
        return "", "", ""

# === Основной запуск ===
def main():
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Файл {INPUT_FILE} не найден.")
        return

    df = pd.read_excel(INPUT_FILE)
    START_INDEX = 0
    END_INDEX = 10  # НЕ включительно

    for col in ["Ключевые слова", "Код ГРНТИ", "Область знания, основной код классификатора"]:
        if col not in df.columns:
            df[col] = ""

    total = len(df)
    print(f"🔍 Обработка проектов (всего в таблице: {total})")

    subset_df = df.iloc[START_INDEX:END_INDEX].copy()

    for i in subset_df.index:
        row = df.loc[i]
        project_id = str(row["Номер проекта"]).strip()
        if not project_id:
            continue

        print(f"[{i - START_INDEX + 1}] Обрабатывается: {project_id}")
        keywords, grnti, area = parse_project_info(project_id)

        df.at[i, "Ключевые слова"] = clean_excel_string(keywords)
        df.at[i, "Код ГРНТИ"] = clean_excel_string(grnti)
        df.at[i, "Область знания, основной код классификатора"] = clean_excel_string(area)

        time.sleep(0.5)

    df.iloc[START_INDEX:END_INDEX].to_excel(OUTPUT_FILE, index=False)
    print(f"\n✅ Сохранено в {OUTPUT_FILE} (обработано {END_INDEX - START_INDEX} проектов)")


if __name__ == "__main__":
    main()
    driver.quit()
