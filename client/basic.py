import requests

endpoint='http://127.0.0.1:8000/djused35/'
aa=(requests.get(endpoint,params={"data_byget":"WOWO"},json={"WW":'e04'})).json()
print(aa["return message"])