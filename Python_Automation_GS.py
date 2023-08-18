import yfinance as yf
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import matplotlib.pyplot as plt

# Replace with your top 20 stock symbols
top_stocks = ["AAPL", "GOOGL", "AMZN", "MSFT", "TSLA", "NVDA", "NFLX", "PYPL", "AMGN", "ADBE", "COST", "INTC",
              "CMCSA", "PEP", "AVGO", "CSCO", "TXN", "QCOM", "CHTR"]

# Fetch hourly data using yfinance
def fetch_stock_data(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1d", interval="1h")
    return data

# Authenticate and write data to Google Sheets
def write_to_google_sheets(data, symbol):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("python-automation-program-gs-89544358d26f.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open("Stock Data and Graphs")
    worksheet = sheet.get_worksheet(0)

    next_row = len(worksheet.get_all_values()) + 1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    values = [timestamp, symbol] + data["Close"].tolist()
    worksheet.insert_row(values, next_row)

# Plot stock price graph and write to Google Sheets
def plot_and_write_graph(data, symbol):
    plt.figure(figsize=(10, 6))
    data.plot()
    plt.title(f"{symbol} Stock Price Movement")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.grid(True)

    image_path = f"{symbol}_plot.png"
    plt.savefig(image_path)
    plt.close()

    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("python-automation-program-gs-89544358d26f.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open("Stock Data and Graphs")
    worksheet = sheet.add_worksheet(title=symbol, rows="100", cols="20")

    worksheet.update("A1", f"={image_path}")

# Main function
def main():
    for symbol in top_stocks:
        data = fetch_stock_data(symbol)
        write_to_google_sheets(data, symbol)
        plot_and_write_graph(data, symbol)

if __name__ == "__main__":
    main()
