from requests import api
import time

r = api.get("https://javaheri.pl")
time.sleep(5)
print(r.status_code)
time.sleep(5)
print(r.headers['content-type'])
time.sleep(5)
print(r.encoding)
time.sleep(5)
print(r.json)