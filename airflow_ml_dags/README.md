# Homework №3
### _To get started_
```
export DATA_DIR=$(pwd)/data; 
export FERNET_KEY=$(python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")
docker-compose build
docker-compose up
```