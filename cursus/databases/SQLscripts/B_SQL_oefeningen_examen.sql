#ex1

use database_tennis;

-- select s.spelersnr, naam, count(b.bedrag) as aantal, sum(b.bedrag) as totaal
-- from spelers s 
-- join bestuursleden as bl using(spelersnr) 
-- join boetes b using(spelersnr)
-- where EIND_DATUM is null and year(DATUM) < 1990
-- group by s.spelersnr
-- order by totaal

# andere oplossingen
-- select s.spelersnr, s.naam,count(boete.betalingsnr) as aantal,sum(boete.bedrag) as totaal
-- from spelers as s
-- join (select bl.spelersnr
-- from bestuursleden as bl
-- where eind_datum is null) as actbestlid using (spelersnr)
-- join (select b.spelersnr,b.bedrag,b.betalingsnr
-- from boetes as b
-- where year(datum) < 1990) as boete using(spelersnr)
-- group by s.spelersnr
-- order by totaal

-- use database_tennis; #spelers as s,bestuursleden as bl,boetes as b,wedstrijden as w, teams as t
-- select s.spelersnr,s.naam,count(b.bedrag) as aantal,sum(b.bedrag) as totaal_bedrag
-- from spelers as s,boetes as b
-- join (select spelersnr from bestuursleden as bl where bl.eind_datum is null) as best using (spelersnr)
-- where s.spelersnr = best.spelersnr and year(b.datum) < 1990
-- group by spelersnr
-- order by totaal_bedrag


#ex2 Geef de spelers (woonplaats, naam, geslacht, in volgorde van hun geslacht en naam) voor
#wie minstens  ́éen boete betaald werd maar die geen aanvoerder zijn van een team.Werk 2
#totaal verschillende oplossingen uit


-- select s.naam,s.plaats,s.geslacht
-- from spelers as s
-- where s.spelersnr not in (select t.spelersnr
-- from teams as t) and s.spelersnr in (select b.spelersnr from boetes as b)
-- group by s.spelersnr
-- order by s.geslacht,s.naam

-- use database_tennis;
-- select s.naam,s.plaats,s.geslacht
-- from spelers as s
-- join boetes as b using (spelersnr)
-- where s.spelersnr not in (select t.spelersnr from teams as t)
-- group by s.spelersnr
-- order by s.geslacht,s.naam

-- use database_tennis;
-- select s.naam,s.plaats,s.geslacht
-- from spelers as s
-- join boetes as b using (spelersnr)
-- left join teams as t using (spelersnr)
-- where t.spelersnr is null
-- group by s.spelersnr
-- order by s.geslacht,s.naam

#ex3 Geef het aantal verschillende spelers dat ooit een wedstrijd gespeeld 

-- select count(distinct w.spelersnr)as aantal
-- from wedstrijden as w

-- select count(s.spelersnr) as aantal
-- from spelers as s
-- join (select w.spelersnr from wedstrijden as w group by w.spelersnr)  as  wed on wed.spelersnr = s.spelersnr

-- select count(s.sp) as aantal
-- from (select s.spelersnr as sp
-- from spelers as s
-- join wedstrijden as w using(spelersnr)
-- group by spelersnr) as s

# 4 Welke speler(s) hebben ooit het maximum boetebedrag, dat ooit betaald werd, betaald ?
#Sorteer alfabetisch op basis van de familienaam

-- select s.voorletters, s.naam
-- from spelers as s
-- join boetes as b using (spelersnr)
-- where b.bedrag = (select max(b.bedrag) 
-- from boetes as b)
-- order by naam

#5 Geef een lijst van al de spelers die in Zoetermeer of Amsterdam wonen (nummer, naam,
#woonplaats en geslacht waarbij je als geslacht “man” of “vrouw”
#geeft). Geef twee mogelijke manieren om dit te doen.

-- select s.spelersnr,s.naam,s.plaats, case
-- 					when s.geslacht = 'v' then 'vrouw'
--                     else  'man'
--                     end as 'm-v'
-- from spelers as s
-- where s.plaats = 'zoetermeer' or s.plaats = 'amsterdam'

-- select s.spelersnr,s.naam,s.plaats, if(s.geslacht = 'v' , 'vrouw','man') 
-- from spelers as s
-- where s.plaats = 'zoetermeer' or s.plaats = 'amsterdam' 

#ex6 Welke speler heeft in totaal een boetebedrag dat dubbel zo hoog is als het totale bedrag van
#speler 104

-- select s.spelersnr,s.naam,concat(s.straat," ",s.huisnr," ",s.postcode," ",s.plaats) as adres
-- from spelers as s
-- join boetes as b using (spelersnr)
-- group by spelersnr
-- having sum(b.bedrag) = (select sum(b.bedrag)*2
-- from boetes as b
-- where b.spelersnr = 104)

-- select b.spelersnr
-- from boetes as b
-- group by b.spelersnr
-- having sum(b.bedrag)  =
-- (select sum(b.bedrag)*2
-- from boetes as b
-- where b.spelersnr = 104) 

#ex7 En welke speler(s) hebben evenveel boetes betaald dan Niewenburg B uit Rijswijk ?

-- select s.spelersnr, naam
-- from spelers s join boetes b using(spelersnr)
-- where s.spelersnr != (select spelersnr
-- 					from spelers 
-- 					where naam = 'Niewenburg' and voorletters = 'B' and plaats = 'Rijswijk')
-- group by b.spelersnr
-- having count(b.betalingsnr) =
-- 	(select count(betalingsnr)
-- 	from spelers join boetes using(spelersnr) 
-- 	where naam = 'Niewenburg' and voorletters = 'B' and plaats = 'Rijswijk')

-- select s.spelersnr,s.naam
-- from spelers as s
-- join boetes as b using (spelersnr)
-- group by spelersnr
-- having count(b.bedrag) = (select count(b.bedrag) as aantal
-- from spelers as s
-- join boetes as b using (spelersnr)
-- where s.naam = 'niewenburg')
-- and s.naam != 'niewenburg'


#ex 8 Bereken per speler het totaal bedrag aan boetes dat deze speler betaald heeft. Vande speler
#moet je zijn/haar nummer en naam weergeven, samen met het berekende totaal

-- select s.spelersnr,s.naam,sum(bedrag)
-- from spelers as s

-- 	join boetes as b using (spelersnr)
--     group by s.spelersnr
--     order by spelersnr

#ex 9 Geef per team de verloren wedstrijden. Zorg dat teams zonder verloren wedstrijden ook in
#de output verschijnen. Duid per wedstrijd aan of het om een actief bestuurslid gaat. Sorteer
#op divisie en wedstrijdnummer.

-- select w.teamnr,t.divisie,w.wedstrijdnr, w.spelersnr,if(w.spelersnr in (select bl.spelersnr 
-- from bestuursleden as bl
-- where bl.eind_datum is null), 'actief', "---") as bestuurslid
-- from wedstrijden as w
-- join teams as t using (teamnr)
-- where w.verloren = 3 
-- group by w.wedstrijdnr
-- order by divisie,wedstrijdnr



-- select w.teamnr, t.divisie, w.wedstrijdnr,w.spelersnr, case 
-- 				when bl.eind_datum is not null then "actief"
--                 end as bestuurslid
-- from wedstrijden as w
-- left join teams as t using (teamnr)
-- left join bestuursleden as bl on bl.spelersnr = w.spelersnr
-- where (w.verloren-w.gewonnen) > 0 
-- group by w.wedstrijdnr
-- order by t.divisie, W.wedstrijdnr


#ex 10 Geef voor alle spelers die geen penningmeester zijn of zijn geweest alle gewonnen wedstrijden,
#gesorteerd op wedstrijdnummer.

-- select w.spelersnr,w.wedstrijdnr
-- from wedstrijden as w
-- where w.gewonnen = 3 and w.spelersnr not in (select bl.spelersnr 
-- from bestuursleden as bl
-- where bl.functie = 'penningmeester')
-- order by w.wedstrijdnr


-- select w.spelersnr, w.wedstrijdnr
-- from wedstrijden as w
-- left join
-- 	(select bl.spelersnr 
-- 	from bestuursleden as bl
-- 	where bl.functie = 'penningmeester'
-- 	group by bl.spelersnr) as best using (spelersnr) 
-- where best.spelersnr IS NULL and w.gewonnen = 3











