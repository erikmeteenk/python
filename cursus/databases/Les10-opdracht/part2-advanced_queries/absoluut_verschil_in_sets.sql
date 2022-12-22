use database_tennis;
select s.naam, w.wedstrijdnr, abs(w.gewonnen-w.verloren) as verschil_in_sets
from wedstrijden as w
join spelers as s using (spelersnr)