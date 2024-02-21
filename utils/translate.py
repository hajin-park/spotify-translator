'''
Handle translation and transcription of audio files
'''

import whisper

def translate(file, from_lang):
    model = whisper.load_model("large")

    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(file)
    audio = whisper.pad_or_trim(audio)

    # Process audio
    transcription = model.transcribe(audio, language=from_lang, task="transcribe")["text"]
    translation = model.transcribe(audio, language=from_lang, task="translate")["text"]

    return transcription, translation