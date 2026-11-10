# Määrittelydokumentti


#### Opinto-ohjelma: Tietojenkäsittelytieteen kandiohjelma (TKT)

Projektissa toteutetaan kirjoitusvirheiden korjaaja, joka käyttää Levenshtein-etäisyyttä käyttäjän kirjoittaman sanan vertaamiseen sanakirjan sanoihin

#### Ohjelmointikieli:
Python

#### Muut hallitsemani ohjelmointikielet: 
- Java
- Javascript

#### Projektin aihe: 
Ohjelman tarkoituksena on tunnistaa käyttäjän kirjoittamat virheet, sekä ehdottaa niille korjauksia. Ohjelma vertaa käyttäjn syöttämää sanaa sanakirjan sanoihin ja etsii sille lähimmät vaihtoehdot. 
Ohjelma ehdottaa lähintä sanaa sanakirjasta. 

### Algoritmit ja tietorakenteet:
##### Algoritmit:
- Levenshtein-etäisyys
- Dynaaminen ohjelmointi

##### Tietorakenteet
- 2-uloitteinen taulukko
- lista
- dictionary

### Syötteet: 
Ohjelma saa syötteenä käyttäjän kirjoittaman sanan ja sanakirjan, joka sisältää oikieta sanoja

##### Esimerkki:
Syöte: alogritmi

Tuloste: algoritmi

#### Aika- ja tilavaativuudet: 
Levenshtein-etäisyyden laskeminen kahden sanan välillä:
- aikavaativuus: O(mn)
- tilavaativuus: O(mn)
  
(m ja n ovat vartailtavien sanojen pituudet)

Jos sanakirjassa on x sanaa, yhden haun kokonaisaikavaativuus on:
- O(kmn)

#### Harjoitustyön ydin: 
Harjoitustyön ydin on Leveshtein-etäisyysalgoritmin toteuttaminen dynaamisen ohjelmoinnin avulla. Algoritmi
laskee kahden sanan välisen etäisyyden selvittämällä pienimmän mahdollisen määrän merkkioperaatioita:
- kijaimen lisäys
- kirjaimen poisto
- kirjaimen korvaus toisella kirjaimella,

joilla toinen sana voidaan muuntaa toiseksi. Ohjelman muu toiminnallisuus tukee tämän algoritmin käyttöä, mutta
varsinainen painopiste on algoritmin toteutuksessa ja analysoinnissa.

