import requests
import argparse


username , password = None, None

try:
    with open(".env", "r") as f:
        r1, r2 = f.readlines()
        username = r1.split("=")[-1]
        password = r2.split("=")[-1]
except FileNotFoundError:
    pass
except Exception:
    pass
else:
    print("Read from .env")
    
if username is None or password is None:
    # Instantiate the parser
    parser = argparse.ArgumentParser(description='Optional app description')

    # Required positional argument
    parser.add_argument('sharif_usr', type=str,
                        help='A required integer positional argument')
                        
    # Required positional argument
    parser.add_argument('sharif_pass', type=str,
                        help='A required integer positional argument')

    args = parser.parse_args()

    if not args:
        exit("You should pass both Username and Password from .bat on .env file")
        
    username , password = args.sharif_usr, args.sharif_pass
    
    print("read from hard coded")
 

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

response = requests.post('https://net2.sharif.edu/login', headers=headers, data=data)

if not response:
    print("UNKNOWN ERROR: No Response!")
elif "You are logged in" in response.text:
    print("The IP Assigned Successfully!")
else:
    print(f"Login Failed! Please check your username and password")
