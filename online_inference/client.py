import requests
import click
import time
from get_test_data import gen_valid_data, gen_invalid_data


@click.command('client_test')
def main():
    SERVER_URL = 'http://127.0.0.1:3000'

    while True:
        if requests.get(f'{SERVER_URL}/health').status_code == 200:
            break
        time.sleep(0.1)

    for _ in range(5):
        data = gen_valid_data()
        res = requests.post(f'{SERVER_URL}/predict', json=data)

        print(res.status_code)
        print(res.content)

    for _ in range(5):
        data = gen_invalid_data()
        res = requests.post(f'{SERVER_URL}/predict', json=data)

        print(res.status_code)
        print(res.content)


if __name__ == '__main__':
    main()
