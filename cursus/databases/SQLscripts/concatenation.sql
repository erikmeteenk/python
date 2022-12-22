use database_tennis;
select spelersnr, concat(naam, " ", voorletters) as naam,plaats,postcode from spelers
where plaats = 'den haag'
#group by naam
order by naam

