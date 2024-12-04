import docx

# document = docx.Document()
#
# document.add_paragraph('hello world', 'Title')
#
#
# document.add_paragraph('By Jorge Lazaro', 'Heading 1')
#
# document.add_paragraph('this is a word doc for my python class')
#
# document.save('helloworld.docx')


import random
import docx
import requests

# Initialize Word document
national_park_doc = docx.Document()
national_park_doc.add_paragraph('National Park Guide', 'Title')

# Fetch list of parks
national_park_url = 'https://national-parks-1150.azurewebsites.net/api/list'
park_response = requests.get(national_park_url).json()

# Randomly select five parks
five_random_national = random.sample(park_response, 5)

# Fetch details for each selected park and add to Word document
for park in five_random_national:
    base_park_url = 'https://national-parks-1150.azurewebsites.net/api/'
    park_code = park['park_code']
    park_name = park['name']

    # Add park name as a heading
    national_park_doc.add_heading(park_name, level=2)

    # Fetch park details
    parks_urls = base_park_url + park_code
    parkapi_response = requests.get(parks_urls)

    if parkapi_response.status_code == 200:
        park_data = parkapi_response.json()

        # Add description if available
        description = park_data.get('description', 'No description available.')
        national_park_doc.add_paragraph(f"Description: {description}")

        # Add activities if available
        activities = park_data.get('activities', [])
        if activities:
            activities_list = ", ".join(activities)
            national_park_doc.add_paragraph(f"Activities: {activities_list}")
        else:
            national_park_doc.add_paragraph("Activities: None available.")

        # Add additional information as needed
        location = park_data.get('location', 'Location not provided.')
        national_park_doc.add_paragraph(f"Location: {location}")

# Save the Word document
national_park_doc.save('testingparksonetwo.docx')