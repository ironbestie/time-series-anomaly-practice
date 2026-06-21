cat > README.md << 'EOF'
# Система прогнозирования и обнаружения аномалий в телеметрии NASA SMAP

##  Описание проекта
Учебный прототип системы для анализа временных рядов телеметрии спутника SMAP (NASA). 
Проект выполнен в рамках учебной практики.

**Решаемые задачи:**
1. Прогнозирование значений сенсора P-1 (базовая модель и LSTM).
2. Обнаружение аномалий в работе бортовых систем (Z-score, Percentile, Isolation Forest).

## 🛰 Предметная область
SMAP (Soil Moisture Active Passive) — спутник NASA. Телеметрия включает сотни сенсоров. 
Аномалия = сбой датчика или нештатный режим работы. Своевременное обнаружение предотвращает отказ аппарата.

## 📊 Датасет
[NASA Anomaly Detection Dataset SMAP & MSL](https://www.kaggle.com/datasets/patrickfleith/nasa-anomaly-detection-dataset-smap-msl)

⚠️ **Датасет не включён в репозиторий из-за большого объёма.** 
Для его скачивания выполните:
```bash
pip install kagglehub
python data/download_data.py
