import requests
import argparse

# Instantiate the parser
parser = argparse.ArgumentParser(description='Optional app description')

# Required positional argument
parser.add_argument('sharif_usr', type=str,
                    help='A required integer positional argument')
                    
# Required positional argument
parser.add_argument('sharif_pass', type=str,
                    help='A required integer positional argument')

args = parser.parse_args()


headers = {
    'Origin': 'https://net2.sharif.edu',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'Referer': 'https://net2.sharif.edu/login',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

data = {
    'username': args.sharif_usr,
    'password': args.sharif_pass,
}

response = requests.post('https://net2.sharif.edu/login', headers=headers, data=data)

if not response:
    print("UNKNOWN ERROR: No Response!")
elif "You are logged in" in response.text:
    print("The IP Assigned Successfully!")
else:
    print(f"Login Failed! Please check your username and password")
