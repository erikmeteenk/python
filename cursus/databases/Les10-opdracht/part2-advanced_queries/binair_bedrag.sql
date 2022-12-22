use database_tennis;
select b.spelersnr,s.naam,b.bedrag,bin (b.bedrag) as binair ,hex(b.bedrag) as hexadecimaal
from boetes as b,spelers as s
where b.spelersnr = s.spelersnr