from base64 import b64decode
import requests


def info_in_block(number_block):
    url_for_block = f'https://akash-api.w3coins.io/blocks/{number_block}'
    response = requests.get(url_for_block)
    data_list: list = response.json().get('block').get('data').get('txs')
    for data in data_list:
        print(b64decode(data))


info_in_block(11260637)
