from local_config import API_KEY

BASE_PATH = "http://data.fixer.io/api/latest?access_key="

url = BASE_PATH + API_KEY

rules = {
    'archive': True,
    'email': {
        'receiver': 'mehdi.code@pm.me',
        'enable': True,
        'preferred': ['USD', 'BTC', 'IRR']
    },
    'notification': {
        'enable': True,
        'receiver': '',
        'preferred': {
            'BTC': {'min': 2.2201055e-05, 'max': 2.2201055e-05},
            'IRR': {'min': 47000, 'max': 50000}
        }
    }
}
