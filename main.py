import json

import requests

from config import url, rules
from mail import send_smtp_mail


def get_rates():
    """
    send a get requests to the fixer.ip api and get live rates
    :return: requests.Response instance
    """
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return None


def archive(filename, rates):
    """
    get filename and rate, save them to the specific directory
    :param filename:
    :param rates:
    :return: None
    """
    with open(f'archive/{filename}.json', 'w') as f:
        f.write(json.dumps(rates))


def send_mail(timestamp, rates):
    """
    get timestamp and rates, check if there is preferred rates and
    then send email through smtp
    :param timestamp:
    :param rates:
    :return:
    """
    subject = f'{timestamp} rates'

    if rules['preferred'] is not None:
        tmp = dict()
        for exc in rules['preferred']:
            tmp[exc] = rates[exc]

    text = json.dumps(rates)
    send_smtp_mail(subject, text)


if __name__ == "__main__":
    res = get_rates()

    if rules['archive']:
        archive(res['timestamp'], res['rates'])

    if rules['send_mail']:
        send_mail(res['timestamp'], res['rates'])
