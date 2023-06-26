#!/bin/bash

USERNAME="********"
PASSWORD="********"

LOGIN_URL="https://net2.sharif.ir/login"
LOGOUT_URL="https://net2.sharif.ir/logout"
LOGIN_DATA="username=${USERNAME}&password=${PASSWORD}"

echo "Logout..."
echo

curl -s ${LOGOUT_URL} >/dev/null

if [ $? -eq 0 ]; then
echo "Logout succeeded!"
else
echo "Logout request failed with error code $?."
fi

echo "Login..."
echo

curl -s -XPOST -d "${LOGIN_DATA}" ${LOGIN_URL} >/dev/null

if [ $? -eq 0 ]; then
echo "Login succeeded!"
else
echo "Login request failed with error code $?."
fi

echo "Running the script finished."
echo

exit 0
# read -p "Press any key to continue..."