# CubChase
Python project for faculty subject.


Cub Chase – Simba’s Pride GameBreak (1998)

Napisati igricu nalik Cub Chase igrici. Napraviti šemu lavirinta, sličnu kao u originalnoj
igrici, kroz koje avatari mogu da se kreću.
Uloge:
 Dva ili više igrača, pokreću svog avatara pomoću strelica, odnosno ASDW
tastera:
o Kreću se gore-dole-levo-desno, kroz lavirint.
o Prvi igrač koji prođe kroz deo lavirinta ostavlja trag koji se ne može
promeniti dok traje nivo.
o Na početku nivoa igrači se nalaze na istom delu lavirinta.
o Svaki igrač ima 3 života po nivou. Kada izgubi život igrač se pojavi na
istom mestu odakle je započeo nivo.
 Neprijatelji:
o Kreći se nasumično gore-dole-levo-desno, kroz tunele.
o Na početku nivoa, nalaze se raštrkani po lavirintu.
 Zamka:
o Na početku svakog nivoa na lavirintu se nasumično postavi proizvoljan
broj zamki.
o Kada igrač prvi put pređe preko zamke on je aktivira. Zamka je aktivna
10 sekundi, zatim nestaje iz nivoa.
o Ako neprijatelj dodirne aktiviranu zamku ostaje zarobljen 5 sekundi i
tada igrači ne gube život ako ga dodirnu.
Pravila:
 Igra se beskonačno nivoa (prihvatljivo je napraviti jedan nivo koji se igra
beskonačno mnogo puta).
 Ukoliko neprijatelj dodirne igrača, on gubi život.
 Nakon svakog nivoa neprijatelji se brže kreću.
 Za prelaz na sledeći nivo potrebno je proći svaki deo lavirinta u kom se može
ostaviti trag i stići do izlaza koji je definisan u lavirintu.
 Pobednik je igrač koji ostavio najviše traga u lavirintu, svaki trag se računa sa
100 poena.
 Pri prelasku na sledeći nivo prikazati koliko igrači imaju poena.
 Igrica se završava kada svi igrači izgube sve živote
Za realizaciju koristiti Python3, PyQt5, multiprocessing. Raditi u timovima od 4
člana.Napisati dokumentaciju u kojoj opisuje opšti rad aplikacije i rezimirati prednosti i
mane korišćenja Python jezika, PyQt5 okvira i paralelizacije rada.
