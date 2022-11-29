if [ -z $PATH_TO_MODEL ]
then
    export PATH_TO_MODEL="models.pkl"
fi

if [ -z $PATH_TO_TRANSFORMER ]
then
    export PATH_TO_TRANSFORMER="transformer.pkl"
fi

uvicorn main:app --reload --host 0.0.0.0 --port 8000