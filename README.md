# Binance Futures Order Bot

A professional CLI-based trading bot for Binance USDT-M Futures supporting multiple order types with robust logging, validation, and documentation.

## 🎯 Features

### Core Orders (Mandatory)
- ✅ **Market Orders** - Instant execution at current market price
- ✅ **Limit Orders** - Execute at specified price or better

### Advanced Orders (Bonus)
- ✅ **Stop-Limit Orders** - Trigger limit order when stop price is reached
- ✅ **OCO (One-Cancels-the-Other)** - Simultaneous take-profit and stop-loss
- ✅ **TWAP (Time-Weighted Average Price)** - Split large orders over time
- ✅ **Grid Trading Strategy** - Automated buy-low/sell-high in price range

### Additional Features
- ✅ Input validation for all parameters
- ✅ Structured logging with timestamps
- ✅ Error handling and retry logic
- ✅ Testnet support for safe testing
- ✅ Comprehensive CLI interface

## 📁 Project Structure

```
binance_bot/
│
├── bot.py                      # Main CLI entry point
├── requirements.txt            # Python dependencies
├── .env.example               # Environment template
├── bot.log                    # Execution logs
├── README.md                  # This file
│
└── src/                       # Source code
    ├── __init__.py
    ├── config.py              # API configuration
    ├── logger.py              # Logging utilities
    ├── validator.py           # Input validation
    ├── market_orders.py       # Market order logic
    ├── limit_orders.py        # Limit order logic
    │
    └── advanced/              # Advanced order types
        ├── __init__.py
        ├── stop_limit.py      # Stop-limit orders
        ├── oco.py             # OCO orders
        ├── twap.py            # TWAP strategy
        └── grid_strategy.py   # Grid trading
```

## 🚀 Setup Instructions

### 1. Prerequisites
- Python 3.8 or higher
- Binance account with API access
- pip (Python package manager)

### 2. Installation

```powershell
# Clone or extract the project
cd binance_bot

# Install dependencies
pip install -r requirements.txt
```

### 3. API Configuration

#### Get Binance API Credentials

**For Testnet (Recommended for testing):**
1. Go to https://testnet.binancefuture.com/
2. Click "Generate HMAC_SHA256 Key"
3. Save your API Key and Secret Key

**For Production:**
1. Log in to Binance
2. Go to API Management
3. Create a new API key
4. Enable "Enable Futures" permission
5. Save your API Key and Secret Key

#### Configure Environment

```powershell
# Copy the example environment file
copy .env.example .env

# Edit .env with your API credentials
notepad .env
```

Update `.env` with your credentials:
```
BINANCE_API_KEY=your_actual_api_key_here
BINANCE_API_SECRET=your_actual_secret_key_here
TESTNET=True  # Set to False for production
```

⚠️ **Important**: Never commit your `.env` file to version control!

### 4. Verify Installation

```powershell
# Test the bot
python bot.py help
```

## 📖 Usage Guide

### Basic Commands

#### Market Orders
Execute immediately at current market price.

```powershell
python bot.py market BTCUSDT BUY 0.01
python bot.py market ETHUSDT SELL 0.1
```

#### Limit Orders
Execute at specified price or better.

```powershell
python bot.py limit BTCUSDT BUY 0.01 50000
python bot.py limit ETHUSDT SELL 0.1 3500 GTC
```

### Advanced Orders

#### Stop-Limit Orders
Trigger a limit order when stop price is reached.

```powershell
# Place stop-loss for a long position
python bot.py stop-limit BTCUSDT SELL 0.01 49000 48500

# Parameters: SYMBOL SIDE QUANTITY STOP_PRICE LIMIT_PRICE [TIME_IN_FORCE]
```

**Use Cases:**
- Stop-loss on long: SELL with stop_price < current_price
- Stop-loss on short: BUY with stop_price > current_price

#### OCO Orders
Place take-profit and stop-loss simultaneously.

```powershell
# Exit a long position with TP and SL
python bot.py oco BTCUSDT SELL 0.01 55000 49000

# Parameters: SYMBOL SIDE QUANTITY TAKE_PROFIT STOP_LOSS
```

**Note**: When one order executes, manually cancel the other.

#### TWAP Strategy
Split large orders into smaller chunks over time.

```powershell
# Buy 0.1 BTC split into 5 orders, 60 seconds apart
python bot.py twap BTCUSDT BUY 0.1 5 60 MARKET

# Parameters: SYMBOL SIDE TOTAL_QTY NUM_ORDERS INTERVAL_SEC [ORDER_TYPE]
```

**Benefits:**
- Reduces market impact
- Better average price
- Ideal for large orders

#### Grid Trading
Automated buy-low/sell-high within price range.

```powershell
# Create a grid between 48000-52000 with 10 levels
python bot.py grid BTCUSDT 48000 52000 10 0.01

# Parameters: SYMBOL LOWER_PRICE UPPER_PRICE GRID_LEVELS QTY_PER_GRID
```

**Best For:**
- Ranging/sideways markets
- Automated trading
- Capturing price oscillations

### Alternative: Direct Module Execution

You can also run individual modules directly:

```powershell
# Market order
python src/market_orders.py BTCUSDT BUY 0.01

# Limit order
python src/limit_orders.py BTCUSDT BUY 0.01 50000 GTC

# Advanced orders
python src/advanced/stop_limit.py BTCUSDT SELL 0.01 52000 51500
python src/advanced/oco.py BTCUSDT SELL 0.01 55000 49000
python src/advanced/twap.py BTCUSDT BUY 0.1 5 60 MARKET
python src/advanced/grid_strategy.py BTCUSDT 48000 52000 10 0.01
```

## 📊 Logging

All bot operations are logged to `bot.log` with structured format:

```
2025-12-03 14:30:45 | INFO     | BinanceBot | Order placed successfully | order_type=MARKET | symbol=BTCUSDT | side=BUY | quantity=0.01 | status=SUCCESS | order_id=123456
```

### Log Levels
- **INFO**: Successful operations
- **WARNING**: Non-critical issues
- **ERROR**: Failed operations with details
- **DEBUG**: Detailed execution flow

### Viewing Logs

```powershell
# View entire log
type bot.log

# View last 20 lines
Get-Content bot.log -Tail 20

# Follow log in real-time
Get-Content bot.log -Wait
```

## 🔒 Security Best Practices

1. **API Keys**
   - Never hardcode API keys in source code
   - Use `.env` file for credentials
   - Add `.env` to `.gitignore`
   - Use testnet for development

2. **API Permissions**
   - Only enable "Enable Futures" permission
   - Do not enable withdrawal permissions
   - Use IP whitelist if possible

3. **Testing**
   - Always test on testnet first
   - Start with small quantities
   - Verify order parameters before execution

## 🧪 Testing

### Using Binance Testnet

1. Set `TESTNET=True` in `.env`
2. Get testnet credentials from https://testnet.binancefuture.com/
3. Testnet provides free test USDT for trading

### Test Checklist

- [ ] Market order execution
- [ ] Limit order placement and cancellation
- [ ] Stop-limit order trigger
- [ ] OCO order pair placement
- [ ] TWAP execution over time
- [ ] Grid strategy creation
- [ ] Input validation for invalid parameters
- [ ] Error handling for API failures
- [ ] Log file generation

## 🐛 Troubleshooting

### Common Issues

**1. API Key Error**
```
Error: API credentials not found
```
**Solution**: Ensure `.env` file exists with valid credentials

**2. Connection Error**
```
Error: Failed to connect to Binance API
```
**Solution**: Check internet connection and API endpoint

**3. Invalid Symbol**
```
Error: Invalid symbol format
```
**Solution**: Use valid USDT-M futures pairs (e.g., BTCUSDT, ETHUSDT)

**4. Insufficient Balance**
```
Error: Insufficient balance
```
**Solution**: Ensure you have enough USDT in futures wallet

**5. Order Size Too Small**
```
Error: Quantity below minimum
```
**Solution**: Check symbol's minimum order quantity on Binance

## 📚 API Reference

### Order Parameters

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| SYMBOL | string | Trading pair | BTCUSDT |
| SIDE | string | BUY or SELL | BUY |
| QUANTITY | float | Order quantity | 0.01 |
| PRICE | float | Limit price | 50000 |
| STOP_PRICE | float | Stop trigger price | 49000 |
| TIME_IN_FORCE | string | GTC, IOC, FOK | GTC |

### Time in Force Options

- **GTC** (Good Till Cancel): Order remains until filled or cancelled
- **IOC** (Immediate or Cancel): Fill immediately, cancel remainder
- **FOK** (Fill or Kill): Fill completely or cancel entire order

## 🔗 Resources

- [Binance Futures API Documentation](https://binance-docs.github.io/apidocs/futures/en/)
- [Binance Testnet](https://testnet.binancefuture.com/)
- [Project Repository](https://github.com/[your_username]/binance_bot)

## 📝 Assignment Compliance

This project fulfills all assignment requirements:

### Core Orders (50%)
- ✅ Market orders with validation
- ✅ Limit orders with validation

### Advanced Orders (30%)
- ✅ Stop-Limit orders
- ✅ OCO orders
- ✅ TWAP strategy
- ✅ Grid trading strategy

### Logging & Errors (10%)
- ✅ Structured `bot.log` with timestamps
- ✅ Comprehensive error traces
- ✅ All operations logged

### Report & Documentation (10%)
- ✅ Clear README.md with setup instructions
- ✅ Usage examples for all order types
- ✅ API configuration guide
- ✅ Troubleshooting section

## 📄 License

This project is created for educational purposes as part of a Python developer assignment.

## 👤 Author

[Your Name]  
Submission Date: [Date]  
Assignment: Binance Futures Order Bot

---

**⚠️ Disclaimer**: This bot is for educational purposes. Trading cryptocurrencies involves significant risk. Always test thoroughly on testnet before using with real funds.

