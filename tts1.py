import pyttsx3
import speech_recognition as sr
from PIL import ImageGrab,Image
import pygetwindow as gw
import pyautogui
import time  # Pour ajouter un délai

from pytesseract import pytesseract


def capture_chrome_window(title_contains):
    # Trouver toutes les fenêtres qui contiennent le titre donné
    windows = gw.getWindowsWithTitle(title_contains)
    if windows:
        # Prendre la première fenêtre qui correspond au titre
        window = windows[0]
        # Activer et mettre en avant la fenêtre (ne fonctionne pas en arrière-plan)
        window.activate()
        # Attendre un moment pour que la fenêtre soit active
        pyautogui.sleep(2)
        # Capturer la zone d'écran de la fenêtre
        bbox = (window.left, window.top, window.left + window.width, window.top + window.height)
        screenshot = ImageGrab.grab(bbox)
        # Enregistrer l'image capturée
        screenshot.save("chrome_window_capture.png")
        print("Capture d'écran enregistrée.")
    else:
        print("Aucune fenêtre Chrome trouvée avec ce titre.")

def supprimer_contour(image_path, bordure):
    # Charger l'image
    image = Image.open(image_path)

    # Calculer les dimensions de la nouvelle image
    gauche = bordure
    haut = bordure
    droite = image.width - bordure
    bas = image.height - bordure

    # Créer la nouvelle image sans les bords
    image_sans_contour = image.crop((gauche, haut, droite, bas))

    # Sauvegarder ou afficher la nouvelle image
    image_sans_contour.save('chrome_window_capture.png')
    image_sans_contour.show()



def bring_window_to_front_and_type(window_title, text):
    try:
        # Trouve la fenêtre par son titre
        window = gw.getWindowsWithTitle(window_title)[0]  # Prend la première fenêtre qui correspond
        if window:
            # Active la fenêtre pour la mettre au premier plan
            window.activate()
            # Attend un court instant pour s'assurer que la fenêtre est active
            time.sleep(1)
            # Simule la frappe de texte
            pyautogui.write(text, interval=0.01)
            pyautogui.press('enter')
        else:
            print(f"La fenêtre '{window_title}' n'a pas été trouvée.")
    except IndexError:
        # Gestion au cas où la fenêtre spécifiée n'existe pas
        print(f"La fenêtre '{window_title}' n'a pas été trouvée.")



# Configuration de la synthèse vocale avec Pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Fonction pour lire un texte à voix haute avec Pyttsx3
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Fonction pour détecter une commande vocale
def detect_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio, language='fr-FR')
        print(command)
        return command
    except sr.UnknownValueError:
        command="Désolé, je n'ai pas compris ce que vous avez dit."
        print("Désolé, je n'ai pas compris ce que vous avez dit.")
        return command
    except sr.RequestError as e:
        command="Impossible de demander les résultats de la reconnaissance vocale ; {0}".format(e)
        print("Impossible de demander les résultats de la reconnaissance vocale ; {0}".format(e))
        return command

# Boucle pour continuer à écouter les commandes
while True:
    print("parle")
    commande = detect_voice()

    # Ecrire dans la fenêtre
    bring_window_to_front_and_type('Google Chrome', commande)
    time.sleep(5)
    # Utiliser une partie du titre de la fenêtre Chrome que vous souhaitez capturer
    capture_chrome_window("Google Chrome")
    # Remplacer 'chemin_vers_votre_image' par le chemin de votre fichier image
    supprimer_contour('chrome_window_capture.png', 200)

    # Defining paths to tesseract.exe
    # and the image we would be using
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path = r"chrome_window_capture.png"

    # Opening the image & storing it in an image object
    img = Image.open(image_path)

    # Providing the tesseract executable
    # location to pytesseract library
    pytesseract.tesseract_cmd = path_to_tesseract

    # Passing the image object to image_to_string() function
    # This function will extract the text from the image
    text = pytesseract.image_to_string(img)

    # Displaying the extracted text
    print(text[:-1])
    speak(text[:-1])