use database_tennis;

select s.spelersnr,s.bondsnr,(select date(s.geb_datum) as criterion8467 from spelers as s
where s.bondsnr = 8467) as criterion
from spelers as s
where geb_datum  > (select date(s.geb_datum) as criterion
from spelers as s
where s.bondsnr = 8467)
order by s.spelersnr

