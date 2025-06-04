IBKR Portfolio Tracker (Demo)
A demo version of a powerful Interactive Brokers (IBKR) portfolio tracking bot that syncs real-time data to Google Sheets and sends Telegram alerts for portfolio updates. This is a demo with limited functionality (2 positions, 5-minute updates). Contact me for the full version!
🚀 Features (Demo)

Real-Time Portfolio Tracking: Fetches up to 2 positions from IBKR.
Google Sheets Sync: Updates a Google Sheet with portfolio data every 5 minutes.
Telegram Alerts: Notifies for significant P&L changes (with demo note).
Open-Source Demo: Built with Python and ib_insync for transparency.


📊 Use Cases

Retail traders testing IBKR portfolio tracking.
Fund managers exploring automation.
Algo traders evaluating integration potential.

🛠️ Setup Instructions

Install Dependencies:pip install -r requirements.txt


Set Up Google Sheets API:
Create a Google Cloud Project.
Enable Google Sheets and Drive APIs.
Download credentials.json and share your sheet with the service account.


Configure IBKR:
Run TWS or IB Gateway with API access (port 7497 for paper, 7496 for live).


Configure Telegram:
Create a Telegram bot via BotFather and get the token.
Get your chat ID.


Update Config:
Edit config/config.ini with your Google Sheet ID, Telegram token, and chat ID.


Run the Demo:
Place credentials.json in the root folder.
Run: python ibkr_portfolio_tracker.py



📸 Screenshots

⚠️ Demo Limitations

Tracks only the first 2 portfolio positions.
Updates Google Sheet every 5 minutes.
Limited alert customization.
Contact me for the full version with real-time updates, all positions, and advanced features!

📬 Contact for Full Version
Reach out on these platforms for the full version or customizations:  


Telegram  
Fiverr  
LinkedIn  
Website  

🤝 Contributing

Star this repo ⭐ to support the project.
Submit issues for feedback (full version requests preferred).
Contact me for collaboration.



⭐ Star this repo to support the demo and get the full version! ⭐
