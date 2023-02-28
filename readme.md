# Python Ticker Powered by PyCoinGecko

## How to Use It
There is a list at the top of the Python file called tokenTickers. Each string in this array is going to be put through the price call, then formatted into a print statement that
loops until the end of the list and continues in an infinite While loop pausing for 7 seconds after each array is completed. You can edit this to do many different things, such as alert you at certain prices via SMTP, trigger a request if you have access to a trading API, or loop until a certain key is pressed and then accept a new list from the user.

## Dependencies
The only dependency in this project is the CoinGecko API. Install this using pip install pycoingecko in the directory of your project. You can find out more information on the module [here](https://pypi.org/project/pycoingecko/). The API documentation can be found [here](https://www.coingecko.com/en/api/documentation)

## Limitations
The time module is used liberally in this ticker to find a balance of getting a live feed while not passing the API request limit and keeping the feed readable. This also helps hide the limitations of using this for large amounts of data collection. So with that said, while there is a free plan by default that requires no API key and allows for ~30 requests/minute, there are CoinGecko API plans that can be found [here](https://www.coingecko.com/en/api/pricing_2) if you are looking for something more heavy duty. Another limitation is that due to using CoinGecko for the API, we are only getting their data that they aggregate for their website and analytics services.