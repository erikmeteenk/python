use database_tennis; #spelers as s,bestuursleden as bl,boetes as b,wedstrijden as w, teams as t

select bll.spelersnr,s.naam,count(b.bedrag) as aantal,round(sum(b.bedrag)) as bedrag
from  (select bl.spelersnr 
 from bestuursleden as bl
 where bl.eind_datum is null) as bll
join boetes as b using (spelersnr)
join spelers as s using(spelersnr)
where bll.spelersnr in (select b.spelersnr from boetes as b where year(datum) < 1990)
group by s.spelersnr
order by b.bedrag




















