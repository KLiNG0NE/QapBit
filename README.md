# QapBit #

Videobitratenrechner

![](film-frames.png)

**QapBit** berechnet die Videobitrate. Dieser Wert wird für Videcodecs z. B. bei der *variablen Bitrate* angegeben. – Die Bitrate kann zwar berechnet werden, jedoch schwankt die reale Bitrate je nach verwendetem Codec und Ausgangsmaterial. Daher kann dieser Wert nur einen ungefähren Richtwert darstellen.

> QapBit – „Qap“ bedeutet „funktionieren“ → „funktionierende Bitrate“

---

## Übersicht ##

- [Funktion](#funktion)
- [Screenshot](#screenshot)
- [Installation/Ausführen](#installationausführen)
- [Kompilieren](#kompilieren)
- [Lizenzen](#lizenzen)

---

## Funktion ##

Ein kleines Tool zur Berechnung der Videobitrate.

- Berechnung basierend auf Zielgröße (MiB) und Dauer.
- Berücksichtigung von Audio-Bitrate und Container-Overhead.
- Verschiedene Presets für gängige Medien.

---

## Screenshot ##

![](Screenshot.png)

---

## Installation/Ausführen ##

### Alle OS ###

Nachdem [Python](https://www.python.org/) für das jeweilige Betriebssystem installiert wurde kann die Datei ``qapbit.py`` ausgeführt werden:

```
python qapbit.py
```

Das Program wurde unter Windows 11 mit Python 3.12.10 getestet. Die Python-Version kann mit folgendem Befehl ermittelt werden:

```
python --version
```

---

## Kompilieren ##

Durch Kompilieren des Programs, ist es auch ohne Python-Umgebung auf dem jeweiligen Betriebssystem lauffähig.

### Windows ###

In Windows kann das Programm zu einer EXE-Datei kompiliert werden.

1. Pyinstaller via *PIP* installieren:

```
pip install pyinstaller
```

2. Mit *Pyinstaller* kompilieren:

```
pyinstaller --onefile --windowed qapbit.py
```

Anschließend ist die EXE-Datei im Unterordner ``\dist`` auffindbar. Diese Datei kann einfach per Doppelklick ausgeführt werden. (Die Grafiken sollten im selben Ordner liegen.)

---

## Lizenzen ##

Folgende Lizenzen sind zu beachten:

### Eigener Code ###

<img src="gpl-v3-logo.png" alt="GPL-Logo" width="128">

- [GNU GENERAL PUBLIC LICENSE Version 3](LICENSE)

### Externe Quellen ###

Folgende externe Quellen wurden genutzt:

#### Grafiken ####

- https://openmoji.org/

#### Fonts ####

- [Liberation Fonts](https://github.com/liberationfonts/liberation-fonts)
- [Fira Code](https://github.com/tonsky/FiraCode)

---

[KLiNG0NE](https://github.com/KLiNG0NE/) – [QapBit](https://github.com/KLiNG0NE/QapBit/)
