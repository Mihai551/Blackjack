Am implementat algoritmul unui joc de BlackJack care să fie jucat prin tastarea diferitelor comenzi în consolă.
În primă fază, se citea lista participanţilor dintr-un fişier, iar apoi fiecare jucător era întrebat dacă doreşte să intre in joc. În cazul răspunsului negativ, se trecea peste acesta, iar în cazul răspunsului pozitiv jucătorul era întrebat de suma pe care doreşte să o parieze. Prin intermediul comenzilor, fiecare jucător putea să tragă câte o carte sau să se oprească. Când o mână depăşea 21 de puncte, dacă în aceasta se afla un As, valoarea acestuia se modifica automat din 11 în 1.
Dealer-ul era programat să tragă câte o carte până când mâna sa avea o valoare mai mare sau egală cu 17.
Pentru implementarea jocului, am definit clasele: Carte, Pachet, Dealer şi Jucător.
Clasa “Carte” a fost definită având două atribute care reprezintă tipul cărţii (ex: damă) şi valoarea cărţii (ex: 10)
Clasa “Pachet” a fost definită având trei metode: una pentru construirea pachetului cu obiecte de tip “Carte”, una pentru amestecarea cărţilor şi una pentru a trage cărţile din acesta. 
Clasa “Dealer” a fost definită având o metodă pentru tragerea cărţilor, una pentru calcularea scorului şi două atribute, scorul şi lista cărţilor.
Clasa “Jucător” a fost definită având atributele: nume, vârstă, naţionalitate, sumă totală (citite dintr-un fişier) şi scor, lista cărţilor din mână, sumă pariată, care erau definite în timpul jocului prin intermediul metodelor. Atributul sumă totală se actualizează după fiecare rundă. Au fost definite metode de primire automată a două cărţi, de extragere a unei cărţi din pachet la cerere, de pariat o sumă şi de calculare a scorului.
Într-un fişier, numit “other_methods” am definit metodele “create()”, care creează lista jucătorilor citind dintr-un fişier şi “Joc(dealer, jucatori)”.
În metoda “Joc(dealer, jucatori)” se creează un obiect de tip “Pachet” şi, apoi, este scris codul care are ca rol implementarea derulării jocului şi a regulilor de joc în care se iterează peste lista cu jucători şi se întreabă, pe rând, fiecare jucător dacă intră în joc runda respectivă, cât pariază, dacă mai trage o carte sau se opreşte (după ce acesta a primit deja două cărţi automat la început).
În “main” se iniţializează Dealer-ul şi lista de jucători, cu ajutorul clasei “Dealer” şi a metodei pentru crearea listei, definite anterior şi se apelează metoda “Joc(dealer, jucator)”.
