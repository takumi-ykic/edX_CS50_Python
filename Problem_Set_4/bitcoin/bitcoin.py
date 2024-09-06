import requests
import sys
import json

try:
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)
    else:
        try:
            num = float(sys.argv[1])
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            data = json.loads(response.text)
            price = data["bpi"]["USD"]["rate_float"]

            total = price * num
            print(f"${total:,.4f}")
        except ValueError:
            print("Command-line argument is not a number")
            sys.exit(1)
except requests.RequestException:
    ...
