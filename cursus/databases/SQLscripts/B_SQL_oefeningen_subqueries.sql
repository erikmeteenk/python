use database_tennis;
# subqueries kunnen overal geplaatst worden: select, where 
-- select s.naam, s.voorletters, s.plaats, w.wedstrijdnr, w.spelersnr, t.divisie 
-- from wedstrijden as w
-- 	join teams as t using (teamnr)
-- 	join spelers as s on s.spelersnr = w.spelersnr
-- where divisie = "tweede" and w.spelersnr not in (select b.spelersnr from boetes as b where b.datum < "1981-1-1")
-- group by s.naam


#toon alle aanvoerders hun spelersnr,naam,voorletters, aantal boetes gekregen 
#en aantal teams waarvoor hij aanvoerder is

select  s.spelersnr ,naam, voorletters,count(betalingsnr), aantal_teams
from spelers as s
join teams as t using (spelersnr)
join boetes as b using (spelersnr)
join (select t.spelersnr,count(t.teamnr) as aantal_teams
		from teams as t
		group by spelersnr) as sub on s.spelersnr = sub.spelersnr
group by spelersnr
