from datetime import datetime
import requests
import json
import time
import csv

def create_csv():
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Data", "Czas wykonania", "Kurs funta"])

def append_rate_csv(rate, req_time, duration):
    with open('data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([str(req_time), str(duration), rate])

def decor_time(function):
    def wrapper():
        req_time = datetime.now()
        start_time = time.time()
        rate = function()
        end_time = time.time()
        req_duration = int((end_time - start_time) * 1000)
        duration = round(req_duration)
        print('Data i godzina: ' + str(req_time))
        print('Czas wykonania zapytania: ' + str(duration) + ' ms')
        print('----------------------')
        append_rate_csv(rate, req_time, duration)
    return wrapper


@decor_time
def currency():
    try:
        r = requests.get('https://api.ratesapi.io/api/latest?base=GBP&symbols=PLN')
        data = r.text
        parse = json.loads(data)
        rate = str(parse['rates']['PLN'])
        print('Kurs funta: ' + rate)
    except requests.exceptions.Timeout:
        print('Serwis chwilowo niedostępny')
    return rate


create_csv()
while True:
    currency()
    time.sleep(15)