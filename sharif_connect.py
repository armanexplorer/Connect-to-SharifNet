#!/usr/bin/env python3

import argparse
from urllib.error import HTTPError, URLError
from urllib.request import urlopen, Request
from urllib.parse import urlencode

CRED_PATH = 'credentials.txt'
LOGIN_URL = 'https://net2.sharif.edu/login'

username , password = None, None

# Instantiate the parser
parser = argparse.ArgumentParser(description='Optional app description')

# Optional keyword argument
parser.add_argument('--username', type=str,
                    help='An optional string keyword argument')
                    
# Optional keyword argument
parser.add_argument('--password', type=str,
                    help='An optional string keyword argument')

args = parser.parse_args()

if args.username and args.password:
    try:
        username , password = args.username, args.password
        print("Username and password from console argumants will be used to login...")
    except:
        pass
    
    
if username is None or password is None:
    try:
        with open(CRED_PATH, "r") as f:
            l1, l2 = f.readlines()
            username = l1.strip().split("=")[-1]
            password = l2.strip().split("=")[-1]
    
    except FileNotFoundError:
        pass
    except Exception:
        pass
    else:
        print("Username and password from credentials file will be used to login...")
 

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
    'username': username,
    'password': password,
}

response = None
data = urlencode(data).encode("utf-8")

request = Request(LOGIN_URL, headers=headers or {}, data=data)

try:
    with urlopen(request, timeout=10) as response:
        response = response.read().decode("utf-8")
except HTTPError as error:
    print(error.status, error.reason)
except URLError as error:
    print(error.reason)
except TimeoutError:
    print("Request timed out")
    

if not response:
    print("UNKNOWN ERROR: No Response!")
elif "You are logged in" in response:
    print("Done! (The IP Assigned Successfully)")
else:
    print(f"Login Failed! Please check your username and password")

