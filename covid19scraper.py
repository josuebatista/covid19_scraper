import requests, datetime
from bs4 import BeautifulSoup

usa_state_url = [
    ('AL','https://www.worldometers.info/coronavirus/usa/alabama/'),
    ('AK','https://www.worldometers.info/coronavirus/usa/alaska/'),
    ('AZ','https://www.worldometers.info/coronavirus/usa/arizona/'),
    ('AR','https://www.worldometers.info/coronavirus/usa/arkansas/'),
    ('CA','https://www.worldometers.info/coronavirus/usa/california/'),
    ('CO','https://www.worldometers.info/coronavirus/usa/colorado/'),
    ('CT','https://www.worldometers.info/coronavirus/usa/connecticut/'),
    ('DE','https://www.worldometers.info/coronavirus/usa/delaware/'),
    ('DC','https://www.worldometers.info/coronavirus/usa/district-of-columbia/'),
    ('FL','https://www.worldometers.info/coronavirus/usa/florida/'),
    ('GA','https://www.worldometers.info/coronavirus/usa/georgia/'),
    ('HI','https://www.worldometers.info/coronavirus/usa/hawaii/'),
    ('ID','https://www.worldometers.info/coronavirus/usa/idaho/'),
    ('IL','https://www.worldometers.info/coronavirus/usa/illinois/'),
    ('IN','https://www.worldometers.info/coronavirus/usa/indiana/'),
    ('IA','https://www.worldometers.info/coronavirus/usa/iowa/'),
    ('KS','https://www.worldometers.info/coronavirus/usa/kansas/'),
    ('KY','https://www.worldometers.info/coronavirus/usa/kentucky/'),
    ('LA','https://www.worldometers.info/coronavirus/usa/louisiana/'),
    ('ME','https://www.worldometers.info/coronavirus/usa/maine/'),
    ('MD','https://www.worldometers.info/coronavirus/usa/maryland/'),
    ('MA','https://www.worldometers.info/coronavirus/usa/massachusetts/'),
    ('MI','https://www.worldometers.info/coronavirus/usa/michigan/'),
    ('MN','https://www.worldometers.info/coronavirus/usa/minnesota/'),
    ('MS','https://www.worldometers.info/coronavirus/usa/mississippi/'),
    ('MO','https://www.worldometers.info/coronavirus/usa/missouri/'),
    ('MT','https://www.worldometers.info/coronavirus/usa/montana/'),
    ('NE','https://www.worldometers.info/coronavirus/usa/nebraska/'),
    ('NV','https://www.worldometers.info/coronavirus/usa/nevada/'),
    ('NH','https://www.worldometers.info/coronavirus/usa/new-hampshire/'),
    ('NJ','https://www.worldometers.info/coronavirus/usa/new-jersey/'),
    ('NM','https://www.worldometers.info/coronavirus/usa/new-mexico/'),
    ('NY','https://www.worldometers.info/coronavirus/usa/new-york/'),
    ('NC','https://www.worldometers.info/coronavirus/usa/north-carolina/'),
    ('ND','https://www.worldometers.info/coronavirus/usa/north-dakota/'),
    ('OH','https://www.worldometers.info/coronavirus/usa/ohio/'),
    ('OK','https://www.worldometers.info/coronavirus/usa/oklahoma/'),
    ('OR','https://www.worldometers.info/coronavirus/usa/oregon/'),
    ('PA','https://www.worldometers.info/coronavirus/usa/pennsylvania/'),
    ('RI','https://www.worldometers.info/coronavirus/usa/rhode-island/'),
    ('SC','https://www.worldometers.info/coronavirus/usa/south-carolina/'),
    ('SD','https://www.worldometers.info/coronavirus/usa/south-dakota/'),
    ('TN','https://www.worldometers.info/coronavirus/usa/tennessee/'),
    ('TX','https://www.worldometers.info/coronavirus/usa/texas/'),
    ('UT','https://www.worldometers.info/coronavirus/usa/utah/'),
    ('VT','https://www.worldometers.info/coronavirus/usa/vermont/'),
    ('VA','https://www.worldometers.info/coronavirus/usa/virginia/'),
    ('WA','https://www.worldometers.info/coronavirus/usa/washington/'),
    ('WV','https://www.worldometers.info/coronavirus/usa/west-virginia/'),
    ('WI','https://www.worldometers.info/coronavirus/usa/wisconsin/'),
    ('WY','https://www.worldometers.info/coronavirus/usa/wyoming/')
    ]


def scrapeGlobalCase(us_state):
    try:
        res = [y for (x, y) in usa_state_url if x == us_state]
        if not res:
            raise ValueError("Invalid state code provided.")
        url = res[0]
        req = requests.get(url, timeout=10)
        req.raise_for_status()
        bsObj = BeautifulSoup(req.text, "html.parser")
        dato = bsObj.find_all(attrs={'style': True})
        LastUpdate = dato[3].text.strip()
        data = bsObj.find_all("div", class_="maincounter-number")
        NumConfirmed = int(data[0].text.strip().replace(',', ''))
        NumDeaths = int(data[1].text.strip().replace(',', ''))
        NumRecovered = int(data[2].text.strip().replace(',', ''))
        NumActive = NumConfirmed - NumDeaths - NumRecovered
        return {
            'us_state': us_state,
            'date': LastUpdate,
            'confirmedCases': NumConfirmed,
            'activeCases': NumActive,
            'recoveredCases': NumRecovered,
            'deaths': NumDeaths
        }
    except requests.exceptions.RequestException as e:
        print(f"HTTP request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")