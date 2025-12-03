# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Install Dependencies (1 min)
```powershell
cd C:\Users\Leena\binance_bot
pip install -r requirements.txt
```

### Step 2: Setup API Keys (2 min)

**Get Testnet Keys** (Recommended):
1. Visit: https://testnet.binancefuture.com/
2. Click "Generate HMAC_SHA256 Key"
3. Copy your API Key and Secret

**Configure .env**:
```powershell
copy .env.example .env
notepad .env
```

Paste your keys:
```
BINANCE_API_KEY=your_testnet_api_key_here
BINANCE_API_SECRET=your_testnet_secret_key_here
TESTNET=True
```

### Step 3: Test the Bot (2 min)

```powershell
# View help
python bot.py help

# Test market order (on testnet)
python bot.py market BTCUSDT BUY 0.001

# Test limit order
python bot.py limit BTCUSDT BUY 0.001 40000

# Test TWAP
python bot.py twap BTCUSDT BUY 0.005 3 10 MARKET

# Test grid strategy
python bot.py grid BTCUSDT 45000 55000 5 0.001
```

### Step 4: Check Logs
```powershell
type bot.log
```

## ✅ You're Ready!

Now you can:
- Execute all order types
- View logs in `bot.log`
- Refer to `README.md` for detailed documentation
- Use `REPORT_TEMPLATE.md` for creating your report

## 🎯 Next Steps for Submission

1. **Test all order types** on Binance testnet
2. **Take screenshots** of executions
3. **Create report.pdf** using REPORT_TEMPLATE.md
4. **Zip the project**:
   ```powershell
   Compress-Archive -Path "C:\Users\Leena\binance_bot\*" -DestinationPath "C:\Users\Leena\[your_name]_binance_bot.zip"
   ```

5. **Push to GitHub**:
   ```powershell
   cd C:\Users\Leena\binance_bot
   git init
   git add .
   git commit -m "Initial commit: Binance Futures Bot"
   git remote add origin https://github.com/[your_username]/[your_name]-binance-bot.git
   git push -u origin main
   ```

## 📋 Submission Checklist

- [ ] All dependencies installed
- [ ] API keys configured
- [ ] All order types tested
- [ ] Screenshots captured
- [ ] `report.pdf` created
- [ ] `.zip` file created
- [ ] GitHub repository created and pushed
- [ ] Instructor added as collaborator

## 🆘 Need Help?

Check `README.md` → Troubleshooting section

