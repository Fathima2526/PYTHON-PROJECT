import requests
import matplotlib.pyplot as plt


api_key = "7099bcf686a8453bb85164629250612"  
city = "New York"                   

url = "http://api.weatherapi.com/v1/current.json"
params = {
    "key": api_key,
    "q": city
}

try:
    response = requests.get(url, params=params)
    print("Status code:", response.status_code)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['current']['temp_c']
        print(f"Current temperature in {city}: {temp}°C")
        
        
        plt.bar(city, temp, color="skyblue")
        plt.title(f"Current Temperature in {city}")
        plt.ylabel("Temperature (°C)")
        plt.text(0, temp + 0.5, f"{temp:.1f}°C", ha='center')
        plt.show()
        
    else:
        print("Error fetching data. Response text:", response.text)
        
except Exception as e:
    print("Request failed:", e)
