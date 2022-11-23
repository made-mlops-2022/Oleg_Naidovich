def run_predict_pipeline(X_test, y_test, clf):
    preds = predict_model(clf, X_test)
    return preds


def predict_model(model: object, X_test):
    return model.predict(X_test)
