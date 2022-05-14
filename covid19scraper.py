import requests, datetime
from bs4 import BeautifulSoup
def scrapeGlobalCase ():
    try:
        url = "https://www.worldometers.info/coronavirus/usa/pennsylvania/"
        req = requests.get(url)
        bsObj = BeautifulSoup(req.text, "html.parser")
        dato = bsObj.find_all(attrs={'style':True})
        LastUpdate = dato[3].text.strip()
        data = bsObj.find_all("div",class_ = "maincounter-number")
        NumConfirmed = int(data[0].text.strip().replace(',', ''))
        NumDeaths = int(data[1].text.strip().replace(',', ''))
        NumRecovered = int(data[2].text.strip().replace(',', ''))
        NumActive = NumConfirmed - NumDeaths - NumRecovered
        # TimeNow = datetime.datetime.now() 
        return {
            #'date': str(TimeNow),
            'date': LastUpdate,
            'ConfirmedCases': NumConfirmed,
            'ActiveCases': NumActive,
            'RecoveredCases': NumRecovered,
            'Deaths': NumDeaths
        }
    except Exception as e: print(e)

# testresults = scrapeGlobalCase()
# print(testresults)