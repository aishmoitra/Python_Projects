# Music Time Machine Project - Documentation

This project scrapes the Billboard Hot 100 chart for a given date and creates a private Spotify playlist with those songs.

## Features

- **Scrapes Billboard Hot 100**: Fetches the top 100 songs from Billboard for a specific date.
- **Spotify Authentication**: Uses Spotipy to authenticate with Spotify.
- **Searches for Songs on Spotify**: Finds the corresponding tracks on Spotify.
- **Creates a Spotify Playlist**: Generates a private playlist in the user's account.
- **Adds Songs to Playlist**: Populates the playlist with available songs from the Hot 100 chart.

## How It Works

1. **User Inputs Date**: The user provides a date in `YYYY-MM-DD` format.
2. **Fetch Billboard Hot 100**: The script scrapes Billboard’s website for the top 100 songs of that date.
3. **Search Songs on Spotify**: Each song is searched on Spotify using the Spotipy API.
4. **Create Playlist**: A new private playlist is created on the user’s Spotify account.
5. **Add Songs**: The found songs are added to the playlist.

## File Structure

- **main.py**: The main script that scrapes Billboard, interacts with Spotify, and creates a playlist.
- **requirements.txt**: Lists the Python dependencies required to run the script.

## Setup Instructions

### 1. **Set Up Spotify API**

- Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and log in.
- Click "Create an App" and fill in the required details.
- Copy your **Client ID** and **Client Secret**.
- Set the redirect URI to `http://example.com` (or your preferred URI).

### 2. **Install Dependencies**

Run the following command to install required Python packages:

```bash
  pip install requests beautifulsoup4 spotipy
```

### 3. **Set Up Authentication**

Update `main.py` with your Spotify credentials:

```python
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    redirect_uri="http://example.com",
    scope="playlist-modify-private"
))
```

Replace `YOUR_CLIENT_ID` and `YOUR_CLIENT_SECRET` with your actual credentials.

### 4. **Run the Script**

Execute the script by running:

```bash
  python main.py
```

Enter a date when prompted (e.g., `2023-08-15`). The script will then:
- Fetch the Billboard Hot 100 songs for that date.
- Search for them on Spotify.
- Create a new playlist and add the songs.

### 5. **View Your Playlist**

Once the script completes, the playlist will be available in your Spotify account under "Your Library."

## Troubleshooting

- **Some songs not found?**
  - Spotify may not have some songs or may list them under different names. Try modifying the search query.
- **Authentication errors?**
  - Ensure your credentials are correct and your redirect URI matches the one set in the Spotify Developer Dashboard.
- **Billboard website changed?**
  - If Billboard updates its website structure, the scraping logic may need adjustments.

## Customization

- Change the playlist name format in `create_playlist_and_add_songs()`.
- Modify the search query logic in `get_spotify_uris()` to improve song-matching accuracy.
- Extend functionality to scrape and create playlists for other Billboard charts.

## Dependencies

- Python 3.x
- requests (for web scraping)
- BeautifulSoup4 (for parsing HTML)
- Spotipy (for Spotify API access)

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.

