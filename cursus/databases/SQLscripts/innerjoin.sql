SELECT naam, VOORLETTERS,spelers.spelersnr, begin_datum , functie FROM database_tennis.bestuursleden

INNER JOIN database_tennis.spelers ON spelers.spelersnr = bestuursleden.spelersnr 

group by naam

#order by naam