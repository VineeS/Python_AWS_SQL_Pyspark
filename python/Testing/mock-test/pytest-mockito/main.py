import requests

def get_data():
    url = "https://api.example.com/data"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    print(get_data())