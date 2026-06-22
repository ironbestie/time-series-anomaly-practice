# Система прогнозирования и обнаружения аномалий в телеметрии NASA SMAP

## 📌 Описание проекта
Учебный прототип системы для анализа временных рядов телеметрии спутника SMAP (NASA).
Проект выполнен в рамках учебной практики МТИ25.

**Решаемые задачи:**
1. Прогнозирование значений сенсора P-1
2. Обнаружение аномалий в работе бортовых систем

## 🛰 Предметная область
SMAP (Soil Moisture Active Passive) — спутник NASA для мониторинга влажности почвы.
Телеметрия включает сотни сенсоров. Аномалия = сбой датчика или нештатный режим работы.

## 📊 Датасет
[NASA Anomaly Detection Dataset SMAP & MSL](https://www.kaggle.com/datasets/patrickfleith/nasa-anomaly-detection-dataset-smap-msl)

⚠️ **Датасет не включён в репозиторий** (большой объём). Он автоматически скачивается при первом запуске ноутбука через `kagglehub`.

## 🚀 Запуск проекта

### Вариант 1: Google Colab (рекомендуется)
1. Открой файл `anomaly_detection_project.ipynb` в Google Colab
2. Выполняй ячейки последовательно (или «Выполнить все»)
3. При первом запуске потребуется авторизация в Kaggle

[**Открыть в Google Colab**](https://colab.research.google.com/drive/1GUvJpiJt3kA_fvI9qquRGJU7wyxupHhv?usp=sharing)

### Вариант 2: Локально
```bash
pip install -r requirements.txt
jupyter notebook anomaly_detection_project.ipynb
