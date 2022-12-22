select betalingsnr,s.spelersnr,naam as spelersnaam, bedrag,case 
						when bedrag between 0 and 40 then 'low' 
                        when bedrag between 40 and  80 then 'med' 
                        else 'high' 
                        end as categorie
from spelers as s join boetes as b on s.spelersnr = b.spelersnr 