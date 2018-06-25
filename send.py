import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTI5NjkzMTIyLCJqdGkiOiI2ZWI4MzI5ZTc4YjA0MGMzOTc0NmFjYmQ2ZmYwZDE4MyIsInVzZXJfaWQiOjF9.Z_FpKyxmG4E6k4aP3sqlqDhYHih95HB9-6ESxXo1vOY'

r = requests.get('http://127.0.0.1:8000/App/addresses/', headers = headers)
print(r.text)