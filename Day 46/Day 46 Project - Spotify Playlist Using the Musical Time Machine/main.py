from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100"
CLIENT_ID = YOUR CLIENT ID
CLIENT_SECRET = YOUR CLIENT SECRET
USERNAME = YOUR USERNAME
REDIRECT_URI = "http://example.com"

scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, redirect_uri=REDIRECT_URI, client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET, show_dialog=True, cache_path="token.txt"))
user_id = sp.current_user()["id"]

year = input("Which year do you want to time travel to? Type the date in this format - YYYY-MM-DD: ")

response = requests.get(url=f"{URL}/{year}")
billboard = response.text.encode('utf8').decode('ascii', 'ignore')
soup = BeautifulSoup(billboard, "html.parser")
all_songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")

songs = []
song_uris = []
for song in all_songs:
    songs.append(song.getText())
for i in range(len(songs)):
    music = sp.search(q=f"track:{songs[i]} year:{year.split('-')[0]}", type="track")
    print(music)
    try:
        uri = music["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{songs[i]} doesn't exist in Spotify. Skipped.")
playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
