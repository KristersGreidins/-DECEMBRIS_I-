"""Izveidojiet Python programmu, kas atkarībā no pašreizējās stundas izvada atbilstošu sveicienu, izmantojot if priekšrakstu. (labrīt, labdien, labvakar)
Izmantojiet GIT, lai izsekotu kodu un veidotu komitus."""

import time

sis_bridis=time.localtime().tm_hour

if 5 <= sis_bridis < 12:
    print("Labrīt!")
elif 12 <= sis_bridis < 18:
    print("Labdien!")
else:
    print("Labvakar!")