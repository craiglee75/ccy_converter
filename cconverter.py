# Currency Converter

import requests

ccy_from = input('What ccy do you hold: ').lower()
ccy_tolist = ['eur', 'usd']
ex_rates = {}


def new_cache():
    global ccy_tolist, ex_rates
    for ccy in ccy_tolist:
        url = f'http://www.floatrates.com/daily/{ccy}.json'
        response = requests.get(url).json()
        ex_rates[str(ccy)] = response


new_cache()
while True:
    ccy_to = input('What ccy would you like to exchange (enter of exit to stop): ').lower()
    if ccy_to == '' or ccy_to == 'exit':
        break
    else:
        amount = int(input(f'How much {ccy_from} would you like to convert: '))
        print('Checking the cache...')
        if ccy_to in ccy_tolist:
            print('Oh! It is in the cache!')
            result = amount / ex_rates[ccy_to][ccy_from]['rate']
            print(f'You received {round(result, 2)} {ccy_to.upper()}.')
        else:
            print('Sorry, but it is not in the cache!')
            ccy_tolist.append(ccy_to)
            new_cache()
            result = amount / ex_rates[ccy_to][ccy_from]['rate']
            print(f'You received {round(result, 2)} {ccy_to.upper()}.')
