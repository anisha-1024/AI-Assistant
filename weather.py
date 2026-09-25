# https://www.google.com/search?q=weather+pune
#user agent - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36
# span id - wob_tm

from requests_html import HTMLSession
import speech_to_text

def weather():
    s = HTMLSession()
    query = "pune"
    url = f'https://wttr.in/{query}?format=j1'

    r = s.get(url, headers={'User-Agent':'Mozilla/5.0'})

    data = r.json()
    temp = data['current_condition'][0]['temp_C']
    unit = "°C"
    desc = data['current_condition'][0]['weatherDesc'][0]['value']

    return temp+" "+unit+" "+desc

# test
if __name__ == "__main__":
    print(weather())