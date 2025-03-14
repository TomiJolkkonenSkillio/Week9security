import requests

def etsi_vitsi():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        responssi = requests.get(url)
        responssi.raise_for_status()
        vitsi = responssi.json()
        print(f"{vitsi['setup']} - {vitsi['punchline']}")
    except requests.exceptions.RequestException as e:
        print(f"Tuli virhe: {e}")

if __name__ == "__main__":
    etsi_vitsi()