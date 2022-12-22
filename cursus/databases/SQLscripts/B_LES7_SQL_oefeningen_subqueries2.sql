use database_tennis;

#1 Geef voor alle spelers die geen penningmeester zijn of zijn geweest 
#alle gewonnen wedstrijden, gesorteerd op wedstrijdnummer.

-- select w.spelersnr, w.wedstrijdnr
-- from wedstrijden as w
-- where w.spelersnr not in (select bl.spelersnr from bestuursleden as bl where bl.functie = "penningmeester") 
-- and w.gewonnen = 3

-- select w.spelersnr,w.wedstrijdnr
-- from wedstrijden as w
-- left join (select bl.spelersnr from bestuursleden as  bl where bl.functie = 'penningmeester') 
-- as pen using (spelersnr) 
-- where pen.spelersnr is null and gewonnen = 3
-- order by w.wedstrijdnr


#2 Geef van elke speler het spelersnr, de naam en het verschil tussen zijn of haar jaar van toetreding 
#en het gemiddeld jaar van toetreding van de spelers die in dezelfde plaats wonen. Sorteer op spelersnr. 
#Toon 3 getallen na de komma, zet het verschil om naar het numeric type met precisie van 5 en een schaal van 3.
#Numeric type??????

-- select distinct s.spelersnr, s.naam, format((s.jaartoe - p.gem_jaar_toetreding),3)
-- from spelers as s
-- join (select avg(s.jaartoe) as gem_jaar_toetreding,plaats from spelers as s 
-- group by s.plaats ) as p on s.plaats = p.plaats
-- order by s.spelersnr

#3 Je kan per speler berekenen hoeveel boetes die speler heeft gehad en wat het totaalbedrag per speler is. 
#Pas nu deze query aan zodat per verschillend aantal boetes wordt getoond hoe vaak dit aantal boetes voorkwam.
#Sorteer eerst op de eerste kolom en daarna op de tweede kolom. Ik begrijp de vraag niet??????

-- select distinct a.aantal_boetes as a,count(a.aantal_boetes) as 'count'
-- from( select s.spelersnr,count(b.bedrag) as aantal_boetes, sum(b.bedrag) as tot_bedr_boetes
-- from spelers as s
-- join boetes as b on s.spelersnr = b.spelersnr
-- group by s.spelersnr) as a
-- group by a.aantal_boetes
-- order by a.aantal_boetes

-- (select distinct bedrag, count(b.bedrag) from boetes as b
-- group by bedrag order by count(b.bedrag) ) 

#4 Geef van alle spelers het verschil tussen het jaar van toetreding en het geboortejaar,
# maar geef alleen die spelers waarvan dat verschil groter is dan 20. 
#Sorteer deze gegevens beginnend bij de eerste kolom, eindigend bij de laatste kolom.

-- select s.spelersnr, s.naam,voorletters ,jaartoe - year(geb_datum) as toetredingsleeftijd
-- from spelers as s
-- where jaartoe - year(geb_datum) > 20
-- order by s.spelersnr,s.naam,s.voorletters, toetredingsleeftijd

-- select s.spelersnr,s.naam,s.voorletters,(s.jaartoe-year(s.geb_datum)) as leeftijd_toetreding
-- from spelers as s
-- having leeftijd_toetreding > 20
-- order by s.spelersnr, s.naam,s.voorletters, leeftijd_toetreding

#5 Geef voor elke aanvoerder het spelersnr, de naam en het aantal boetes dat voor hem of haar betaald is 
#en het aantal teams dat hij of zij aanvoert. Aanvoerders zonder boetes mogen niet getoond worden. 
#Sorteer, beginnend bij de eerste kolom, eindigend bij de laatste kolom.

-- select s.spelersnr, s.naam, t.teamnr,a.aantal_teams,b.aantal_boetes
-- from spelers as s
-- join teams as t on t.spelersnr = s.spelersnr
-- join (select b.spelersnr, count(b.betalingsnr) as aantal_boetes 
-- from boetes as b
-- group by b.spelersnr) as b on b.spelersnr = s.spelersnr
-- join (select t.spelersnr,count(t.teamnr) as aantal_teams
-- from teams as t
-- group by t.spelersnr) as a on t.spelersnr = s.spelersnr
-- group by s.spelersnr,t.teamnr
-- order by s.spelersnr, s.naam,t.teamnr

-- select t.spelersnr,s.naam,s.voorletters,aantal_boetes,count(t.teamnr) as aantal_teams 
-- from teams as t
-- left join spelers as s on s.spelersnr = t.spelersnr
-- join (select b.spelersnr, count(b.betalingsnr) as aantal_boetes
-- from boetes as b
-- group by spelersnr) as boet on t.spelersnr = boet.spelersnr
-- group by t.spelersnr
-- order by t.spelersnr,s.naam,s.voorletters,aantal_boetes,aantal_teams


#6 = IDEM als OPGAVE2 Geef van elke speler het spelersnr, de naam en het verschil tussen zijn of haar jaar van toetreding 
#en het gemiddeld jaar van toetreding van de spelers die in dezelfde plaats wonen. 
#Sorteer op spelersnr. Zet het berekende verschil om naar het datatype numeric met precisie 5 en schaal 3. ??????

#7 Geef een lijst van alle spelers (spelersnr en woonplaats) die met minstens twee in dezelfde plaats wonen. 
#Sorteer aflopend op woonplaats, daarna op spelersnr.

-- select s.spelersnr, s.plaats
-- from spelers as s
-- where s.plaats in (select a.plaats
-- from (select s.spelersnr,s.plaats,count(s.plaats) as aantal
-- from spelers as s 
-- group by s.plaats ) as a
-- where a.aantal > 1)
-- order by plaats desc,s.spelersnr

-- select s.spelersnr,s.plaats
-- from spelers as s
-- join (select s.spelersnr,s.plaats
-- from spelers as s
-- group by s.plaats
-- having count(s.plaats) >1) as pl on pl.plaats = s.plaats
-- group by spelersnr
-- order by plaats desc,spelersnr

#8 We willen een statistiek van hoeveel wedstrijden de spelers winnen.
#Geef een lijst met aantal gewonnen wedstrijden en het aantal spelers dat dit aantal wedstrijden gewonnen heeft.
#Dus bv als er vier spelers zijn die elk drie wedstrijden hebben gewonnen, dan is de output: 
#aantal_gewonnen: 3, aantal_spelers: 4. Dit graag voor alle aantallen gewonnen wedstrijden en alle spelers.
#Sorteer op aantal gewonnen wedstrijden.

-- select  agw.aantal_gewonnen,count(agw.aantal_gewonnen) as aantal_spelers
-- from (select w.spelersnr,count(gewonnen) as aantal_gewonnen
-- from wedstrijden as w where w.gewonnen = 3 
-- group by w.spelersnr) as agw
-- group by agw.aantal_gewonnen
-- order by agw.aantal_gewonnen

-- select ag.aantal_gewonnen,count(ag.spelersnr) as aantal_spelers
-- from  (select count(w.wedstrijdnr) as aantal_gewonnen,w.spelersnr
-- 	from wedstrijden as w
-- 	where w.gewonnen = 3
-- 	group by w.spelersnr) as ag
-- group by ag.aantal_gewonnen   
-- order by aantal_gewonnen
#9 Maak een lijst met de spelers( naam van de speler, voorletter en woonplaats die ooit gespeeld hebben
# voor een team dat nu in de tweede divisie speelt en waarvoor geen enkele boete betaald werd 
#voor 1 januari 1981. Geen dubbels, sorteer van voor naar achter

-- select s.naam,s.voorletters,s.plaats
-- from spelers as s
-- group by spelersnr
-- having s.spelersnr not in 
-- ( select b.spelersnr as spelermetboetevoor81 #lijst spelers zonder boete voor 01-01-1981
-- from boetes as b 
-- where b.datum < '1981-01-01' ) 
-- and s.spelersnr in 
-- (select w.spelersnr as speler2dedivisie #lijst van spelers 2de divisie
-- from wedstrijden as w
-- join teams as t using (teamnr)
-- where t.divisie = 'tweede'
-- group by w.spelersnr)
-- order by s.naam,s.voorletters,s.plaats





#10 Toon mij alle aanvoerders hun  spelersnr, naam, voorletters, aantalboetes die hij gekregen heeft 
# en aantalteams waarvoor de speler aanvoerder is.




-- select t.spelersnr,s.naam,s.voorletters,ba.aantal_boetes,ta.aantal_teams
-- from teams as t
-- join spelers as s using (spelersnr)
-- join  (select count(t.teamnr) as aantal_teams 
-- from teams as t
-- group by t.spelersnr) as ta on s.spelersnr = t.spelersnr #hier worden het aanta teams geteld
-- join (select count(b.betalingsnr) as aantal_boetes,b.spelersnr
-- from boetes as b
-- group by b.spelersnr
-- having  b.spelersnr in (select t.spelersnr from teams as t)) as ba on s.spelersnr = ba.spelersnr #hier worden het aantal boetes geteld
-- group by spelersnr
-- order by spelersnr



-- use database_tennis; #spelers as s,bestuursleden as bl,boetes as b,wedstrijden as w, teams as t
-- select t.spelersnr,s.naam,s.voorletters,count(b.betalingsnr) as aantal_boetes,ta.aantal_teams
-- from teams as t
-- join spelers as s using (spelersnr)
-- join boetes as b using (spelersnr)
-- join (select count(t.teamnr) as aantal_teams,t.spelersnr 
-- from teams as t
-- group by t.spelersnr) as ta on ta.spelersnr = t.spelersnr
-- group by spelersnr
-- order by spelersnr





