# IBKR Portfolio Tracker (Demo)

A demo version of a robust **Interactive Brokers (IBKR)** portfolio tracking bot that syncs portfolio data to **Google Sheets** and sends **Telegram alerts** for portfolio updates. **This demo is limited to 2 positions and 5-minute updates. Contact me for the full version with real-time tracking and advanced features.**

## Features (Demo)
- Tracks up to 2 portfolio positions from IBKR.
- Updates Google Sheets with portfolio data every 5 minutes.
- Sends Telegram alerts for significant P&L changes (with demo note).
- Built with Python and `ib_insync` for reliability and transparency.

## Use Cases
- Retail traders testing IBKR portfolio automation.
- Fund managers exploring portfolio monitoring solutions.
- Algo traders evaluating integration with trading strategies.

## Setup Instructions
1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Configure Google Sheets API**:
   - Create a Google Cloud Project.
   - Enable Google Sheets and Drive APIs.
   - Download `credentials.json` and share your sheet with the service account.
3. **Set Up IBKR**:
   - Run TWS or IB Gateway with API access enabled (port 7497 for paper, 7496 for live).
4. **Configure Telegram**:
   - Create a Telegram bot via BotFather and obtain the token.
   - Get your chat ID.
5. **Update Configuration**:
   - Edit `config/config.ini` with your Google Sheet ID, Telegram token, and chat ID.
6. **Run the Demo**:
   - Place `credentials.json` in the root folder.
   - Run: `python ibkr_portfolio_tracker.py`

## Demo Limitations
- Tracks only the first 2 portfolio positions.
- Updates Google Sheet every 5 minutes.
- Limited alert customization.
- **Contact me** for the full version with real-time updates and all positions.

## Contact for Full Version
Reach out for the full version or customizations:  
- [Fiverr](https://www.fiverr.com/jahanzaib313110)  
- [Telegram](https://t.me/JanzebBlockdev)

## Contributing
- Star this repository to support the project.
- Submit issues for feedback (full version requests preferred).
- Contact me for collaboration opportunities.

---
⭐ **Star this repo** to support the demo and get the full version! ⭐
