import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://rscf.ru/project/")
wait = WebDriverWait(driver, 20)

wait.until(
    lambda d: d.find_element(By.ID, "page-preloader").get_attribute("class") == "preloader done"
)

# Блок 1 - Клик по кнопке выбора периода
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-id='period-select']")))
button.click()

# Блок 2 - Ждём открытия выпадающего списка
wait.until(lambda d: button.get_attribute("aria-expanded") == "true")
dropdown_menu = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.dropdown-menu.show")))

# Блок 3 - Клик по году "2024 г."
options = dropdown_menu.find_elements(By.CSS_SELECTOR, "a.dropdown-item")
for option in options:
    text = option.text.strip().replace('\xa0', ' ')
    if "2024" in text:
        option.click()
        break

# Блок 4 - Клик по кнопке "Найти проекты"
search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search-projects-btn")))
search_button.click()

# Блок 5 - Ждём появления таблицы
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table#filtered-table tbody tr")))

# Блок 6 - Дожидаемся полной подгрузки
time.sleep(2)

# Блок 7 - Получаем HTML таблицы через Selenium
table_html = driver.find_element(By.ID, "filtered-table").get_attribute("outerHTML")
soup = BeautifulSoup(table_html, "html.parser")

# Блок 8 - Парсим строки
data = []
rows = soup.select("tbody tr")
for row in rows:
    cols = row.find_all("td")
    if len(cols) < 6:
        continue

    # Блок 8.1 - Извлечение данных
    num = cols[0].get_text(strip=True)
    project_number = cols[1].get_text(strip=True)
    title_leader = cols[2].get_text(" ", strip=True)
    codes = cols[3].get_text(" ", strip=True)
    contest = cols[4].get_text(" ", strip=True)
    organization = cols[5].get_text(" ", strip=True)

    data.append([num, project_number, title_leader, codes, contest, organization])

# Блок 9 - Закрываем браузер
driver.quit()

# Блок 10 - Сохраняем в Excel
df = pd.DataFrame(data, columns=[
    "№", "Номер проекта", "Название, руководитель",
    "Коды классификатора", "Конкурс", "Организация, регион"
])
df.to_excel("rscf_projects_2024.xlsx", index=False)

print("✅ Успешно: сохранено в rscf_projects_2024.xlsx")
