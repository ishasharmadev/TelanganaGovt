import requests
from bs4 import BeautifulSoup


# func to get all survey nos. here 
def get_survey_numbers(district, mandal, village):
    url = "https://dharani.telangana.gov.in/knowLandStatus"

    # data to send in post req
    data = {
        "District": district,
        "Mandal": mandal,
        "Village": village
    }

    # Send post request
    response = requests.post(url, data=data)

    # if successful then store content 
    if response.status_code == 200:
        # Parse the HTML response
        soup = BeautifulSoup(response.content, "html.parser")
        
        # list of survey nos 
        survey_numbers = []
        for option in soup.find_all("option"):
            survey_number = option.get("value")
            if survey_number:
                survey_numbers.append(survey_number)

        return survey_numbers
    else:
        print("No survey code found. Try again")
        return []

# trial
district = "Adilabad"
mandal = "Bela"
village = "Bela"

survey_numbers = get_survey_numbers(district, mandal, village)
if survey_numbers:
    print(f"Survey numbers for {district}, {mandal}, {village}:")
    for num in survey_numbers:
        print(num)
else:
    print("No survey numbers found")
