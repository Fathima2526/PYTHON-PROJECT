import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ask for the key when the script runs (never write it in the code)
api_key = input("Enter your WeatherAPI key:ba052b7b42c14fae972123936261710 ").strip()

cities = ["New York", "London", "Chennai", "Tokyo", "Sydney"]
url = "https://api.weatherapi.com/v1/current.json"

records = []
for city in cities:
    try:
        response = requests.get(url, params={"key": api_key, "q": city}, timeout=10)
        if response.status_code == 200:
            temp = response.json()["current"]["temp_c"]
            records.append({"City": city, "Temperature (°C)": temp})
            print(f"{city}: {temp}°C")
        else:
            print(f"Error for {city}: {response.status_code} {response.text}")
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
