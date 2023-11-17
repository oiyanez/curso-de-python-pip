import requests

def get_categories():
    r = requests.get("https://api.escuelajs.co/api/v1/categories")
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categories = r.json()
    print("\n")
    nombres = list(map(lambda x:print(x["name"]), categories ))
    return nombres
