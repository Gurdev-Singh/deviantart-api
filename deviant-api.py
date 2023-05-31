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
  #print(access_token)

  response = requests.get('https://www.deviantart.com/api/v1/oauth2/user/profile/{}?access_token={}'.format(username,access_token))

  if response.status_code != 200:
    raise requests.exceptions.HTTPError(response)

  response_json = response.json()

  return response_json

userData = getProfileData('gurdevs')
print(userData)

def test_getProfileData(testUsername):
  expected_result = {
    'userid': 'B7871042-59B8-982D-F117-9E0EF24FEC49',
    'username': '{}'.format(testUsername),
    'usericon': 'https://a.deviantart.net/avatars/default.gif',
    'type': 'regular'
  }

  actual_result = getProfileData('gurdevs')
  
  assert actual_result['user']['username'] == expected_result['username']

#this test will fail as I changed the username in test method call.
test_getProfileData('gurdevs-diff')

#this test will pass as I passed the correct username in test method call.
test_getProfileData('gurdevs')
