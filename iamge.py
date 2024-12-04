import requests
from pprint import pprint

r = requests.get("https://www.nps.gov/common/uploads/structured_data/17EC840E-9926-2E09-F2DD47A282915BBB.jpg")
# print(r.content)
# with open('park.png', 'wb') as f:
#     f.write(r.content)

print(r.headers)

#
# import random
# import docx
# import requests
# from pprint import pprint
#
# national_park_doc = docx.Document()
# national_park_doc.add_paragraph('National Park Guide', 'Heading 1')
#
# national_park_url = 'https://national-parks-1150.azurewebsites.net/api/list'
# park_response = requests.get(national_park_url).json()
#
#
#
# five_random_national = random.sample(park_response, 5)
# # pprint(five_random_national)
#
# for park in five_random_national:
#
#     base_park_url = 'https://national-parks-1150.azurewebsites.net/api/'
#     park_code = park['park_code']
#     park_name = park['name']
#
#     parks_urls = base_park_url + park_code
#
#
#     parkapi_response = requests.get(parks_urls)
#     if parkapi_response.status_code == 200:
#         park_data = parkapi_response.json()
#         pprint(park_data)