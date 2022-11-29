MLOps Project
==============================
author: Oleg Naidovich

### Installation
```
pip installl -r requirements.txt
```

### _To get data_
```
dvc pull -r gdrive
```

### _To run EDA_
* Find a report at `reports/report.html` or from `ml_prject/` run to generate a new file:
```
python3 src/data/create_eda_report.py
```

### _To run Data Processing Pipeline_
* Find preprocessed and splitted data at `data/train` and `data/test`
* Transformer lies at `models`
* From `ml_prject` run to get preprocessed and splitted data (default):
```
python3 src/preprocess.py
```

### _To run Train Pipeline_
* Find saved model at  `models` folder
* From `ml_prject` run to get KNN classifier (default)
```
python3 src/train.py
```
### _To run Prediction Pipeline_
* Find final outputs at `data/predictions` folder
* From `ml_prject` run to get predictions (default)
```bash
python3 src/predict.py 
```
