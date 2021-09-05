# CMPUT404 Lab1
# Fall 2021
# Vicky Zhao

import requests

requests_version = requests.__version__
print('Requests version is ' + requests_version)

Google_homepage = requests.get('https://www.google.com')
print('Google home page is ' + str(Google_homepage))

source_code = requests.get('https://github.com/ziwei11/CMPUT404_Lab1')
print(source_code.text)
