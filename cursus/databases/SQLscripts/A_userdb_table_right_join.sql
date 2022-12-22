SELECT kleinkinderen.naam, kleinkinderen.voornaam, juf FROM userdb.kleinkinderen

right JOIN userdb.kinderenklas3 ON kinderenklas3.voornaam = kleinkinderen.voornaam
#neemt alle kinderen die in klas3 zitten 

order by naam