from datetime import datetime
import requests
import json
import time

r = requests.get('https://api.ratesapi.io/api/latest?base=GBP&symbols=PLN')
data = r.text
nexttime = time.time()

while True:
    try:
        def decor_currency(function):
             def currency():
                parse = json.loads(data)
                print('Kurs funta: ' + str(parse['rates']['PLN']))
                return function()
             return currency()

        @decor_currency
        def get_time():
            print('Data i godzina: ' + str(datetime.now()))
            print('Czas wykonania zapytania: ' + str(r.elapsed.total_seconds() * 1000) + ' ms')
            print('----------------------')

    except TimeoutError:
        print('Serwis chwilowo niedostępny')


    nexttime += 15
    sleeptime = nexttime - time.time()
    if sleeptime > 0:
        time.sleep(sleeptime)