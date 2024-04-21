import sys
import pandas as pd
if len(sys.argv) != 2:
    print("Использование: python json2csv.py example.json")
    sys.exit(1)
filename = sys.argv[1]
try:
    obj = pd.read_json(filename)
    output_filename = filename.split('.')[0] + ".csv"
    obj.to_csv(output_filename, index=False)
    print(f"Файл успешно преобразован в CSV: {output_filename}")
except Exception as e:
    print(f"Ошибка при преобразовании файла: {e}")
