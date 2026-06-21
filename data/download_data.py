"""
Скрипт для скачивания датасета NASA SMAP & MSL.
Запустите этот файл перед работой с ноутбуком:
    python data/download_data.py
"""
import kagglehub

# Скачивание датасета
path = kagglehub.dataset_download("patrickfleith/nasa-anomaly-detection-dataset-smap-msl")
print("Датасет успешно скачан в папку:", path)
