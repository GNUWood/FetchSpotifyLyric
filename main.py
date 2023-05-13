import requests
import json
import time


def GetLyrics(trackID, accesstoken):
    lyricslist = []
    lyricapi = "https://spclient.wg.spotify.com/color-lyrics/v2/track/" + trackID + "?format=json"
    header = {
        "authorization": "Bearer " + accesstoken,
        "App-platform": "WebPlayer",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"
    }
    lyricdata = requests.get(lyricapi,headers=header)
    lyricjson = lyricdata.json()["lyrics"]
    for v in lyricjson["lines"]:
    	print(v[words])

trackID = input("TrackID: ")
accesstoken = input("AccessToken: ")
GetLyrics(trackID=trackID,accesstoken=accesstoken)
