import requests, json


api_key = "8b8218bb7e0feffe5ace6189f7b743e2"

def get_data(place,days=None,kind=None):
    
    place = 'tokyo'
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    
    for i in data["list"][:5]:
        days5 = i["main"]["temp"]
        
    
    return data


if __name__ == "__main__":
    print(get_data(place= "tokyo"))

