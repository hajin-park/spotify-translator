from utils.fetch_spotify import spotify_track
from utils.fetch_spotify import spotify_playlist
from utils.fetch_spotify import spotify_album
from utils.download_youtube import download_one
from utils.translate import translate


def main():
    url = input("Enter track/playlist/album URL: ")
    songs = []

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
        download_one(song)
        print(f"\nTranslating track: {song['name']}\n")
        results = translate(f"audio/{song['name']}.mp3", "Korean")
        print(f"Transcription:\n{results[0]}\n")
        print(f"Translation:\n{results[1]}\n")

if __name__ == "__main__":
    main()
