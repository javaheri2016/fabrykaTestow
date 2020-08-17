from datetime import datetime
import requests
import json
import time


def decor_time(function):
    def wrapper():
        req_time = datetime.now()
        start_time = time.time()
        function()
        end_time = time.time()
        print('Data i godzina: ' + str(req_time))
        print('Czas wykonania zapytania: ' + str((end_time - start_time) * 1000) + ' ms')
        print('----------------------')
    return wrapper()


@decor_time
def currency():
    try:
        r = requests.get('https://api.ratesapi.io/api/latest?base=GBP&symbols=PLN')
        data = r.text
        parse = json.loads(data)
        print('Kurs funta: ' + str(parse['rates']['PLN']))
    except requests.exceptions.Timeout:
        print('Serwis chwilowo niedostępny')


while True:
    currency()
    time.sleep(15)
