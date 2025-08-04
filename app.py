import requests
import pyttsx3

# Initialize engine
engine = pyttsx3.init()
engine.setProperty('rate', 180)

# Try to set a female voice (if available)
voices = engine.getProperty('voices')
for voice in voices:
    if 'female' in voice.name.lower() or 'zira' in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

def speak(text):
    print("🗣️", text)
    engine.say(text)
    engine.runAndWait()

def get_weather(city):
    try:
        res = requests.get(f"https://wttr.in/{city}?format=j1").json()
        temp = res["current_condition"][0]["temp_C"]
        desc = res["current_condition"][0]["weatherDesc"][0]["value"]
        speak(f"{city} weather: {desc}, {temp}°C")
    except:
        speak("Sorry, couldn't fetch weather info.")

# --- Main loop ---
while True:
    city = input("Enter city (or 'exit'): ").strip()
    if city.lower() == "exit":
        break
    get_weather(city)