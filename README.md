# Binance Futures Trading Bot (Testnet)

## 📌 Overview

This project is a Python-based trading bot that interacts with the Binance Futures Testnet (USDT-M). It allows users to place MARKET and LIMIT orders through a clean command-line interface, with proper validation, logging, and error handling.

The application is designed with a modular structure to ensure readability, maintainability, and ease of extension.

---

## 🚀 Features

* Place **MARKET** and **LIMIT** orders
* Supports both **BUY** and **SELL**
* CLI-based interaction (command mode + interactive menu)
* Input validation for safe execution
* Structured logging of requests, responses, and errors
* Clean and modular code architecture

---

## 🧱 Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py          # Binance API client wrapper
│   ├── orders.py          # Order execution logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup
│
├── cli.py                 # CLI entry point
├── test_connection.py     # API connection test
├── requirements.txt
├── README.md
├── trading_bot.log        # Sample logs
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```
git clone <
cd trading_bot
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_api_secret
```

⚠️ Note:

* Use **Binance Futures Testnet** API keys only
* Do not use mainnet keys

---

## ▶️ How to Run

### 🔹 CLI Mode

```
python cli.py trade --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.01
```

### 🔹 Interactive Menu

```
python cli.py menu
```

---

## 📊 Sample Output

```
📊 ORDER SUMMARY
==============================
Symbol        : BTCUSDT
Side          : BUY
Order Type    : MARKET
Quantity      : 0.01

📡 RESPONSE
==============================
Order ID      : 130399xxxx
Status        : NEW
Executed Qty  : 0.0000
Avg Price     : Not filled yet

✅ Order placed successfully!
```

---

## 📝 Logging

All API interactions are logged in:

```
trading_bot.log
```

Logs include:

* Order requests
* API responses
* Errors and exceptions

---

## ⚠️ Assumptions

* The bot operates on **Binance Futures Testnet (USDT-M)**
* User provides valid API credentials
* Quantity precision may vary depending on symbol

---

## 🧠 Design Approach

The application follows a modular architecture:

* **Client Layer** → Handles API interaction
* **Logic Layer** → Manages order execution
* **Validation Layer** → Ensures input correctness
* **CLI Layer** → Handles user interaction

This separation ensures scalability and easier debugging.

---

## 🧪 Testing

* Tested with both MARKET and LIMIT orders
* Verified API connectivity using test script
* Logs generated for successful execution

---

## ✨ Future Improvements

* Add Stop-Limit / OCO order support
* Improve CLI with enhanced UI (colors, formatting)
* Add web-based dashboard (optional)

---

## 📌 Conclusion

This project demonstrates a structured approach to building a trading system with proper API integration, validation, and logging, while maintaining clean and reusable code.

---
