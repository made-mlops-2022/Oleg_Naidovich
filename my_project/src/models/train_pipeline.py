import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, \
    precision_score, recall_score


def run_train_pipeline(X: np.ndarray,
                       y: np.ndarray,
                       clf_name: str,
                       clf_params: dict,
                       n_folds: int):

    if clf_name == 'KNeighborsClassifier':
        clf = KNeighborsClassifier(**clf_params)

    total_metrics = []
    KFold = StratifiedKFold(n_splits=n_folds, shuffle=True)
    for fold, (idx_train, idx_val) in enumerate(KFold.split(X, y)):
        X_train, X_val = X[idx_train], X[idx_val]
        y_train, y_val = y[idx_train], y[idx_val]

        clf.fit(X_train, y_train)

        oof_pred = clf.predict(X_val)
        currect_metrics = get_metrics(y_val, oof_pred)
        total_metrics.append(currect_metrics)

    clf.fit(X, y)
    return clf, total_metrics


def get_metrics(y_true: np.ndarray, y_pred: np.ndarray):
    return {'accuracy': accuracy_score(y_true, y_pred),
            'f1_score': f1_score(y_true, y_pred, average='micro'),
            'precision': precision_score(y_true, y_pred, average='micro'),
            'recall': recall_score(y_true, y_pred, average='micro')}
