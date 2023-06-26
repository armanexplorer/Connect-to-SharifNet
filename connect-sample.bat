@ECHO OFF

SET "USERNAME=mazloumzadeh"
SET "PASSWORD=8C2eXEKfj35TmRW"

SET "LOGIN_URL=https://net2.sharif.ir/login"
SET "LOGOUT_URL=https://net2.sharif.ir/logout"
SET "LOGIN_DATA=username=%USERNAME%&password=%PASSWORD%"

echo Logout...
echo:

curl -s %LOGOUT_URL% >NUL

if %errorlevel% equ 0 (
    echo Logout succeeded!
) else (
    echo Logout request failed with error code %errorlevel%.
)

echo Login...
echo:
curl -s -XPOST -d "%LOGIN_DATA%" %LOGIN_URL% >NUL

if %errorlevel% equ 0 (
    echo Login succeeded!
) else (
    echo Login request failed with error code %errorlevel%.
)

echo Running the script finished.
echo:

pause
@REM exit 0