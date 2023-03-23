import sys
import requests

try:
    n = sys.argv[1]
    n = float(n)

    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    rate = data['bpi']['USD']['rate']


    f_rate = float(rate.replace(',', ''))
    print(f_rate)

    result = f_rate * n
    print(f'${result:,.4f}')

except ValueError:
    sys.exit('Command-line argument is not a number')

except IndexError:
    sys.exit('Missing command-line argument')