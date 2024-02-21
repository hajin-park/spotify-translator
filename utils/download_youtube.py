'''
Download songs from youtube
'''

import os
import urllib
import urllib.request
from pathlib import Path
from mutagen.easyid3 import EasyID3
from mutagen.id3 import APIC, ID3
from mutagen.mp3 import MP3
from spotify_dl import youtube as yt


def download_one(song):
    songs = {
        "urls": [
            {
                "save_path": Path("audio/"),
                "songs": [
                    song
                ],
            }
        ]
    }
    yt.download_songs(
        songs=songs,
        output_dir=f"{os.path.dirname(os.path.realpath(__file__))}/audio/",
        format_string="best",
        skip_mp3=False,
        keep_playlist_order=False,
        no_overwrites=False,
        remove_trailing_tracks=False,
        use_sponsorblock="yes",
        file_name_f=yt.default_filename,
        multi_core=0,
    )