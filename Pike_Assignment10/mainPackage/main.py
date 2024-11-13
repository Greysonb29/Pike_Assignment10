# main.py

# Name: Connor MacFarland, Greyson Barber
# email: macfarct@mail.uc.edu, barbergn@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:  11/13/2024
# Course #/Section:   IS 4010- 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment: Execute an API call using a URL in a group project.
# Brief Description of what this module does:  the main.py recieves the results from the API database and prints it then writes to a csv file. 
# Anything else that's relevant: 
# Citation: W3 Schools, https://stackoverflow.com/questions/49593657/how-to-call-an-api-using-python-requests-library, geeksforgeeks, JSon inclass. 




from apiPackage.api import *

def main():
   
    api_key = "vgg4voSVVpnB23VfZDo0wW4oB5h1Fv9MgdGd9pyy"
   
    stock_data_api = StockDataAPI(api_key)
   
    symbols = "AAPL,MSFT,TSLA"
    data = stock_data_api.fetch_data(symbols)
   
    parsed_data = stock_data_api.parse_data(data)
   
    if parsed_data:
        for stock in parsed_data:
            print(f"{stock['name']} ({stock['symbol']}): {stock['price']} USD "
                  f"Change: {stock['change']} ({stock['percent_change']}%)")
   
    stock_data_api.save_to_csv(parsed_data)

if __name__ == "__main__":
    main()