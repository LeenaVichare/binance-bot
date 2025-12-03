"""
Binance Futures Order Bot - Main CLI Interface
Unified entry point for all order types
"""

import sys
from src.market_orders import MarketOrderExecutor
from src.limit_orders import LimitOrderExecutor
from src.advanced.stop_limit import StopLimitOrderExecutor
from src.advanced.oco import OCOOrderExecutor
from src.advanced.twap import TWAPExecutor
from src.advanced.grid_strategy import GridStrategyExecutor
from src.logger import bot_logger

def print_help():
    """Print help message with usage instructions"""
    help_text = """
Binance Futures Order Bot - CLI Interface
==========================================

CORE ORDERS:
  python bot.py market <SYMBOL> <SIDE> <QUANTITY>
    Example: python bot.py market BTCUSDT BUY 0.01

  python bot.py limit <SYMBOL> <SIDE> <QUANTITY> <PRICE> [TIME_IN_FORCE]
    Example: python bot.py limit BTCUSDT BUY 0.01 50000 GTC

ADVANCED ORDERS:
  python bot.py stop-limit <SYMBOL> <SIDE> <QUANTITY> <STOP_PRICE> <LIMIT_PRICE> [TIME_IN_FORCE]
    Example: python bot.py stop-limit BTCUSDT SELL 0.01 52000 51500

  python bot.py oco <SYMBOL> <SIDE> <QUANTITY> <TAKE_PROFIT> <STOP_LOSS>
    Example: python bot.py oco BTCUSDT SELL 0.01 55000 49000

  python bot.py twap <SYMBOL> <SIDE> <TOTAL_QUANTITY> <NUM_ORDERS> <INTERVAL_SEC> [ORDER_TYPE]
    Example: python bot.py twap BTCUSDT BUY 0.1 5 60 MARKET

  python bot.py grid <SYMBOL> <LOWER_PRICE> <UPPER_PRICE> <GRID_LEVELS> <QTY_PER_GRID>
    Example: python bot.py grid BTCUSDT 48000 52000 10 0.01

PARAMETERS:
  SYMBOL          - Trading pair (e.g., BTCUSDT, ETHUSDT)
  SIDE            - BUY or SELL
  QUANTITY        - Order quantity
  PRICE           - Limit price
  STOP_PRICE      - Price to trigger stop order
  TAKE_PROFIT     - Take profit price
  STOP_LOSS       - Stop loss price
  NUM_ORDERS      - Number of orders for TWAP
  INTERVAL_SEC    - Seconds between TWAP orders
  GRID_LEVELS     - Number of grid levels
  TIME_IN_FORCE   - GTC (default), IOC, or FOK

For more information, see README.md
"""
    print(help_text)

def main():
    """Main CLI entry point"""
    
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    try:
        if command == 'help' or command == '--help' or command == '-h':
            print_help()
            sys.exit(0)
        
        elif command == 'market':
            if len(sys.argv) < 5:
                print("Usage: python bot.py market <SYMBOL> <SIDE> <QUANTITY>")
                sys.exit(1)
            
            symbol, side, quantity = sys.argv[2], sys.argv[3], sys.argv[4]
            executor = MarketOrderExecutor()
            result = executor.place_market_order(symbol, side, quantity)
            
            print(f"\n✓ Market order placed successfully!")
            print(f"Order ID: {result.get('orderId')}")
            print(f"Executed Quantity: {result.get('executedQty')}")
            print(f"Status: {result.get('status')}")
        
        elif command == 'limit':
            if len(sys.argv) < 6:
                print("Usage: python bot.py limit <SYMBOL> <SIDE> <QUANTITY> <PRICE> [TIME_IN_FORCE]")
                sys.exit(1)
            
            symbol, side, quantity, price = sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
            tif = sys.argv[6] if len(sys.argv) > 6 else 'GTC'
            
            executor = LimitOrderExecutor()
            result = executor.place_limit_order(symbol, side, quantity, price, tif)
            
            print(f"\n✓ Limit order placed successfully!")
            print(f"Order ID: {result.get('orderId')}")
            print(f"Price: {result.get('price')}")
            print(f"Status: {result.get('status')}")
        
        elif command == 'stop-limit' or command == 'stoplimit':
            if len(sys.argv) < 7:
                print("Usage: python bot.py stop-limit <SYMBOL> <SIDE> <QUANTITY> <STOP_PRICE> <LIMIT_PRICE> [TIME_IN_FORCE]")
                sys.exit(1)
            
            symbol, side, quantity = sys.argv[2], sys.argv[3], sys.argv[4]
            stop_price, limit_price = sys.argv[5], sys.argv[6]
            tif = sys.argv[7] if len(sys.argv) > 7 else 'GTC'
            
            executor = StopLimitOrderExecutor()
            result = executor.place_stop_limit_order(symbol, side, quantity, stop_price, limit_price, tif)
            
            print(f"\n✓ Stop-limit order placed successfully!")
            print(f"Order ID: {result.get('orderId')}")
            print(f"Stop Price: {result.get('stopPrice')}")
            print(f"Limit Price: {result.get('price')}")
        
        elif command == 'oco':
            if len(sys.argv) < 7:
                print("Usage: python bot.py oco <SYMBOL> <SIDE> <QUANTITY> <TAKE_PROFIT> <STOP_LOSS>")
                sys.exit(1)
            
            symbol, side, quantity = sys.argv[2], sys.argv[3], sys.argv[4]
            take_profit, stop_loss = sys.argv[5], sys.argv[6]
            
            executor = OCOOrderExecutor()
            result = executor.place_oco_order(symbol, side, quantity, take_profit, stop_loss)
            
            print(f"\n✓ OCO orders placed successfully!")
            print(f"Take-Profit Order ID: {result['take_profit_order'].get('orderId')}")
            print(f"Stop-Loss Order ID: {result['stop_loss_order'].get('orderId')}")
        
        elif command == 'twap':
            if len(sys.argv) < 7:
                print("Usage: python bot.py twap <SYMBOL> <SIDE> <TOTAL_QUANTITY> <NUM_ORDERS> <INTERVAL_SEC> [ORDER_TYPE]")
                sys.exit(1)
            
            symbol, side, total_qty = sys.argv[2], sys.argv[3], float(sys.argv[4])
            num_orders, interval = int(sys.argv[5]), int(sys.argv[6])
            order_type = sys.argv[7] if len(sys.argv) > 7 else 'MARKET'
            
            executor = TWAPExecutor()
            result = executor.execute_twap(symbol, side, total_qty, num_orders, interval, order_type)
            
            print(f"\n✓ TWAP execution completed!")
            print(f"Executed Quantity: {result['total_quantity_executed']}")
            print(f"Average Price: {result['average_price']:.2f}")
            print(f"Orders: {result['num_orders_executed']}/{result['num_orders_requested']}")
        
        elif command == 'grid':
            if len(sys.argv) < 7:
                print("Usage: python bot.py grid <SYMBOL> <LOWER_PRICE> <UPPER_PRICE> <GRID_LEVELS> <QTY_PER_GRID>")
                sys.exit(1)
            
            symbol = sys.argv[2]
            lower, upper = float(sys.argv[3]), float(sys.argv[4])
            levels, qty = int(sys.argv[5]), float(sys.argv[6])
            
            executor = GridStrategyExecutor()
            result = executor.create_grid(symbol, lower, upper, levels, qty)
            
            print(f"\n✓ Grid strategy created!")
            print(f"Total Orders: {result['total_orders_placed']}")
            print(f"Buy Orders: {len(result['buy_orders'])}")
            print(f"Sell Orders: {len(result['sell_orders'])}")
        
        else:
            print(f"Unknown command: {command}")
            print("Use 'python bot.py help' for usage instructions")
            sys.exit(1)
    
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        bot_logger.error(f"Command failed: {command}", error=str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()

