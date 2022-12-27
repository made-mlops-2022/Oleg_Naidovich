if [ -z $PATH_TO_MODEL ]
then
    export PATH_TO_MODEL="models.pkl"
fi

if [ -z $PATH_TO_TRANSFORMER ]
then
    export PATH_TO_TRANSFORMER="transformer.pkl"
fi

if [[ ! -f $PATH_TO_MODEL ]]
then
    gdown https://drive.google.com/uc?id=1NUOoinTdKszHYEXblNrjeM-GJGFT88wq --output=$PATH_TO_MODEL
else
    echo "model exists"
fi

if [[ ! -f $PATH_TO_TRANSFORMER ]]
then
    gdown https://drive.google.com/uc?id=1jJR1wARI70amf_DW2WG7ER5wPg_dpRg3 --output=$PATH_TO_TRANSFORMER
else
    echo "transformer exists"
fi

uvicorn main:app --reload --host 0.0.0.0 --port 8000