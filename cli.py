import typer
from bot.orders import place_order
from bot.logging_config import setup_logger

app = typer.Typer()
logger = setup_logger()


def display_result(symbol, side, order_type, quantity, price, result):
    print("\n📊 ORDER SUMMARY")
    print("=" * 30)

    print(f"Symbol        : {symbol}")
    print(f"Side          : {side}")
    print(f"Order Type    : {order_type}")
    print(f"Quantity      : {quantity}")

    if price:
        print(f"Price         : {price}")

    print("\n📡 RESPONSE")
    print("=" * 30)

    print(f"Order ID      : {result.get('orderId')}")
    print(f"Status        : {result.get('status')}")
    print(f"Executed Qty  : {result.get('executedQty')}")

    avg_price = result.get("avgPrice")
    print(f"Avg Price     : {avg_price if avg_price != '0.0' else 'Not filled yet'}")

    print("\n✅ Order placed successfully!\n")


@app.command()
def trade(
    symbol: str = typer.Option(...),
    side: str = typer.Option(...),
    order_type: str = typer.Option(...),
    quantity: float = typer.Option(...),
    price: float = typer.Option(None)
):
    result = place_order(symbol, side, order_type, quantity, price, logger)
    display_result(symbol, side, order_type, quantity, price, result)


@app.command()
def menu():
    print("\n📈 Trading Bot Menu")
    print("1. MARKET order")
    print("2. LIMIT order")

    choice = input("Enter choice: ")

    symbol = input("Symbol: ").upper()
    side = input("Side (BUY/SELL): ").upper()
    quantity = float(input("Quantity: "))

    if choice == "1":
        order_type = "MARKET"
        price = None
        result = place_order(symbol, side, order_type, quantity, price, logger)

    elif choice == "2":
        order_type = "LIMIT"
        price = float(input("Price: "))
        result = place_order(symbol, side, order_type, quantity, price, logger)

    else:
        print("Invalid choice")
        return

    display_result(symbol, side, order_type, quantity, price, result)


if __name__ == "__main__":
    app()