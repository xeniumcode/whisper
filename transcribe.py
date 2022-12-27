import whisper


def transcribe_audio(file_location):
    model  = whisper.load_model("small")
    audio  = whisper.load_audio(file_location)
    result = whisper.transcribe(model,audio)
    return result["text"]