'''
Fetch specified tracks from Spotify
'''

import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotify_dl.spotify import fetch_tracks
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")


def spotify_auth():
    # test client ids, b64 for just to deter.
    client = spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET
        )
    )
    return client


def spotify_track(url):
    sp = spotify_auth()
    item_type = "track"
    songs = fetch_tracks(sp, item_type, url)
    return songs
    # assert {
    #     "album": "Hell Freezes Over (Remaster 2018)",
    #     "artist": "Eagles",
    #     "cover": "https://i.scdn.co/image/ab67616d0000b27396d28597a5ae44ab66552183",
    #     "genre": "album rock",
    #     "name": "Hotel California - Live On MTV, 1994",
    #     "num": 6,
    #     "num_tracks": 15,
    #     "year": "1994",
    #     "track_url": None,
    #     "playlist_num": 1,
    #     "spotify_id": "2GpBrAoCwt48fxjgjlzMd4",
    #     'tempo': 74.656,
    # } == songs[0]


def spotify_playlist(url):
    sp = spotify_auth()
    item_type = "playlist"
    songs = fetch_tracks(sp, item_type, url)
    return songs
    # assert [
    #     {
    #         "album": "Progressive Psy Trance Picks Vol.8",
    #         "artist": "Odiseo",
    #         "cover": "https://i.scdn.co/image/ab67616d0000b273ce6d0eef0c1ce77e5f95bbbc",
    #         "genre": "progressive psytrance",
    #         "name": "Api",
    #         "num": 10,
    #         "track_url": None,
    #         "num_tracks": 20,
    #         "year": "2012",
    #         "playlist_num": 1,
    #         "spotify_id": "4rzfv0JLZfVhOhbSQ8o5jZ",
    #         'tempo': 135.016,
    #     },
    #     {
    #         "album": "Wellness & Dreaming Source",
    #         "artist": "Vlasta Marek",
    #         "cover": "https://i.scdn.co/image/ab67616d0000b273aa2ff29970d9a63a49dfaeb2",
    #         "genre": "singing bowl",
    #         "name": "Is",
    #         "num": 21,
    #         "num_tracks": 25,
    #         "year": "2015",
    #         "playlist_num": 2,
    #         "track_url": None,
    #         "spotify_id": "5o3jMYOSbaVz3tkgwhELSV",
    #         'tempo': 137.805,
    #     },
    #     {
    #         "album": "This Is Happening",
    #         "artist": "LCD Soundsystem",
    #         "cover": "https://i.scdn.co/image/ab67616d0000b273ee0d0dce888c6c8a70db6e8b",
    #         "genre": "alternative dance",
    #         "name": "All I Want",
    #         "num": 4,
    #         "num_tracks": 9,
    #         "track_url": None,
    #         "year": "2010",
    #         "playlist_num": 3,
    #         "spotify_id": "4Cy0NHJ8Gh0xMdwyM9RkQm",
    #         'tempo': 134.99,
    #     },
    #     {
    #         "album": "Glenn Horiuchi Trio / Gelenn Horiuchi Quartet: Mercy / Jump Start "
    #         "/ Endpoints / Curl Out / Earthworks / Mind Probe / Null Set / "
    #         "Another Space (A)",
    #         "artist": "Glenn Horiuchi Trio",
    #         "cover": "https://i.scdn.co/image/ab67616d0000b2738b7447ac3daa1da18811cf7b",
    #         "genre": "",
    #         "name": "Endpoints",
    #         "num": 2,
    #         "num_tracks": 8,
    #         "year": "2011",
    #         "track_url": None,
    #         "playlist_num": 4,
    #         "spotify_id": "6hvFrZNocdt2FcKGCSY5NI",
    #         'tempo': 114.767,
    #     },
    #     {
    #         "album": "All The Best (Spanish Version)",
    #         "artist": "Zucchero",
    #         "cover": "https://i.scdn.co/image/ab67616d0000b27304e57d181ff062f8339d6c71",
    #         "name": "You Are So Beautiful",
    #         "num": 18,
    #         "track_url": None,
    #         "genre": "italian adult pop",
    #         "num_tracks": 18,
    #         "year": "2007",
    #         "playlist_num": 5,
    #         "spotify_id": "2E2znCPaS8anQe21GLxcvJ",
    #         'tempo': 122.318,
    #     },
    # ] == songs


def spotify_album(url):
    sp = spotify_auth()
    item_type = "album"
    songs = fetch_tracks(sp, item_type, url)
    return songs
    # assert [
    #     {
    #         "album": "Queen II (Deluxe Remastered Version)",
    #         "artist": "Queen",
    #         "cover": "https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5",
    #         "genre": "classic rock",
    #         "name": "Procession - Remastered 2011",
    #         "num": 1,
    #         "track_url": None,
    #         "num_tracks": 16,
    #         "year": "1974",
    #         "playlist_num": 1,
    #         "spotify_id": "69Yw7H4bRIwfIxL0ZCZy8y",
    #         'tempo': 120.955,
    #     },
    #     {
    #         "album": "Queen II (Deluxe Remastered Version)",
    #         "artist": "Queen",
    #         "cover": "https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5",
    #         "genre": "classic rock",
    #         "name": "Father To Son - Remastered 2011",
    #         "num": 2,
    #         "num_tracks": 16,
    #         "track_url": None,
    #         "year": "1974",
    #         "playlist_num": 2,
    #         "spotify_id": "5GGSjXZeTgX9sKYBtl8K6U",
    #         'tempo': 147.384,
    #     },
    #     {
    #         "album": "Queen II (Deluxe Remastered Version)",
    #         "artist": "Queen",
    #         "cover": "https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5",
    #         "genre": "classic rock",
    #         "name": "White Queen (As It Began) - Remastered 2011",
    #         "num": 3,
    #         "track_url": None,
    #         "num_tracks": 16,
    #         "year": "1974",
    #         "playlist_num": 3,
    #         "spotify_id": "0Ssh20fuVhmasLRJ97MLnp",
    #         'tempo': 152.769,
    #     },
    #     {
    #         "album": "Queen II (Deluxe Remastered Version)",
    #         "artist": "Queen",
    #         "cover": "https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5",
    #         "genre": "classic rock",
    #         "name": "Some Day One Day - Remastered 2011",
    #         "num": 4,
    #         "num_tracks": 16,
    #         "track_url": None,
    #         "year": "1974",
    #         "playlist_num": 4,
    #         "spotify_id": "2LasW39KJDE4VH9hTVNpE2",
    #         'tempo': 115.471,
    #     },
    #     {
    #         "album": "Queen II (Deluxe Remastered Version)",
    #         "artist": "Queen",
    #         "cover": "https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5",
    #         "genre": "classic rock",
    #         "name": "The Loser In The End - Remastered 2011",
    #         "num": 5,
    #         "track_url": None,
    #         "num_tracks": 16,
    #         "year": "1974",
    #         "playlist_num": 5,
    #         "spotify_id": "6jXrIu3hWbmJziw34IHIwM",
    #         'tempo': 145.124,
    #     },
    #     {
    #         "album": "Queen II (Deluxe Remastered Version)",
    #         "artist": "Queen",
    #         "cover": "https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5",
    #         "genre": "classic rock",
    #         "name": "Ogre Battle - Remastered 2011",
    #         "num": 6,
    #         "num_tracks": 16,
    #         "year": "1974",
    #         "track_url": None,
    #         "playlist_num": 6,
    #         "spotify_id": "5dHmGuUeRgp5f93G69tox5",
    #         'tempo': 108.544,
    #     },
    #     {
    #         "album": "Queen II (Deluxe Remastered Version)",
    #         "artist": "Queen",
    #         "cover": "https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5",
    #         "genre": "classic rock",
    #         "name": "The Fairy Feller's Master-Stroke - Remastered 2011",
    #         "num": 7,
    #         "num_tracks": 16,
    #         "track_url": None,
    #         "year": "1974",
    #         "playlist_num": 7,
    #         "spotify_id": "2KPj0oB7cUuHQ3FuardOII",
    #         'tempo': 159.156,
    #     },
    #     {
    #         "album": "Queen II (Deluxe Remastered Version)",
    #         "artist": "Queen",
    #         "cover": "https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5",
    #         "genre": "classic rock",
    #         "name": "Nevermore - Remastered 2011",
    #         "num": 8,
    #         "track_url": None,
    #         "num_tracks": 16,
    #         "year": "1974",
    #         "playlist_num": 8,
    #         "spotify_id": "34CcBjL9WqEAtnl2i6Hbxa",
    #         'tempo': 118.48,
    #     },
    #     {
    #         "album": "Queen II (Deluxe Remastered Version)",
    #         "artist": "Queen",
    #         "cover": "https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5",
    #         "genre": "classic rock",
    #         "name": "The March Of The Black Queen - Remastered 2011",
    #         "num": 9,
    #         "track_url": None,
    #         "num_tracks": 16,
    #         "year": "1974",
    #         "playlist_num": 9,
    #         "spotify_id": "1x9ak6LGIazLhfuaSIEkhG",
    #         'tempo': 112.623,
    #     },
    #     {
    #         "album": "Queen II (Deluxe Remastered Version)",
    #         "artist": "Queen",
    #         "cover": "https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5",
    #         "genre": "classic rock",
    #         "name": "Funny How Love Is - Remastered 2011",
    #         "num": 10,
    #         "track_url": None,
    #         "num_tracks": 16,
    #         "year": "1974",
    #         "playlist_num": 10,
    #         "spotify_id": "4CITL18Tos0PscW1amCK4j",
    #         'tempo': 145.497,
    #     },
    #     {
    #         "album": "Queen II (Deluxe Remastered Version)",
    #         "artist": "Queen",
    #         "cover": "https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5",
    #         "genre": "classic rock",
    #         "name": "Seven Seas Of Rhye - Remastered 2011",
    #         "num": 11,
    #         "track_url": None,
    #         "num_tracks": 16,
    #         "year": "1974",
    #         "playlist_num": 11,
    #         "spotify_id": "1e9Tt3nKBwRbuaU79kN3dn",
    #         'tempo': 126.343,
    #     },
    #     {
    #         "album": "Queen II (Deluxe Remastered Version)",
    #         "artist": "Queen",
    #         "cover": "https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5",
    #         "genre": "classic rock",
    #         "name": "See What A Fool I've Been - Live BBC Session, London / July 1973 / " "2011 Remix",
    #         "num": 1,
    #         "track_url": None,
    #         "num_tracks": 16,
    #         "year": "1974",
    #         "playlist_num": 12,
    #         "spotify_id": "0uHqoDT7J2TYBsJx6m4Tvi",
    #         'tempo': 172.274,
    #     },
    #     {
    #         "album": "Queen II (Deluxe Remastered Version)",
    #         "artist": "Queen",
    #         "cover": "https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5",
    #         "genre": "classic rock",
    #         "name": "White Queen (As It Began) - Live At Hammersmith Odeon, London / " "December 1975",
    #         "num": 2,
    #         "track_url": None,
    #         "num_tracks": 16,
    #         "year": "1974",
    #         "playlist_num": 13,
    #         "spotify_id": "3MIueGYoNiyBNfi5ukDgAK",
    #         'tempo': 146.712,

    #     },
    #     {
    #         "album": "Queen II (Deluxe Remastered Version)",
    #         "artist": "Queen",
    #         "cover": "https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5",
    #         "genre": "classic rock",
    #         "name": "Seven Seas Of Rhye - Instrumental Mix 2011",
    #         "num": 3,
    #         "track_url": None,
    #         "num_tracks": 16,
    #         "year": "1974",
    #         "playlist_num": 14,
    #         "spotify_id": "34WAOFWdJ83a3YYrDAZTjm",
    #         'tempo': 128.873,
    #     },
    #     {
    #         "album": "Queen II (Deluxe Remastered Version)",
    #         "artist": "Queen",
    #         "cover": "https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5",
    #         "genre": "classic rock",
    #         "name": "Nevermore - Live BBC Session, London / April 1974",
    #         "num": 4,
    #         "track_url": None,
    #         "num_tracks": 16,
    #         "year": "1974",
    #         "playlist_num": 15,
    #         "spotify_id": "2AFIPUlApcUwGEgOSDwoBz",
    #         'tempo': 122.986,
    #     },
    #     {
    #         "album": "Queen II (Deluxe Remastered Version)",
    #         "artist": "Queen",
    #         "cover": "https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5",
    #         "genre": "classic rock",
    #         "name": "See What A Fool I’ve Been - B-Side Version / Remastered 2011",
    #         "num": 5,
    #         "track_url": None,
    #         "num_tracks": 16,
    #         "year": "1974",
    #         "playlist_num": 16,
    #         "spotify_id": "4G4Sf18XkFvNTV5vAxiQyd",
    #         'tempo': 169.166,
    #     },
    # ] == songs
    # assert (len(songs)) == 16