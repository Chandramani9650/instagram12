import requests,json
Apikey = "c8ab5e60918f3136ecab4c59086c9585"
BaseURL = "https://api.openweathermap.org/data/2.5/weather?"
city_name = input("enter city name")
completeURL = BaseURL + "appid="+ Apikey + "&q=" + city_name
response = requests.get(completeURL)
data  = response.json()
# print(data)
if data !="401":
    Temp = data["main"]["temp"]

    temp1 = Temp - 273
    # round(temp1, 2)
    print("Current temperature of "+city_name+" is "+str(round(temp1, 2)) + "/C")
else:
    print("this city not found something error")

