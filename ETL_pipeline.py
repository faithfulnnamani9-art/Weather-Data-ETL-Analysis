import requests
import pandas as pd
API_KEY =  "23a44102e1b21d8bc08149ae9622078b"
cities = ["Lagos", "Abuja", "Enugu"]
weather_data = []
for city in cities:
    url =  f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_data.append({
            "city":city, "Temperature (°C)":
            data["main"]["temp"], "Humidity (%)":
            data["main"]["humidity"], "weather condidtion":
            data["weather"][0]["description"], "Wind Speed (m/s)":
            data["wind"]["speed"], "Date and Time": data["dt"]})
        df = pd.DataFrame(weather_data)
        print(df)
import requests
import pandas as pd
API_KEY =  "23a44102e1b21d8bc08149ae9622078b"
cities = ["Lagos", "Abuja", "Enugu"]
weather_data = []
for city in cities:
    url =  f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_data.append({
            "city":city, "Temperature (°C)":
            data["main"]["temp"], "Humidity (%)":
            data["main"]["humidity"], "weather condidtion":
            data["weather"][0]["description"], "Wind Speed (m/s)":
            data["wind"]["speed"], "Date and Time": data["dt"]})
        df = pd.DataFrame(weather_data)
        print(df)
df.rename(columns={"weather condidtion": "Weather Condition"},inplace=True)
df.rename(columns={"city": "City"},inplace=True)
print(df.dtypes)
print(df.isnull().sum())
print(df.duplicated().sum())
print(df)
df.to_csv("weather_data.csv", index=False)
df.to_excel("weather_data.xlsx", index=False)
import sqlite3
conn = sqlite3.connect("weather.db")
df.to_sql("weather_data",conn,if_exists="replace",index
          =False)
conn.close()
print(df[["City", "Temperature (°C)"]])
Highest_Humidity = df.loc[df["Humidity (%)"].idxmax()]
print("City with Highest Humidity:", Highest_Humidity["City"])
print(df[["City", "Weather Condition"]])