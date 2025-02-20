import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Scraping Billboard Hot 100
def get_billboard_songs(date):
    url = f"https://www.billboard.com/charts/hot-100/{date}/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    songs = [song.get_text().strip() for song in soup.select("li h3.c-title")]
    return songs[:100]

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    redirect_uri="http://example.com",
    scope="playlist-modify-private"
))

# Get Spotify user ID
user_id = sp.current_user()["id"]

def get_spotify_uris(songs, year):
    uris = []
    for song in songs:
        query = f"track:{song} year:{year}"
        result = sp.search(q=query, type="track", limit=1)
        try:
            uri = result["tracks"]["items"][0]["uri"]
            uris.append(uri)
        except IndexError:
            print(f"{song} not found on Spotify.")
    return uris

# Create Spotify Playlist and Add Songs
def create_playlist_and_add_songs(date, uris):
    playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
    sp.playlist_add_items(playlist_id=playlist["id"], items=uris)
    print(f"Playlist '{date} Billboard 100' created!")

if __name__ == "__main__":
    date = input("Enter a date (YYYY-MM-DD) to travel back to: ")
    year = date.split("-")[0]
    billboard_songs = get_billboard_songs(date)
    spotify_uris = get_spotify_uris(billboard_songs, year)
    create_playlist_and_add_songs(date, spotify_uris)




