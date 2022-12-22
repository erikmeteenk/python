use database_tennis;
select s.spelersnr,s.plaats
from spelers as s
where s.plaats in (
select s.plaats from spelers as s
group by s.plaats
having count(s.plaats) >1)
order by s.plaats desc,s.spelersnr





