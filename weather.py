inport requests

API_KEY = "myapikey" #後で書き換え　　　
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q":city, "appid":API_KEY,"units":"metric","lang":"ja"}
    response = requests.get(BASE_URL,params=params)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        description = data["weather][0]["description"]
        print(f"{city}の天気:{description},気温:{temp}℃")

        else:
            print("天気情報を取得できませんでした！")

            city = input("都市名を入力してください:")
            get_weather(city)
            