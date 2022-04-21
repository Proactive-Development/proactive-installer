cd /home
echo -e "ssl._create_default_https_context = ssl._create_unverified_context\n$(cat installer.py)" > installer.py
echo -e "import ssl\n$(cat installer.py)" > installer.py
python3 installer.py
ls
