import requests
import click
from get_test_data import gen_valid_data, gen_invalid_data


@click.command("client_test")
def main():
    def do_valid_request():
        data = gen_valid_data()
        res = requests.post(f"{SERVER_URL}/predict", json=data)
        print(res.status_code)
        print(res.content)

    def do_unvalid_request():
        data = gen_invalid_data()
        res = requests.post(f"{SERVER_URL}/predict", json=data)
        print(res.status_code)
        print(res.content)

    SERVER_URL = "http://127.0.0.1:3000"
    N_VALID_REQ = 3
    N_UNVALID_REQ = 3

    if requests.get(f"{SERVER_URL}/health").status_code != 200:
        raise Exception

    for _ in range(N_VALID_REQ):
        print("=" * 50)
        do_valid_request()
    for _ in range(N_UNVALID_REQ):
        print("=" * 50)
        do_unvalid_request()


if __name__ == "__main__":
    main()
