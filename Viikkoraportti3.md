## Vikkoraportti 3 
Viikon aikana olen jatkanut kirjoitusvirheiden korjaajan toteuttamista Pythonilla. Olen kehittänyt projektin ydinalgoritmia ja muuttanut alkuperäisen Levenshtein-etäisyyden ohjaajan palautteen mukaiseksi Damerau-Levenshtein-etäisyydeksi. Algoritmi hyödyntää dynaamista ohjelmointia ja kaksiulotteista taulukkoa.

Olen toteuttanut algoritmin, joka laskee kahden sanan välisen etäisyyden huomioimalla kirjainten lisäämisen, poistamisen, korvaamisen sekä kahden vierekkäisen kirjaimen vaihtamisen.

Olen myös kehittänyt sanakirjan käsittelyä. Ohjelma lukee suomenkielisen sanalistan tiedostosta, joka sisältää noin 93 000 sanaa. Lisäksi olen toteuttanut toiminnallisuuden, joka vertaa käyttäjän syöttämää sanaa sanakirjan sanoihin ja palauttaa viisi lähintä korjausehdotusta.

Olen aloittanut yksikkötestien kirjoittamisen Damerau-Levenshtein-algoritmille. Testeillä tarkistetaan esimerkiksi samojen sanojen vertailua sekä kirjainten lisäämistä, poistamista, korvaamista ja vaihtamista.

Projektin rakennetta ja riippuvuuksien hallintaa on kehitetty ottamalla käyttöön Poetry. Olen myös jatkanut Git-versionhallinnan käyttöä ja päivittänyt projektin dokumentaatiota.

#### Seuraavaksi tehtävät asiat
Seuraavaksi tarkoituksena on toteuttaa oma Trie-tietorakenne sanakirjan tallentamista ja hakemista varten. Lisäksi tarkoituksena on kehittää projektille selainpohjainen käyttöliittymä Flaskilla. Yksikkötestejä tullaan täydentämään ja projektin toteutus- sekä testausdokumentaatiota aloitetaan.
