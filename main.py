# This is a sample Python script.

from ccxt.base.exchange import Exchange
from dotenv import dotenv_values

basestring = str


config = dotenv_values(".env")

print(config)
key = config['API_KEY']
secret = config['API_SECRET']


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    x = 1
    y = 2
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
