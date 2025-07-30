import time
import os
import pandas as pd
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
OUTPUT_FILE = "rscf_projects_2024_enriched.xlsx"  # временный файл для первых 10
BASE_URL = "https://rscf.ru/project/"
MAX_PROJECTS = None  # <-- Тестовый ограничитель: Для провреки парсвера на 10 проектах - указать число 10

# Ставим нужные настройки для Selenium
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 20)

# Парсим каждую карточку проекта, вытаскивая Ключевые слова, Область знания, Код ГРНТИ
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


def main():
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Файл {INPUT_FILE} не найден.")
        return

    df = pd.read_excel(INPUT_FILE)

    for col in ["Ключевые слова", "Код ГРНТИ", "Область знания, основной код классификатора"]:
        if col not in df.columns:
            df[col] = ""

    total = len(df)
    print(f"🔍 Обработка проектов (всего в таблице: {total})")

    count = 0
    for i, row in df.iterrows():
        if MAX_PROJECTS is not None and count >= MAX_PROJECTS:
            break

        project_id = str(row["Номер проекта"]).strip()
        if not project_id:
            continue

        print(f"[{count + 1}] Обрабатывается: {project_id}")
        keywords, grnti, area = parse_project_info(project_id)

        df.at[i, "Ключевые слова"] = keywords
        df.at[i, "Код ГРНТИ"] = grnti
        df.at[i, "Область знания, основной код классификатора"] = area

        count += 1
        time.sleep(1.5)

    df.to_excel(OUTPUT_FILE, index=False)
    print(f"\n✅ Сохранено в {OUTPUT_FILE} (обработано {count} проектов)")


if __name__ == "__main__":
    main()
    driver.quit()
