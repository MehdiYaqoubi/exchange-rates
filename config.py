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
}
