use database_tennis;
#gebruik van concat om de isnumeric() faciliteit in Mysql te gebruiken
select s.spelersnr,s.naam,s.classement, case
						when concat('',classement * 1) = classement  then 'hoofdtabel' #concat
                        else 'neventabel'
                        end as tornooitabel
from spelers as s