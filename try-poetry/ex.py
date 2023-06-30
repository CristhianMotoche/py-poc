import requests

resp = requests.post(
    'http://checkurl.phishtank.com/checkurl/',
    data={'url': 'https://idtex.market/',
          'format': 'json'})

print(resp.json())
