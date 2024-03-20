import argparse
import time
import json
import os
import sys
from logging import DEBUG, ERROR
from pathlib import Path, PurePath
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def spotify_translator():
    parser = argparse.ArgumentParser(
        prog="spotify_translator", description="Translate Spotify songs."
    )
    parser.add_argument(
        "-l",
        "--url",
        action="store",
        help="Spotify Playlist link URL",
        type=str,
        nargs="+",
        required=False,  # this has to be set to false to prevent useless prompt for url when all user wants is the script version
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        action="store",
        help="Specify download directory for transcriptions, translations, and mp3.",
        required=False,
    )
    parser.add_argument(
        "-d",
        "--download",
        action="store_true",
        help="Download mp3 using youtube-dl",
        required=False,
        default=False,
    )

    # url = input("Enter track/playlist/album URL: ")
    # songs = []

    # try:
    #     if url.find("track") != -1:
    #         songs = spotify_track(url)
    #     if url.find("playlist") != -1:
    #         songs = spotify_playlist(url)
    #     if url.find("album") != -1:
    #         songs = spotify_album(url)
    # except ValueError:
    #     raise ValueError("Invalid URL")

    # for song in songs:
    #     download_one(song)
    #     print(f"\nTranslating track: {song['name']}\n")
    #     results = translate(song["name"], "Korean")
    #     print(f"Transcription:\n{results[0]}\n")
    #     print(f"Translation:\n{results[1]}\n")


if __name__ == "__main__":
    spotify_translator()
