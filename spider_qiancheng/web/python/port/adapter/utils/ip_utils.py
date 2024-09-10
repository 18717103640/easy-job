import requests


def get_ip_address():
    response = requests.get('https://api.ipify.org?format=json')
    return response.json()['ip']


if __name__ == '__main__':
    print(get_ip_address())
