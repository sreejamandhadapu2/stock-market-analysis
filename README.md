Stock Market Data Retrieval & Analysis using Google Sheets 
What’s this project about? 
This project helps you easily fetch stock market data and store it in Google Sheets. Using the Twelve Data API, it pulls historical data and saves it for analysis. You can then visualize this data with Tableau for some powerful insights!

There are two sheets that get updated:

FetchStockData – This is where the stock data goes.

Sheet1 – A backup copy of all the data from the main sheet.

What does it do? 
Fetches historical stock data (you can choose multiple companies)

Automatically stores data in your Google Sheets

Handles missing data and API errors gracefully

Adds delays to prevent hitting API rate limits

Makes it easy to visualize data in Tableau 

What do I need to get started? 
Before you run the script, you’ll need:

A Google Sheets document (don’t worry, just create a new one if you don’t have it!)

An API key from Twelve Data – get it here

How to set it up 
Step 1: Open Google Sheets Apps Script
Open your Google Sheets document.

Click on Extensions > Apps Script.

Step 2: Add the Script
Copy and paste the fetchStockData.js script into the Apps Script editor.

Replace 'YOUR_TWELVE_DATA_API_KEY' with your API key.

Hit Save and you’re all set.

Step 3: Run the Script
In the Apps Script editor, click Run > fetchStockData.

Grant the permissions it asks for (don’t worry, it’s all secure).

The stock data will be fetched and stored in the FetchStockData and Sheet1 sheets.

Visualize the data with Tableau 
To bring your Google Sheets data into Tableau:

Open Tableau Desktop.

Click Connect > Google Sheets.

Choose your Google Sheets file and click Open.

Click Update to refresh the data.

Troubleshooting 
Getting API Limit Errors 
Twelve Data’s free plan allows 8 requests per minute, so the script waits 9 seconds between requests to avoid hitting that limit.

If you need more requests, consider upgrading to a paid plan.

Data not updating in Tableau? 
In Tableau, click Refresh to reload data from Google Sheets.

Make sure Google Sheets API permissions are set up.

Future Updates 
What’s coming soon?
Automated daily updates – The script will run every day on its own!

More advanced stock indicators (like moving averages, RSI, etc.)

A fancy stock data dashboard in Tableau! 