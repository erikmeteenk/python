use database_tennis;

#1 Geef een lijst met het spelersnummer, de naam van de speler, de datum van de boete en het
#bedrag van de boete van al de spelers die een boete gekregen hebben met een bedrag groter
#dan 45,50 euro en in Rijswijk wonen. Sorteer op spelersnr en het volgnummer van de boete.
#Gebruik expliciete joins.


-- select s.spelersnr, s.naam, s.plaats, b.datum, b.bedrag,b.betalingsnr 
-- from spelers as s  
-- join boetes as b on s.spelersnr = b.spelersnr
-- where b.bedrag > 45.5 and s.plaats = "rijswijk"
-- order by s.spelersnr, b.betalingsnr

#2 Maak een lijst van alle mannelijke aanvoerders van een team. Geef voor die aanvoerders 
#de wedstrijden waarin ze gespeeld hebben. Geef ook aanvoerders die geen wedstrijd gespeeld
#hebben. Hierbij toon je voor deze spelers het spelersnummer en de volledige naam, voor het
#team de divisie en voor de wedstrijd het wedstrijdnummer. Sorteer aflopend op het wedstrijdnummer.

-- select s.spelersnr,s.naam,s.voorletters, t.divisie, w.wedstrijdnr
-- from spelers as s
-- join wedstrijden as w using (spelersnr)
-- right join teams as t using (spelersnr)
-- where s.geslacht = "m"
-- order by w.wedstrijdnr desc

-- select s.spelersnr,s.naam,s.voorletters,t.divisie,w.wedstrijdnr
-- from spelers as s 
-- join wedstrijden as w using (spelersnr)
-- join teams as t using(teamnr)
-- where t.spelersnr = w.spelersnr and s.geslacht = "m"
-- order by w.wedstrijdnr desc

#3Geef voor elke wedstrijd het wedstrijdnummer en de volledige naam van de aanvoerder van
#het team waarvoor de wedstrijd werd gespeeld. Sorteer je resultaat volgens het wedstrijd-
#nummer in oplopende volgorde.

-- use database_tennis; #spelers as s,bestuursleden as bl,boetes as b,wedstrijden as w, teams as t
-- select w.wedstrijdnr,s.naam,s.voorletters
-- from wedstrijden as w 
-- join teams as t on w.teamnr = t.teamnr
-- join spelers as s on t.spelersnr = s.spelersnr
-- #group by w.wedstrijdnr
-- order by w.wedstrijdnr asc



-- select w.wedstrijdnr, w.teamnr, s.naam, s.voorletters
-- from wedstrijden as w
-- join teams as t using (teamnr)
-- join spelers as s on s.spelersnr =t.spelersnr 
-- order by w.wedstrijdnr asc

#4 Geef het spelersnummer en bondsnummer van alle spelers die jonger zijn dan de speler met
#bondsnummer 8467. Sorteer op spelersnr.

-- select s.spelersnr,s.bondsnr#,s.geb_datum
-- from spelers as s
-- where s.geb_datum > (  
-- select s.geb_datum 
-- from spelers as s 
-- where s.bondsnr = 8467)

-- select s.spelersnr, s.naam,s.geb_datum,  (select date(s.geb_datum) as criterion8467 from spelers as s
-- where s.bondsnr = 8467) as criterion
-- from spelers as s
-- where geb_datum  > (select date(s.geb_datum) as criterion
-- from spelers as s
-- where s.bondsnr = 8467)
-- order by s.spelersnr


#5 Selecteer de naam van de spelers die Voorzitter geweest zijn, en de periode in 1 kolom. Sor-
#teer van meest recent naar minst recent.

-- select s.naam,bl.functie,case
-- 					when eind_datum is not null then concat(bl.begin_datum," - ",bl.eind_datum)
--                     else concat (bl.begin_datum, " - ", "heden")
--                     end as periode
-- from bestuursleden as bl, spelers as s
-- where s.spelersnr = bl.spelersnr and bl.functie = "voorzitter"
-- order by begin_datum desc

-- select concat_ws( "    ",s.naam, begin_datum, " tot ", eind_datum ) as voorzitters
-- from bestuursleden as bl
-- join spelers as s using (spelersnr)
-- where bl.functie = "voorzitter" #and bl.EIND_DATUM is null
-- order by bl.begin_datum desc





