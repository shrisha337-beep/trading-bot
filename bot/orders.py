from .client import get_client
from .validators import validate_order


def place_order(symbol, side, order_type, quantity, price, logger):
    # Validate input first
    validate_order(symbol, side, order_type, quantity, price)

    client = get_client()

    try:
        # Place order based on type
        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        else:
            raise ValueError("Unsupported order type")

        # Clean logging
        logger.info(
            f"Order placed | Symbol={symbol} | Side={side} | Type={order_type} | Qty={quantity}"
        )

        logger.info(
            f"Response | OrderID={order.get('orderId')} | Status={order.get('status')} | ExecutedQty={order.get('executedQty')}"
        )

        return order

    except Exception as e:
        logger.error(f"Error placing order: {str(e)}")
        raise