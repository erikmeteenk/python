select s.SPELERSNR, naam, wedstrijdnr
from spelers as s, wedstrijden as w
where s.SPELERSNR = w.spelersnr
