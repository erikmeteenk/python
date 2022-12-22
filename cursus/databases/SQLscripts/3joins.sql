select wedstrijdnr, naam as name, s.spelersnr as member,t.teamnr,divisie
from spelers as s join wedstrijden as w  on s.spelersnr = w.spelersnr
join teams as t on w.teamnr = t.teamnr