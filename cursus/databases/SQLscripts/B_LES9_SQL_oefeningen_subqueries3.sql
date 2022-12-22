
use database_tennis;

#1 geef het totaal aantal boetes, het totale boetebedrag, het minimum en het maximum boetebedrag 
#dat door onze club betaald werd. Let er hierbij op dat er gehele getallen worden getoond (rond af indien nodig). 
# van voor naar achter, oplopend. Deze opgave behoeft geen subquery.

-- select count(bedrag) as aantal_boetes,
-- 	format(sum(bedrag),0) as totaal_boetes,
-- 	round(min(bedrag))as minimum,
-- 	round(max(bedrag)) as maximum
-- from boetes

#2 Geef voor elke aanvoerder het spelersnr, de naam en het aantal boetes dat voor hem of haar betaald 
# en het aantal teams dat hij of zij aanvoert. Toon enkel aanvoerders die boetes gekregen hebben. 
#Sorteer van voor naar achter, oplopend.

-- select s.spelersnr,s.naam,count(b.betalingsnr),sub.aantal_teams #juist
-- from spelers as s 
-- join boetes as b on s.spelersnr = b.spelersnr 
-- 	join (select spelersnr, count(teamnr) as aantal_teams
-- 				from teams
-- 				group by spelersnr) as sub on s.spelersnr = sub.spelersnr
-- group by s.spelersnr

-- use database_tennis; #spelers as s,bestuursleden as bl,boetes as b,wedstrijden as w, teams as t
-- select t.spelersnr,s.naam,s.voorletters,count(b.betalingsnr) as aantal_boetes,ta.aantal_teams
-- from teams as t
-- join spelers as s using (spelersnr)
-- join boetes as b using (spelersnr)
-- join (select count(t.teamnr) as aantal_teams,t.spelersnr 
-- from teams as t
-- group by t.spelersnr) as ta on ta.spelersnr = t.spelersnr
-- group by spelersnr
-- order by spelersnr

#3 Geef een lijst met het spelersnummer en de naam van de spelers die in Rijswijk wonen en die in 1980
# een boete gekregen hebben van 25 euro (meerdere voorwaarden dus). 
#Gebruik hiervoor geen exists operator maar wel zijn tegenhanger die meestal bij niet-gecorreleerde 
#subquery's wordt gebruikt. Sorteer van voor naar achter, oplopend.
 
-- select s.spelersnr,s.naam
-- from spelers as s
-- join boetes using (spelersnr)
-- where plaats = "rijswijk" and extract(year from datum) = 1980 and bedrag = 25
-- order by 1 asc,2 asc

-- select s.spelersnr,naam from spelers s
-- inner join (select spelersnr from boetes where bedrag = 25 and extract(year from datum) = 1980) as sub
-- on s.spelersnr = sub.spelersnr
-- order by 1 asc,2 asc


#4 Geef alle spelers voor wie meer boetes zijn betaald dan dat ze wedstrijden hebben gespeeld. 
#Zorg dat spelers zonder wedstrijd ook getoond worden.
#Sorteer van voor naar achter, oplopend.

-- select naam, voorletters, date(geb_datum) as geb_datum # dit werkt
-- from spelers as s 
-- where (select count(*)
-- 	from boetes as b
--     where s.spelersnr = b.spelersnr) > 
--     (select count(*)
--     from wedstrijden as w
--     where s.spelersnr = w.spelersnr)
-- order by 1,2

-- select naam,voorletters, geb_datum #juist oplossing Brent
-- from spelers as s
-- 	inner join (select spelersnr,count(wedstrijdnr) as aantalwedstrijden
-- 		from wedstrijden
--         group by spelersnr) q1 on s.spelersnr = q1.spelersnr
-- 	inner join (select spelersnr,count(betalingsnr) as aantalboetes
-- 		from boetes
--         group by spelersnr) q2 on s.spelersnr = q2.spelersnr
-- 	where aantalwedstrijden < aantalboetes


#5 geef alle spelers die geen wedstrijd hebben gespeeld voor team1
#sorteer op naam daarna op nr


-- select s.spelersnr,naam 
-- from spelers as s 
-- 	where s.spelersnr not in (select w.spelersnr from wedstrijden as w where w.teamnr = 1) 
-- order by naam,spelersnr


#6 Geef voor elke speler die ooit een boete heeft betaald, de hoogste boete weer en 
#hoe lang het is geleden dat deze boete werd betaald. Sorteer van groot naar klein op bedrag
#en van klein naar groot op "leeftijd" van de boete 

-- select s.spelersnr,bh.hb as bedrag,bh.db as verschil #dit verschil hoeft nog bijwerking...
-- from spelers as s
-- join (select b.spelersnr,max(b.bedrag) as hb, (now() - b.datum) as db
-- from boetes as b
-- group by b.spelersnr)as bh using (spelersnr)  

#7 Welke spelers hebben voor alle teams gespeeld uit de teamstabel? 
#dwz voor welke speler bestaat er geen enkel team in de teams tabel waar betreffende 
#speler nooit heeft gespeeld.Sorteer op spelersnr. Gebruik de exists operator


#8 IDEM ALS OEF 9 VAN LES 7... Maak een lijst met de spelers (naam, voorletters,woonplaats) die ooit gespeeld heeft voor 
#een team dat nu in tweede divisie speelt en waarvoor geen enkele boete betaald werd voor
# 1 januari 1981.Sorteer van voor naar achter ,oplopend. Zorg dat geen dubbels worden getoond.


-- select distinct naam, voorletters, plaats
-- from spelers s 
-- join wedstrijden w on s.spelersnr = w.spelersnr 
-- join teams t on w.teamnr = t.teamnr 
-- left join boetes b on s.spelersnr = b.spelersnr
-- where divisie = 'tweede' and s.spelersnr not in (
--                                                     select spelersnr
--                                                     from boetes
--                                                     where datum < '1981-01-01')
-- order by naam,voorletters,plaats


        

	
 
 
 
            

