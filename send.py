import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTI5OTM1NTM4LCJqdGkiOiJmZDE3ZjQ5NmYwMWM0MjYxYjc0NjdlZjA0ZjU1NDU2MyIsInVzZXJfaWQiOjF9.fzgNoWhCvKWhd-MuWjF86A049KZovDqm6K3rPV6sGek'

r = requests.get('http://127.0.0.1:8000/App/addresses/', headers = headers)
print(r.text)