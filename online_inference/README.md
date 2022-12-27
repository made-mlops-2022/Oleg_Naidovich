### Run tests:

* Linux, MacOS: 
    ```
    cd online_inference
    export PATH_TO_TRANSFORMER=transformer.pkl
    export PATH_TO_MODEL=models.pkl  
    python3 -m pytest test_main.py
    ```

* Windows:
    ```
    cd online_inference
    set PATH_TO_TRANSFORMER=transformer.pkl
    set PATH_TO_MODEL=models.pkl  
    python3 -m pytest test_main.py
    ```

### Build docker image:
```
docker build -t mlops .
```

### Run docker container:
```
docker run -d -p 8080:80 mlops
```

### Pull docker image:
```
docker pull olegnai1/mlops
```

My docker image is here: https://hub.docker.com/repository/docker/olegnai1/mlops


## Steps to reduce docker image size:
1. Don’t install unnecessary packages in requirements.txt. Install only very required libs.
2. split src requirement and inline_inference in di.txt was split for ml_project and for online_inference
3. There are two COPY instructions: one for requirements.txt and one for the rest of the necessary files. 
4. COPY only instruction for all files that need to be copied
5. Install only required packages. For this requirements.txt was split for ml_project and for online_inference
6. Use light-weighted base image. Before: 1.46GB, after: 668MB
7. Choose more lightweight basis python version  
