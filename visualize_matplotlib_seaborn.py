import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

api_key = input("Enter your WeatherAPI key:ba052b7b42c14fae972123936261710").strip()
print(f"(key length: {len(api_key)})\n")   # should be 31; if not, the paste is wrong

cities = ["New York", "London", "Chennai", "Tokyo", "Sydney"]
url = "https://api.weatherapi.com/v1/current.json"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                         "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"}

records = []
for city in cities:
    try:
        response = requests.get(url, params={"key": api_key, "q": city},
                                headers=headers, timeout=10)
        if response.status_code == 200:
            temp = response.json()["current"]["temp_c"]
            records.append({"City": city, "Temperature (°C)": temp})
            print(f"{city}: {temp}°C")
        else:
            print(f"Error for {city}: {response.status_code} {response.text[:100]}")
    except requests.RequestException as e:
        print(f"Request failed for {city}: {e}")

if records:
    df = pd.DataFrame(records)
    plt.figure(figsize=(8, 5))
    ax = sns.barplot(data=df, x="City", y="Temperature (°C)", color="skyblue")
    ax.bar_label(ax.containers[0], fmt="%.1f°C")
    plt.title("Current Temperature by City")
    plt.tight_layout()
    plt.savefig("weather_chart.png")
    plt.show()
