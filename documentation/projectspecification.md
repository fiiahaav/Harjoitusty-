# Määrittelydokumentti


#### Opinto-ohjelma: Tietojenkäsittelytieteen kandiohjelma (TKT)

Projektissa toteutetaan kirjoitusvirheiden korjaaja, joka käyttää Levenshtein-etäisyyttä käyttäjän kirjoittaman sanan vertaamiseen sanakirjan sanoihin

#### Ohjelmointikieli:
Python

#### Muut hallitsemani ohjelmointikielet: 
- Java
- JavaScript

#### Projektin aihe: 
Ohjelman tarkoituksena on tunnistaa käyttäjän kirjoittamat virheet, sekä ehdottaa niille korjauksia. Ohjelma vertaa käyttäjän syöttämää sanaa sanakirjan sanoihin ja etsii sille lähimmät vaihtoehdot. 
Ohjelma ehdottaa lähintä sanaa sanakirjasta. 

### Algoritmit ja tietorakenteet:
##### Algoritmit:
- Levenshtein-etäisyys
- Dynaaminen ohjelmointi

##### Tietorakenteet
- 2-ulotteinen taulukko
- lista
- dictionary

### Syötteet: 
Ohjelma saa syötteenä käyttäjän kirjoittaman sanan ja sanakirjan, joka sisältää oikeita sanoja

##### Esimerkki:
Syöte: alogritmi

Tuloste: algoritmi

#### Aika- ja tilavaativuudet: 
Levenshtein-etäisyyden laskeminen kahden sanan välillä:
- aikavaativuus: O(mn)
- tilavaativuus: O(mn)
  
(m ja n ovat vertailtavien sanojen pituudet)

Jos sanakirjassa on k sanaa, yhden haun kokonaisaikavaativuus on:
- O(kmn)

#### Harjoitustyön ydin: 
Harjoitustyön ydin on Levenshtein-etäisyysalgoritmin toteuttaminen dynaamista ohjelmointia käyttäen sekä algoritmin soveltaminen kirjoitusvirheiden tunnistamiseen ja korjaamiseen.

Työssä vertaillaan käyttäjän syötettä sanakirjan sanoihin ja etsitään vaihtoehdot, joiden Levenshtein-etäisyys käyttäjän syötteeseen on pienin. Etäisyys lasketaan selvittämällä pienin mahdollinen määrä merkkioperaatioita, joilla toinen sana voidaan muuntaa toiseksi 

Käytettäviä merkkioperaatioita ovat:


- kirjaimen lisäys
- kirjaimen poisto
- kirjaimen korvaus toisella kirjaimella,

Työn pääpaino on etäisyysalgoritmin toteuttamisessa, testaamisessa ja analysoinnissa. Ohjelman muu toiminnallisuus tukee algoritmin käyttöä, mutta ei ole harjoitustyön varsinainen ydin.

#### Lähteet
- everyfinnishword-projektin suomenkielinen sanalista: https://github.com/hugovk/everyfinnishword