@ECHO OFF

set "sharif_username=XXXXXXXXXXXXXXX"
set "sharif_password=XXXXXXXXXXXXXXX"

echo Running the Python Script...
echo:

python ip_request.py %sharif_username% %sharif_password%

echo Running the script finished.
echo:

pause