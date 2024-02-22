"""
Handle translation and transcription of audio files
"""

import whisper


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
