import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Load credentials from the downloaded JSON file
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("python-automation-program-gs-89544358d26f.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet by its title
sheet = client.open("Stock Data and Graphs")

# Access a specific worksheet by title or index
worksheet = sheet.get_worksheet(0)  # Replace with your worksheet's index or title

# Write data to the sheet
data = [["Timestamp", "Stock A", "Stock B", ...],  # Header row
        ["2023-01-01 14:00:00", 100.00, 150.00, ...],  # Example data
        # ... Add more rows of data ...
       ]
worksheet.insert_rows(data, row=1)  # Insert data starting from the first row

# Close the worksheet
worksheet.update_acell("A1", "Last Updated: " + str(datetime.now()))

# # Access a different worksheet for the graph (sheet2)
# graph_worksheet = sheet.add_worksheet(title="Graph Data", rows="100", cols="20")
#
# # Write graph data to the new worksheet
# graph_data = [["Timestamp", "Stock A Rise/Fall", "Stock B Rise/Fall", ...],  # Header row
#               ["2023-01-01 14:00:00", "+5.00%", "-2.50%", ...],  # Example data
#               # ... Add more rows of data ...
#              ]
# graph_worksheet.insert_rows(graph_data, row=1)
#
# # Done!
