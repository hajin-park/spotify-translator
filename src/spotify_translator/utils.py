from spotify_dl.spotify import (
    fetch_tracks,
    parse_spotify_url,
    get_item_name,
    validate_spotify_urls,
)
from spotify_dl.scaffold import get_tokens
from spotify_dl import youtube as yt
from spotipy.oauth2 import SpotifyClientCredentials
from pathlib import Path
import os
import sys
import whisper
import spotipy


def translate(file, from_lang):
    model = whisper.load_model("large")

    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(f"audio\\{file}.mp3")
    # audio = whisper.pad_or_trim(audio)

    # Process audio
    transcription = model.transcribe(
        audio, language=from_lang, task="transcribe", fp16=False
    )["text"]
    translation = model.transcribe(
        audio, language=from_lang, task="translate", fp16=False
    )["text"]

    with open(f"output\\{file}.txt", "w") as f:
        f.write(f"Transcription:\n{transcription}\n\nTranslation:\n{translation}")

    return transcription, translation


def spotify_auth():
    # test client ids, b64 for just to deter.
    tokens = get_tokens()
    if tokens is None:
        sys.exit(1)
    client_id, client_secret = tokens

    sp = spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(
            client_id=client_id, client_secret=client_secret
        )
    )
    return sp
