use database_tennis;
SELECT s.naam, b.bedrag as origineel_bedrag, round(b.bedrag*b.bedrag) as bedrag_tot_de_tweede,
sqrt(bedrag*bedrag) as opnieuw_origineel 
from spelers as s,boetes as b
