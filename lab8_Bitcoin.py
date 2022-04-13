import requests
from urllib import response
from pprint import pprint



def main():
  
  Bitcoin = get_dollar_amount()
  BitcoinEx = convert_Bit_rate()
  display_result(Bitcoin, BitcoinEx)
    
def get_dollar_amount():
    bitcoin = float(input('Enter the number of bitcoin: '))
    return bitcoin

def request_bitcoin():

    coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

    response = requests.get(coindesk_url)

    data = response.json()
    
    return data
   
    
def convert_Bit_rate():
    data = request_bitcoin()
    Bitcoin_exchange_rate = data['bpi']['USD']['rate_float']
    return Bitcoin_exchange_rate
      
def get_calculate(Bitcoin, BitcoinEx):
    convertAmount =  Bitcoin * BitcoinEx

    return convertAmount

def display_result(Bitcoin, BitcoinEx ):

    conventAmount = get_calculate(Bitcoin, BitcoinEx)

   
    print(f'{Bitcoin} Bitcooin is equivalent to ${conventAmount}')
    
  

if __name__ == '__main__':
    main()

