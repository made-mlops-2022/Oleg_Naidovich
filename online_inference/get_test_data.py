from random import randint, uniform


def gen_invalid_data():
    data = dict(
        age=uniform(-1000, -1),
        sex=uniform(3, 4),
        cp="some str",
        trestbps=uniform(301, 1000),
        chol=uniform(101, 1000),
        fbs=uniform(0, 1),
        restecg=uniform(0, 2),
        thalach=uniform(301, 500),
        exang=uniform(0, 1),
        oldpeak=uniform(11, 25),
        slope=uniform(0, 2),
        ca=[1, 2, 3],
        thal=uniform(20, 28),
    )
    return data


def gen_valid_data():
    data = dict(
        age=randint(0, 150),
        sex=randint(0, 1),
        cp=randint(0, 3),
        trestbps=randint(0, 300),
        chol=randint(0, 100),
        fbs=randint(0, 1),
        restecg=randint(0, 2),
        thalach=randint(0, 300),
        exang=randint(0, 1),
        oldpeak=uniform(0, 10),
        slope=randint(0, 2),
        ca=randint(0, 3),
        thal=randint(0, 2),
    )
    return data
