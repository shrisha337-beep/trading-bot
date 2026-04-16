from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

client = Client(os.getenv("API_KEY"), os.getenv("API_SECRET"))

client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

print(client.futures_account_balance())