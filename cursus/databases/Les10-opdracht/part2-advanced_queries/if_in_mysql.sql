use database_tennis;
SELECT s.naam,IF(b.bedrag<75, 'YES', 'NO') as boete_onder_75
from spelers as s,boetes as b