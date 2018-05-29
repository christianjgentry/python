'''
from requests_oauthlib import OAuth1Session

forge = OAuth1Session('kJkNvYc5noUd7TaGnA5r5gZzoHPa2Gi4',
                        client_secret='1PKnSIXIFDIShVju')
                        
url = 'https://testtest_1.com'

r = forge.get(url)
'''
import requests

def forge_authenticate_app( client_id, client_secret, verbose=False ):
  """Retrieve and return an authentication token
  for this app's API key and secret."""

  data = {
    'client_id' : client_id,
    'client_secret' : client_secret,
    'grant_type' : 'client_credentials',
    'scope' : 'data:read'
  }
  
  r = requests.post(url_authenticate, data=data)

  if verbose:
    print('\nForge authenticate call:')
    print('  Status:', r.status_code)
    print('  Headers:', r.headers['content-type'])
    print('  Content:', r.content)

  if 200 == r.status_code:
    token = r.json()['access_token']
  else:
    token = None

  return token


url_authenticate = 'https://testtest_1.com'

r = forge_authenticate_app('kJkNvYc5noUd7TaGnA5r5gZzoHPa2Gi4', '1PKnSIXIFDIShVju')


print(r)
