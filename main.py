from PIL import ImageGrab,Image
import pygetwindow as gw
import pyautogui
import time  # Pour ajouter un délai

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
            pyautogui.write(text, interval=0.005)
            pyautogui.press('enter')
        else:
            print(f"La fenêtre '{window_title}' n'a pas été trouvée.")
    except IndexError:
        # Gestion au cas où la fenêtre spécifiée n'existe pas
        print(f"La fenêtre '{window_title}' n'a pas été trouvée.")


# Utiliser une partie du titre de la fenêtre Chrome que vous souhaitez capturer
capture_chrome_window("Google Chrome")

#Ecrire dans la fenêtre
bring_window_to_front_and_type('Google Chrome', "hello")

# Remplacer 'chemin_vers_votre_image' par le chemin de votre fichier image
supprimer_contour('chrome_window_capture.png', 200)






