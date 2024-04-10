import json
import pandas as pd
import os
import sys

def json_to_csv(json_file):
    # Открыть JSON файл и загрузить его содержимое
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Создать DataFrame из JSON данных
    df = pd.json_normalize(data)
    
    # Получить имя файла без расширения
    file_name = os.path.splitext(json_file)[0]
    
    # Определить имя CSV файла на основе имени JSON файла
    csv_file = f"{file_name}.csv"
    
    # Сохранить DataFrame в CSV файл
    df.to_csv(csv_file, index=False)
    
    print(f"Файл {csv_file} успешно создан.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python json2csv.py example.json")
    else:
        json_file = sys.argv[1]
        json_to_csv(json_file)
