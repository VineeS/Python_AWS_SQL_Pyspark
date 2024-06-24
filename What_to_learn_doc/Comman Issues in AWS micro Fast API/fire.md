## code for cli-fire.py

#!/usr/bin/env python
import fire
from myLib.logic import wiki

## python interpreter only run a script

if **name** == "**main**":
fire.Fire(wiki)

### commands for running the main as cli

(.venv) vinee@Vinees-MBP Python-AWS-FastAPI-microservicces % touch cli-fire.py
(.venv) vinee@Vinees-MBP Python-AWS-FastAPI-microservicces % chmod +x cli-fire.py
(.venv) vinee@Vinees-MBP Python-AWS-FastAPI-microservicces % ./cli-fire.py --help
env: /python: No such file or directory
(.venv) vinee@Vinees-MBP Python-AWS-FastAPI-microservicces % ./cli-fire.py --help
INFO: Showing help with the command 'cli-fire.py -- --help'.

zsh: suspended ./cli-fire.py --help
(.venv) vinee@Vinees-MBP Python-AWS-FastAPI-microservicces % ./cli-fire.py --help
INFO: Showing help with the command 'cli-fire.py -- --help'.

zsh: suspended ./cli-fire.py --help
(.venv) vinee@Vinees-MBP Python-AWS-FastAPI-microservicces % ./cli-fire.py  
A war god in mythology associated with war, combat, or bloodshed.
(.venv) vinee@Vinees-MBP Python-AWS-FastAPI-microservicces % ./cli-fire.py --length 10
A war god in mythology associated with war, combat, or bloodshed. They occur commonly in polytheistic religions.
Unlike most gods and goddesses in polytheistic religions, monotheistic deities have traditionally been portrayed in their mythologies as commanding war in order to spread religion. (The intimate connection between "holy war" and the "one true god" belief of monotheism has been noted by many scholars, including Jonathan Kirsch in his book God Against The Gods: The History of the War Between Monotheism and Polytheism and Joseph Campbell in The Masks of God, Vol. 3: Occidental Mythology.)
The following is a list of war deities:

== Africa ==

=== Egyptian ===

Anat-- also known as Anath-- was a goddess of fertility, sexuality, love, and war. She was the sister of Baal
Anhur, god of war, not a native god
Anuke, a goddess of war and consort of Anhur
Apedemak, the lion god of war: he is sometimes depicted with three heads
Bast, cat-headed goddess associated with war, protection of Lower Egypt and the pharaoh, the sun, perfumes, ointments, and embalming
Horus, god of the king, the sky, war, and protection
Maahes, lion-headed god of war
Menhit, goddess of war, "she who massacres"
Montu, falcon-headed god of war, valor, and the Sun
Neith, goddess of war, hunting, and wisdom
Pakhet, goddess of war
Satis, deification of the floods of the Nile River and an early war, hunting, and fertility goddess
Sekhmet, goddess of warfare, pestilence, and the desert
Set, god of the desert and storms, associated with war
Sobek, god of the Nile, the army, military, fertility, and crocodiles
Sopdu, god of the scorching heat of the summer sun, associated with war
Wepwawet, wolf-god of war and death who later became associated with Anubis and the afterlife

=== Berber ===
Gurzil, bull-headed warrior god.

=== Nilo-Saharan ===
Nubian

Apedemak, Nubian lion-headed warrior god.

=== Western African-Congo ===
Yoruba

Kokou
Ogoun
Oya

=== Eastern African-Congo ===
Igbo

Amadioha
Ekwensu

=== Ethiopian ===
Maher, god of war.

=== Kenya ===
Kalenjin

Boryet, Kipsigis Death-wielding god of war. Boryet (also luket) is the act of war.
(.venv) vinee@Vinees-MBP Python-AWS-FastAPI-microservicces %

### we can also test a different name from main.py -> logic.py

(.venv) vinee@Vinees-MBP Python-AWS-FastAPI-microservicces % ./cli-fire.py --name "Lebanon"
Lebanon ( LEB-ə-non, -⁠nən; Arabic: لُبْنَان, romanized: Lubnān, local pronunciation: [lɪbˈneːn]), officially the Republic of Lebanon, is a country in the Levant region of West Asia.

# the above code took 1 line from wiki and showed

##### ------ Now added a new function

main.py ->

#!/usr/bin/env python
import fire
from myLib import logic

## python interpreter only run a script

if **name** == "**main**":
fire.Fire(logichelp)

logic.py --> ## want to check all the functions in logic.py not just wiki
import wikipedia

def wiki(name="War Goddess", length=1):
"""This is Wiki Fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki

def search_wiki(name):
"""search wiki for names"""
res = wikipedia.search(name)
return res

(.venv) vinee@Vinees-MBP Python-AWS-FastAPI-microservicces % ./cli-fire.py search_wiki "Barack"
Barack Obama
Barack Obama Sr.
Presidency of Barack Obama
Family of Barack Obama
Barack (name)
Barack (brandy)
Zach Barack
Barack (disambiguation)
Early life and career of
