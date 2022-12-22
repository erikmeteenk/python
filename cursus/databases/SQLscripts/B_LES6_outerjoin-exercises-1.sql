use database_tennis;

# 1 Geef het spelersnummer, het jaar van toetreden en bondsnummer van alle spelers en de
# teams waarvoor ze kapitein zijn. Ook spelers die geen teamkapitein zijn, moeten getoond
#worden. Sorteer op spelersnr aflopend.

-- select s.spelersnr, s.jaartoe, s.bondsnr, t.teamnr
-- from spelers as s
-- left join teams as t using (spelersnr)
-- order by s.spelersnr desc

# 2 Geef voor alle spelers die bestuurslid zijn (of geweest zijn) een lijst van de wedstrijdnummers
#van alle wedstrijden die ze gespeeld hebben, en het verschil in sets waarmee ze gewonnen
#hebben. Bestuursleden zonder wedstrijd moeten ook in het resultaat voorkomen. Sorteer
#op bestuurslidfunctie (oplopend), verschil (aflopend), spelersnr (oplopend) en wedstrijdnr
#(oplopend)

-- select s.spelersnr,s.naam,bl.functie,w.wedstrijdnr,(w.gewonnen-w.verloren) as verschil
-- from spelers as s
-- join bestuursleden as bl using (spelersnr)
-- left join wedstrijden as w using (spelersnr)
-- where bl.spelersnr = s.spelersnr #and  w.gewonnen = 3
-- group by wedstrijdnr
-- order by bl.functie asc,(w.gewonnen-w.verloren) desc,s.spelersnr asc, w.wedstrijdnr asc



#3 Geef voor alle vrouwelijke spelers die in Den Haag, Zoetermeer of Leiden wonen het spel-
#ersnummer, hun woonplaats en een lijst van de teams waarvoor ze ooit gespeeld hebben.
#Sorteer op spelersnr

-- select s.spelersnr, s.naam, s.plaats, w.teamnr
-- from spelers as s
-- left join wedstrijden as w using (spelersnr)
-- where s.geslacht = "v" and (s.plaats = "leiden" or s.plaats = "zoetermeer" or s.plaats = "den haag")

#4 Geef voor elke mannelijke speler wiens naam minstens 2 keer de letter ’e’ bevat een lijst van
#de functies die hij op dit moment uitoefent. Ook mannelijke spelers zonder huidige functie
#moeten getoond worden. Sorteer op spelersnr

-- select s.spelersnr,s.naam,s.geslacht,best.functie
-- from spelers as s
-- left join (select bl.functie,bl.spelersnr from bestuursleden as bl where bl.eind_datum is null ) as best 
-- 	on s.spelersnr = best.spelersnr
-- where s.geslacht ='m' and s.naam like '%e%e%'
-- order by s.spelersnr




#5 Geef een alfabetisch gesorteerde lijst van de namen van alle leden van de tennisvereniging
#die ofwel een recreatiespeler zijn (speelt geen wedstrijden) ofwel een wedstrijdspeler die nog
#geen wedstrijden gespeeld heeft.

-- select s.naam
-- from spelers as s
-- left join wedstrijden as w  using (spelersnr)
-- where w.spelersnr is null
-- order by s.naam

#6 Geef een aflopend gesorteerde lijst van de nummers van alle spelers waarvoor nog geen boete
#werd betaald en die nog nooit in het bestuur van de tennisvereniging hebben gezeten.

-- select s.spelersnr
-- from spelers as s
-- left join boetes as b  using (spelersnr)
-- left join bestuursleden as bl  using (spelersnr)
-- where b.spelersnr is null and bl.spelersnr is null
-- order by s.spelersnr desc

#7 Geef een lijst van alle spelers die nog geen wedstrijd gespeeld hebben. Sorteer op spelersnr

-- select s.spelersnr, s.naam
-- from spelers as s
-- left join wedstrijden as w using (spelersnr)
-- where w.spelersnr is null 
-- order by s.spelersnr 

#8 Geef alle spelers die geen boete gekregen hebben en niet in Den Haag wonen. Sorteer op
#jaar van toetreden

-- select s.spelersnr, s.naam, s.plaats
-- from spelers as s
-- left join boetes as b  using (spelersnr)
-- where b.spelersnr is null and s.plaats <> "den haag"
-- order by s.jaartoe

#9 Geef per team de verloren wedstrijden. Zorg dat teams zonder verloren wedstrijden ook in
#de output verschijnen. Duid per wedstrijd aan of het om een actief bestuurslid gaat. Sorteer
#op divisie en wedstrijdnummer

-- select w.teamnr,t.divisie,w.wedstrijdnr,w.spelersnr,case
-- 							when w.spelersnr in
-- 									(select spelersnr
-- 									from bestuursleden 
-- 									where eind_datum is null) then 'actief'
-- 							else '  -  '
--                             end as bestuurslid
-- from wedstrijden as w
-- left join teams as t using (teamnr)

-- where w.verloren = 3 
-- order by t.divisie, W.wedstrijdnr

