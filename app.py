from flask import Flask , request , render_template
from pathlib import Path
from  transcribe import transcribe_audio
import os

app = Flask(__name__)


@app.route("/" , methods=["GET" , "POST"])
def whisper_app():
    if request.method == "GET" :
        return  render_template("home.html")
    
    if request.method == "POST" :
        # Getting audio file from user and saving it 
        file = request.files["audiofile"]
        file.save(os.path.join(Path("temp_data/"), file.filename))
        file_location = os.path.join(Path("temp_data/"), file.filename)
        """
        # Loading model and transcbing audio
        model = whisper.load_audio("small")
        audio = whisper.load_audio(os.path.join(Path("temp_data/"), file.filename))
        result = whisper.transcribe(model,audio)
        """
        # Returning webpage with transcript
        return render_template("home.html",transcript=transcribe_audio(file_location=file_location))


if __name__ == "__main__" :
    app.run(debug=True)
