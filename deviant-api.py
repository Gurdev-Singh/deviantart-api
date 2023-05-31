import requests

def getProfileData(username):

  url = 'https://www.deviantart.com/oauth2/token'

  body = {
    'grant_type': 'client_credentials',
    'client_id': '25834',
    'client_secret': 'ec631e4a4045eee0785ab247e3c31ea3',
  }

  response = requests.post(url, data=body)

  if response.status_code != 200:
    raise requests.exceptions.HTTPError(response)

  response_json = response.json()

  access_token = response_json['access_token']
  print(access_token)

  response = requests.get('https://www.deviantart.com/api/v1/oauth2/user/profile/{}?access_token={}'.format(username,access_token))

  if response.status_code != 200:
    raise requests.exceptions.HTTPError(response)

  response_json = response.json()

  return response_json

userData = getProfileData('gurdevs')
print(userData)