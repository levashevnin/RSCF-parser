# filename: process_rscf_projects.py

import pandas as pd
import os

def split_from_end(value, separator=","):
    """Разделить строку по первому вхождению разделителя с конца."""
    if pd.isna(value):
        return pd.NA, pd.NA
    parts = value.rsplit(separator, 1)
    if len(parts) == 2:
        return parts[0].strip(), parts[1].strip()
    return value, pd.NA

def split_from_start(value, separator=","):
    """Разделить строку по первому вхождению разделителя с начала."""
    if pd.isna(value):
        return pd.NA, pd.NA
    parts = value.split(separator, 1)
    if len(parts) == 2:
        return parts[0].strip(), parts[1].strip()
    return value, pd.NA

def process_excel_file(filename):
    # Чтение исходного файла
    df = pd.read_excel(filename)

    # Обработка "Название, руководитель"
    df[["Название", "Руководитель"]] = df["Название, руководитель"].apply(lambda x: pd.Series(split_from_end(x)))

    # Обработка "Организация, регион"
    df[["Организация", "Регион"]] = df["Организация, регион"].apply(lambda x: pd.Series(split_from_end(x)))

    # Обработка "Область знания, основной код классификатора"
    df[["Область знания", "Основной код классификатора"]] = df["Область знания, основной код классификатора"].apply(lambda x: pd.Series(split_from_start(x)))

    # Сохраняем результат в новый Excel-файл
    output_filename = "rscf_projects_2024_enriched_processed.xlsx"
    df.to_excel(output_filename, index=False)
    print(f"Обработка завершена. Результат сохранён в: {output_filename}")

if __name__ == "__main__":
    input_file = "rscf_projects_2024_enriched.xlsx"
    if os.path.exists(input_file):
        process_excel_file(input_file)
    else:
        print(f"Файл {input_file} не найден в текущей директории.")
