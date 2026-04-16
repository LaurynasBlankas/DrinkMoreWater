import os

import requests
from dotenv import load_dotenv
import random

load_dotenv()
api_key = os.getenv("api_key")
receiver_id = os.getenv("receiver_id")

def send_telegram(message):
    url_telegram = f"https://api.telegram.org/bot{api_key}/sendMessage"
    payload = {"chat_id": receiver_id, "text": message}
    requests.post(url_telegram, json=payload)

messages = ["Don't forget to hydrate! 💧",
            "Time for a water break! 🚰",
            "Stay hydrated! 🥤",
            "Drink some water! 💦",
            "Water is life! 🌊",
            "Water is love! 🌊",
            "Drink up! 🥛",
            "Keep sipping! 🍶",
            "Water is essential! 💧",
            "Hydration is key! 🔑",
            "Water is the best! 💧",
            "Don't forget to drink water! 🚰",
            "Stay refreshed! 🥤",
            "Water is your friend! 💦",
            "Keep hydrated! 🥛",
            "Don't forget to drink water! 🚰",
            "Stay hydrated and healthy! 🥤",
            "U FOOL, U MUST ABSORB THE FLOWING TREASURE NOW! 💧",
            "psst, water now 🚰",
            "_Water_ 💧",
            "I beg you, go get that water bottle 💧",
            "через не можу 💧"]

msg = messages[random.randint(0, len(messages)-1)]

send_telegram(msg)