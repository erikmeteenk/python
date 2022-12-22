SELECT kleinkinderen.naam, kleinkinderen.voornaam, juf FROM userdb.kleinkinderen

JOIN userdb.kinderenklas3 ON kinderenklas3.voornaam = kleinkinderen.voornaam
#neemt alle kinderen die in "kleinkinderen" zitten en die ook in "kinderenklas3" zitten

order by naam