import speech_recognition as sr
from pydub import AudioSegment

# Convertir le fichier MP3 en WAV
def convert_mp3_to_wav(mp3_file):
    sound = AudioSegment.from_mp3(mp3_file)
    wav_file = mp3_file.replace(".mp3", ".wav")
    sound.export(wav_file, format="wav")
    return wav_file

# Transcrire le fichier audio WAV en texte
def transcribe_audio(wav_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_file) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language="fr-FR")
            return text
        except sr.UnknownValueError:
            return "Google Web Speech API n'a pas pu comprendre l'audio."
        except sr.RequestError as e:
            return f"Impossible de faire une demande à Google Web Speech API; {e}"

# Chemin du fichier MP3
mp3_file = "ton_fichier.mp3"

# Processus de conversion et de transcription
wav_file = convert_mp3_to_wav(mp3_file)
text = transcribe_audio(wav_file)

print(text)
