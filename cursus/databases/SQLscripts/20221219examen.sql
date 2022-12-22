#Vraag1
-- use database_tennis;
-- select count(b.bedrag) as totaalBoetesGroter50
-- from boetes as b
-- where b.bedrag > 50



#Vraag2
-- use database_tennis;
-- select s.spelersnr,s.naam,count(b.bedrag) as aantal_boetes,sum(b.bedrag) as totaal_bedrag
-- from spelers as s,boetes as b
-- where s.spelersnr = b.spelersnr and year(b.datum) < 1990
-- group by s.spelersnr
-- order by s.spelersnr



#vraag3
-- use database_tennis;
-- select distinct spelersnr, wedstrijdnr  
-- from spelers s inner join wedstrijden using(spelersnr)
-- where gewonnen > verloren and spelersnr not in (select spelersnr
--                                             from bestuursleden join spelers using(spelersnr)
--                                             where functie = 'Penningmeester')
-- order by WEDSTRIJDNR


#vraag4
-- use database_tennis;
-- select s.spelersnr,s.naam,b.datum,b.bedrag
-- from spelers as s, boetes as b
-- where s.spelersnr = b.spelersnr and s.plaats = 'Den Haag' and b.bedrag > 50
-- order by s.spelersnr,b.betalingsnr 


#vraag5
-- use database_tennis;
-- select count(b.bedrag) as aantal_boetes,round(sum(b.bedrag)) as totaal_bedrag,
-- round(min(b.bedrag)) as minimum,round(max(b.bedrag)) as maximum
-- from boetes as b
-- order by aantal_boetes,totaal_bedrag,minimum,maximum


#vraag6
-- use database_tennis;
-- select s.naam,s.voorletters
-- from spelers as s
-- join boetes as b using (spelersnr)
-- where s.spelersnr = b.spelersnr and b.bedrag = (select max(b.bedrag) from boetes as b)
-- order by s.naam

#vraag7
-- use database_tennis;
-- select s.spelersnr, s.bondsnr
-- from spelers as s
-- where s.geb_datum > (select s.geb_datum from spelers as s where bondsnr = 8467)
-- order by s.spelersnr


#vraag8
use database_tennis;
select s.spelersnr, s.naam, s.voorletters
from spelers as s
join boetes as b using (spelersnr)
group by spelersnr
having count(b.bedrag) = (select count(b.bedrag) 
from boetes as b
join spelers as s using (spelersnr)
where s.naam = 'Moerman' and s.voorletters = 'D' and s.plaats = 'Zoetermeer')
and s.naam <> 'Moerman'


#vraag9
-- select s.spelersnr,s.naam,year(s.geb_datum) as geboortejaar
-- from spelers as s
-- where s.plaats = 'zoetermeer'



#vraag10
-- SELECT
-- ROUND(AVG(b.bedrag),2) AS "gemiddelde boete",
-- ROUND(MIN(b.bedrag),2) AS "kleinste boete",
-- ROUND(MAX(b.bedrag),2) AS "grootste boete"
-- FROM boetes AS b
