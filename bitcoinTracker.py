import tkinter as tk
import requests
from datetime import datetime

def get_bitcoin_price():
    try:
        url = "https://www.alphavantage.co/query"
        params = {"function": "CURRENCY_EXCHANGE_RATE", "from_currency": "BTC", "to_currency": "USD", "apikey": "YOURTOKEN"}
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        price = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
        return price
    except requests.RequestException:
        return None

def update_price():
    price = get_bitcoin_price()
    if price is not None:
        price_label.config(text=f"BTC: ${price:,.2f}")
    else:
        price_label.config(text="BTC: Error")
    # Ensure the update loop continues
    root.after(1000, update_price)

root = tk.Tk()
root.title("Bitcoin Price")
root.geometry("150x50")
try:
    root.iconbitmap('Bitcoin.ico')
except tk.TclError:
    print("Warning: Could not load Bitcoin.ico for window icon. Using default.")
root.attributes("-topmost", True)  # Always on top
root.resizable(False, False)  # Corrected method call

# Configure style
root.configure(bg="#2c2c2c")
price_label = tk.Label(root, text="BTC: Loading...", font=("Arial", 12), fg="white", bg="#2c2c2c")
price_label.pack(pady=10)

# Start the price update loop
update_price()

# Run the app
root.mainloop()