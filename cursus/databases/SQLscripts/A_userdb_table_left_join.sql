SELECT kleinkinderen.naam, kleinkinderen.voornaam, juf FROM userdb.kleinkinderen

left JOIN userdb.kinderenklas3 ON kinderenklas3.voornaam = kleinkinderen.voornaam
#neemt alle kleinkinderen 

order by naam