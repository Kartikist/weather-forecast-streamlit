import requests, json


api_key = "8b8218bb7e0feffe5ace6189f7b743e2"

def get_data(place,days=None):
    
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    if filtered_data:
        nr_values = 8 * days
        filtered_data = filtered_data[:nr_values]
    
        
        return filtered_data
    else:
        return None


if __name__ == "__main__":
    # print(get_data(place= "tokyo",days=3,kind="Temperature"))
    get_data()

