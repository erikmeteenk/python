use database_tennis;
#1
-- select spelersnr, naam, jaartoe from spelers
-- where plaats = "zoetermeer"

#2
-- select teamnr, spelersnr, divisie
-- from teams
-- where SPELERSNR = 27 

#3select datum, bedrag from boetes
#where bedrag < 75
#order by datum

#4
-- select wedstrijdnr,teamnr,gewonnen,verloren from wedstrijden
-- where teamnr = 1 and gewonnen = 0 or verloren = 0

#5
-- select spelersnr,functie,eind_datum from bestuursleden
-- where eind_datum is null

#6
-- select spelersnr,functie,eind_datum from bestuursleden
-- where eind_datum is null

#7
-- select count(bedrag) from boetes

#8
-- select count(wedstrijdnr) from wedstrijden

#9 
-- select naam, jaartoe,straat
-- from spelers
-- where straat like '%weg' or straat like '%laan'
 
#10
-- select min(begin_datum) from bestuursleden
#11
-- select wedstrijdnr, spelersnr, gewonnen, verloren
-- from wedstrijden
-- where gewonnen = 3 and teamnr = 2

#12
-- select wedstrijdnr, spelersnr, gewonnen, verloren, (gewonnen-verloren) as verschil
-- from wedstrijden
-- where spelersnr = 6

#13
-- select spelersnr,functie
-- from bestuursleden
-- where eind_datum is null
-- order by begin_datum

#14
-- select spelersnr,wedstrijdnr,gewonnen,verloren, case
-- 							when gewonnen = 3 then 'gewonnen'
--                             else 'verloren'
--                             end as resultaat
-- from wedstrijden
-- where spelersnr = 6

#15
-- select spelersnr as speler, year(datum) as jaar, bedrag
-- from boetes
-- where bedrag > 75 and year(datum) < 1984

#16
-- select s.spelersnr,s.naam,s.voorletters
-- from spelers as s, teams as t 
-- where s.SPELERSNR = t.spelersnr and geslacht = "v"
#join teams using (spelersnr)
#where geslacht = "v"

#17
-- select distinct s.spelersnr, concat(s.voorletters," ",s.naam) as spelersnaam
-- from spelers as s
-- join wedstrijden as w using (spelersnr)
-- where naam like '%e%' or '%E%'

#18 

-- select t.divisie
-- from teams as t,wedstrijden as w
-- where t.teamnr = w.teamnr and w.spelersnr in 
-- 		(select bl.spelersnr
-- 		from bestuursleden as bl,boetes as b
--         where bl.spelersnr = b.spelersnr and bl.eind_datum is null)
-- group by t.divisie
