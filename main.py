"""consumo de api"""
import json
import requests

def get_data():
    '''poke api'''
    try:
        data = {
            "title": "new product",
            "description": "new product",
            "price": 12.50,
            "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg",
            "category": "electronic"
        }

        response = requests.post('https://fakestoreapi.com/products', data, timeout=10)
        #response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=20&offset=20', timeout=10)
        #response = requests.get('https://fakestoreapi.com/products', timeout=10)
        #print(response.status_code, response.content)
        print(json.dumps(response.json(), indent=2))
    except requests.exceptions.RequestException as err:
        print(f"Ha ocurrido un error: {err}")

if __name__=="__main__":
    get_data()
