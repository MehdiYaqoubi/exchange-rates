from local_config import API_KEY, mail_receiver

BASE_PATH = "http://data.fixer.io/api/latest?access_key="

url = BASE_PATH + API_KEY

rules = {
    'archive': True,
    'email': {
        'receiver': mail_receiver,
        'enable': True,
        'preferred': ['USD', 'BTC', 'IRR']
    },
    'notification': {
        'enable': False,
        'receiver': '',
        'preferred': {
            'BTC': {'min': 2.2201055e-05, 'max': 2.2201055e-05},
            'IRR': {'min': 47000, 'max': 50000}
        }
    }
}
