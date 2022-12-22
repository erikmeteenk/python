use database_tennis;
#gebruik van regexp om de isnumeric() faciliteit in Mysql te gebruiken
select s.spelersnr,s.naam,s.classement, case
						when classement REGEXP '^[0-9]+$'  then 'hoofdtabel' #REGEXP '^[0-9]+$'
                        else 'neventabel'
                        end as tornooitabel
from spelers as s