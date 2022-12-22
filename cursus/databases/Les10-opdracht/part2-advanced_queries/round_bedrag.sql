use database_tennis;
select s.naam,b.betalingsnr,round(b.bedrag) as afgerond_bedrag
from boetes as b
join spelers as s using (spelersnr)