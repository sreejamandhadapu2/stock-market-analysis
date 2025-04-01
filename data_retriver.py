function fetchStockData() {
  const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = spreadsheet.getSheetByName("FetchStockData");
  let sheet1 = spreadsheet.getSheetByName("Sheet1");

  // If sheets don't exist, create them
  if (!sheet) {
    sheet = spreadsheet.insertSheet("FetchStockData");
    Logger.log("✅ Created missing sheet: 'FetchStockData'");
  }
  if (!sheet1) {
    sheet1 = spreadsheet.insertSheet("Sheet1");
    Logger.log("✅ Created missing sheet: 'Sheet1'");
  }

  const symbols = ['AAPL', 'GOOGL', 'AMZN', 'MSFT', 'TSLA']; // Add up to 10 stock symbols
  const apiKey = '2af99f5a04ee4655a9e1aae40f483c21'; // Replace with your actual Twelve Data API key
  const urlBase = 'https://api.twelvedata.com/time_series';

  const startDate = new Date('2025-01-01'); // Fetch data from Jan 1, 2025
  const today = new Date();
  today.setDate(today.getDate() - 1); // Get yesterday’s date

  // Clear both sheets before inserting new data
  sheet.clear();
  sheet1.clear();

  // Add headers to both sheets
  const headers = ["Symbol", "Date", "Open", "High", "Low", "Close", "Volume"];
  sheet.appendRow(headers);
  sheet1.appendRow(headers);

  Logger.log("🚀 Starting stock data update process...");
  Logger.log(`📅 Fetching data from ${startDate.toISOString().split('T')[0]} to ${today.toISOString().split('T')[0]}`);

  symbols.forEach(function(symbol, index) {
    const url = `${urlBase}?symbol=${symbol}&interval=1day&outputsize=5000&apikey=${apiKey}`;

    // Avoid hitting API rate limits (Twelve Data free plan allows 8 requests per minute)
    if (index > 0) Utilities.sleep(9000); // Wait 9 seconds before next request

    Logger.log(`🔍 Fetching stock data for ${symbol}...`);

    try {
      const response = UrlFetchApp.fetch(url, {
        'muteHttpExceptions': true,
        'headers': { 'Cache-Control': 'no-cache, no-store, must-revalidate' }
      });

      const json = JSON.parse(response.getContentText());

      if (json.values) {
        const stockData = json.values;

        stockData
          .filter(data => {
            let currentDate = new Date(data.datetime);
            return currentDate >= startDate && currentDate <= today;
          })
          .sort((a, b) => new Date(a.datetime) - new Date(b.datetime))
          .forEach(data => {
            const row = [
              symbol,
              data.datetime, // Date
              data.open,
              data.high,
              data.low,
              data.close,
              data.volume
            ];
            sheet.appendRow(row);
            sheet1.appendRow(row); // Copy same data to "Sheet1"
          });

        Logger.log(`✅ Data for ${symbol} updated successfully.`);
      } else {
        Logger.log(`❌ Error: No stock data found for ${symbol}.`);
        Logger.log(`🔍 Full API Response: ${JSON.stringify(json)}`);
      }
    } catch (error) {
      Logger.log(`🚨 API Request Failed for ${symbol}: ${error}`);
    }
  });

  Logger.log("🎯 Stock data update process completed!");
}
