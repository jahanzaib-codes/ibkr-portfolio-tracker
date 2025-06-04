from ib_insync import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from telegram import Bot
import asyncio
import pandas as pd
from datetime import datetime
import configparser

# Load configuration
config = configparser.ConfigParser()
config.read('config/config.ini')

# Configuration
IBKR_HOST = config['IBKR']['host']
IBKR_PORT = int(config['IBKR']['port'])
IBKR_CLIENT_ID = int(config['IBKR']['client_id'])
GOOGLE_SHEET_ID = config['GoogleSheets']['sheet_id']
CREDENTIALS_FILE = config['GoogleSheets']['credentials_file']
TELEGRAM_TOKEN = config['Telegram']['token']
TELEGRAM_CHAT_ID = config['Telegram']['chat_id']
UPDATE_INTERVAL = 300  # Demo: Update every 5 minutes
PNL_THRESHOLD = float(config['Settings']['pnl_threshold'])

# Google Sheets Setup
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
client = gspread.authorize(creds)
sheet = client.open_by_key(GOOGLE_SHEET_ID).sheet1

# Telegram Bot Setup
telegram_bot = Bot(token=TELEGRAM_TOKEN)

# IBKR Connection
ib = IB()
ib.connect(IBKR_HOST, IBKR_PORT, clientId=IBKR_CLIENT_ID)

async def send_telegram_message(message):
    """Send a message to Telegram."""
    await telegram_bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

def get_portfolio_data():
    """Fetch portfolio data from IBKR (Demo: Limited to 2 positions)."""
    portfolio = ib.portfolio()[:2]  # Demo: Limit to first 2 positions
    data = []
    for item in portfolio:
        contract = item.contract
        position = item.position
        market_price = item.marketPrice
        unrealized_pnl = item.unrealizedPNL
        realized_pnl = item.realizedPNL
        data.append({
            'Symbol': contract.symbol,
            'Position': position,
            'Market Price': market_price,
            'Unrealized P&L': unrealized_pnl,
            'Realized P&L': realized_pnl
        })
    return pd.DataFrame(data)

def update_google_sheet(df):
    """Update Google Sheet with portfolio data."""
    sheet.clear()
    sheet.update([df.columns.values.tolist()] + df.values.tolist())

async def main():
    """Main loop for demo (limited functionality)."""
    last_pnl = None
    while True:
        try:
            df = get_portfolio_data()
            if df.empty:
                print("No portfolio data available.")
                await asyncio.sleep(UPDATE_INTERVAL)
                continue

            total_pnl = df['Unrealized P&L'].sum() + df['Realized P&L'].sum()
            update_google_sheet(df)
            print(f"Updated Google Sheet at {datetime.now()} (Demo Mode)")

            if last_pnl is not None and abs(total_pnl - last_pnl) > PNL_THRESHOLD:
                message = f"Demo Portfolio Update:\nTotal P&L: ${total_pnl:.2f}\nChange: ${total_pnl - last_pnl:.2f}\nContact for full version!"
                await send_telegram_message(message)
            last_pnl = total_pnl

        except Exception as e:
            error_msg = f"Demo Error: {str(e)}\nContact for full version!"
            print(error_msg)
            await send_telegram_message(error_msg)

        await asyncio.sleep(UPDATE_INTERVAL)

if __name__ == "__main__":
    print("Starting IBKR Portfolio Tracker (Demo Mode)...")
    ib.run(asyncio.run(main()))