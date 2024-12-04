import requests
import docx
import random
# from pprint import pprint
parklist_url = 'https://national-parks-1150.azurewebsites.net/api/list'

parklist_response = requests.get(parklist_url).json()