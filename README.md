
![Logo](https://github.com/MrGameSucht/CamcarpetCreate/blob/main/CamcarpetCreateLogo.png)


# CamcarpetCreate

Dieses Programm dient zur automatischen Erstellung von Camcarpets. Man gibt Höhe, Entfernung und ein Wort ein, und man erhält eine grafische Darstellung des gewünschten Camcarpets. Daraufhin kann man auch das Camcarpet zu einer PDF exportieren.





## Features

- 2D/3D Camcarpet Darstellung
- Camcarpet als A4 Bild exportieren
- Unterstützt alle deutschen Buchstaben


## Installation

Repository Clonen
```
git clone https://github.com/MrGameSucht/CamcarpetCreate.git
```

Python 3.10 oder neuer benutzten

Virtual-Enviroment erstellen (Empfohlen)
```
// Optional cmd direkt im CamcarpetCreate Ordner starten
cd path\to\your\project

// Erstellung
python -m venv .venv

// Aktivierung
.venv\Scripts\activate
```

Dependencies herunterladen
```
pip install -r requirement.txt
```

Programm starten
```
python main.py
```
    
## Usage

Programm in der Commandline starten
```
python main.py
```

Abfragen beantworten
```
Wie hoch ist die Kamera? (in cm) [Höhe]
Wie weit ist die Kamera vom Text entfernt? (in cm) [Entfernung]
Gib ein Wort ein! [Wort]
```

GUI wird geöffnet

![Darstellung](https://github.com/MrGameSucht/CamcarpetCreate/blob/main/CamcarpetGUI.png)

Fenster schließen zur PDF Erstellung
```
Möchtest du den Camcarpet auf A4? (j) Ja, (n) Nein [Antwort]
```

Für Antwort "ja"
```
Welches Format? (h) Hochformat, (q) Querformat [Format]
Welchen scale möchtest du? [Scale]
```

Bild wird angezeigt (hier nicht das orignale Format)

![Bild](https://github.com/MrGameSucht/CamcarpetCreate/blob/main/CamcarpetA4.png)

Bei zufriedenem Ergebnis, Bild speicher
```
Möchtest du das Bild speichern? (j) Ja, (n) Nein [Antwort]
```
Bild wird im Ordner Image gespeichert.
## Real Life Usage

Um das Bild im echten Leben zu benutzen folgende Schritte befolgen:

- Gepseichertes Bild ausdrucken, dabei auf die Formatierung des Druckers achten.
- Kamera in angebene Entfernung und Höhe bringen.
- Kamera am roten Strich in der Mitte ausrichten.
- Foto machen und beeindrucken!
## License

[MIT](https://choosealicense.com/licenses/mit/)

