<h1>Qui n'a pas révé d'un Jarvis sans l'API d'OpenAi ?</h1>

Effectiverment, ce code permet d'utiliser ChatGPT sans l'API, c'est pas mal du bricolage mais je pense que ça vaut le coup d'oeil.

- On enregistres sa voix en mp3.
- On envoies le mp3 à Google.
- Google renvoie un texte.
- On écris le texte (virtuellement) reçu dans la fenêtre avec un intervalle de 0.01s entre chaque caractère.
- On cliques (virtuellement) sur entrée.
- On attends 5 secondes le temps que ça génère. (ça clear la fenêtre en sautant des lignes)
- On prends une capture d'écran.
- On redimensionnes la capture d'écran afin qu'il n'y ait pas la barre des tâches ou la barre d'onglet de Chrome.
- On utilises pyteseract (IA dans le domaine de la reconnaissance du texte dans des images) pour extraire le texte dans la capture d'écran.
-On prends ce texte et on le remet sur Google encore pour générer la vois avec le TextToSpeech.
- On reçois un mp3.
- On joues le mp3 en guise de réponse.

Effectivement, il y a quelques défauts, comme par exemple, la mise en place du code qui est assez fastidieuse ou encore le temps de réponse (15 secondes)
- Bref, si vous voulez en savoir plus je vous invite à checkez le code.
