from utils.fetch_spotify import spotify_track
from utils.fetch_spotify import spotify_playlist
from utils.fetch_spotify import spotify_album
from utils.download_youtube import download_one
from utils.translate import translate


def main():
    url      = input("Enter track/playlist/album URL: ")
    songs    = []

    try:
        if url.find("track") != -1:
            songs = spotify_track(url)
        if url.find("playlist") != -1:
            songs = spotify_playlist(url)
        if url.find("album") != -1:
            songs = spotify_album(url)
    except ValueError:
        raise ValueError("Invalid URL")

    for song in songs:
        print(f"Downloading track: {song.name}\n")
        download_one(song)
        print(f"Translating track: {song.name}\n")
        translation = translate(f"audio/{song.name}.mp3", "kr", "en")
        print(f"Result:\n{translation}\n\n")

if __name__ == "__main__":
    main()
