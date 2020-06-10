import json
import requests
import random

def getaccesstoken():
    client_id = #Your Client Id
    client_secret = #Your Client Secret

    url = 'https://accounts.spotify.com/api/token'

    grant_type = 'client_credentials'
    body_params = {'grant_type': grant_type}
    response = requests.post(url, data=body_params, auth=(client_id, client_secret))
    json_obj = json.loads(response.text)

    return json_obj['access_token']

def getartistid(artistName,accestoken):
    url = 'https://api.spotify.com/v1/search?q={artistName}&type=artist'.format(artistName=artistName)
    response = requests.get(url,headers={"Authorization": "Bearer {accesstoken}".format(accesstoken=accestoken)})
    json_obj = json.loads(response.text)
    return json_obj['artists']['items'][0]['id']

def getartisttoptrack(artistId,accestoken):
    url = 'https://api.spotify.com/v1/artists/{artistId}/top-tracks?country=TR'.format(artistId = artistId)
    response = requests.get(url,headers={"Authorization": "Bearer {accesstoken}".format(accesstoken = accestoken)})
    json_obj = json.loads(response.text)
    return json_obj['tracks']

def getgenres():
    data = getgenresdata()
    genrelist = [genre for genre in data]
    return genrelist

def getrandomartist(genre):
    data = getgenresdata()
    randomnumber = random.randint(0, len(data[genre])-1)
    return data[genre][randomnumber]

def getgenresdata():
    with open('genres.json') as json_file:
        data = json.load(json_file)
    return data

