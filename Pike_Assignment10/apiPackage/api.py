# api

# Name: Connor MacFarland, Greyson Barber
# email: macfarct@mail.uc.edu, barbergn@mail.uc.edu
# Assignment Number: Assignment 010
# Due Date:  11/14/2024
# Course #/Section:   IS 4010- 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  execute an API call using a Url in groups 
# Brief Description of what this module does: Main package takes the API key and fetches the data to build a statement. 
# Anything else that's relevant: 
# Citations W3Schools, Stackoverflow

import requests
import json
import csv

class StockDataAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.stockdata.org/v1/data/quote"
    
    def build_url(self, symbols):
        
        url = f"{self.base_url}?symbols={symbols}&api_token={self.api_key}"
        return url
    
    def fetch_data(self, symbols):
        
        url = self.build_url(symbols)
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None
    
    def parse_data(self, data):
       
        if data and 'data' in data:
            stock_data = []
            for item in data['data']:
                stock = {
                    'symbol': item.get('symbol', ''),
                    'name': item.get('name', ''),
                    'price': item.get('price', ''),
                    'change': item.get('change', ''),
                    'percent_change': item.get('percent_change', '')
                }
                stock_data.append(stock)
            return stock_data
        return []
    
    def save_to_csv(self, data, filename="stock_data.csv"):
        
        keys = data[0].keys() if data else []
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        print(f"Data saved to {filename}")
