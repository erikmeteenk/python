select s.SPELERSNR, naam, bedrag

from spelers as s join boetes as b on (s.SPELERSNR=b.spelersnr)

