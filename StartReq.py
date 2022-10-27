import requests
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTZjusfWgTiXGVSUeApaJmHVUDt9907vgteCyQi9UwUwozJIZDXKx9O0hCkK7JVxBa_w-Qzxc0j3tkL/pub?gid=0&single=true&output=csv"
r = requests.get(url)
print(r.text)
print(str(r.status_code))
print(str(r.encoding))
print(str(r.cookies))
