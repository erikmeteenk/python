use database_tennis;
#1.1 Give an overview of all players (number, name and initials in one column, and year of
#admission). Fig 1.2 doesn’t show the complete list.

-- select s.spelersnr, concat( s.naam, "  ", s.voorletters) as naam, s.jaartoe
-- from spelers as s

#1.2 Limit the overview from the first exercise to only those players that became a member after
#1983.

-- select s.spelersnr, concat( s.naam, "  ", s.voorletters) as naam, s.jaartoe
-- from spelers as s
-- where s.jaartoe > 1983

#1.3 Limit the overview from the first exercise to the players that live in Zoetermeer.

-- select s.spelersnr, concat( s.naam, "  ", s.voorletters) as naam, s.jaartoe
-- from spelers as s
-- where plaats = "zoetermeer"

#1.4 Change the previous query so you only show the players from Zoetermeer who became a
#member of the club before 1984.

-- select s.spelersnr, concat( s.naam, "  ", s.voorletters) as naam, s.jaartoe
-- from spelers as s
-- where s.jaartoe < 1984 and plaats = "zoetermeer"

#1.5 Make a list al all the teams where player number 27 is the captain.

-- select t.teamnr,t.divisie,t.spelersnr
-- from teams as t
-- where t.spelersnr = 27

#1.6 Give an overview of all won tennis matches.

-- select w.wedstrijdnr,w.teamnr,w.spelersnr, w.gewonnen, w.verloren
-- from wedstrijden as w
-- where w.gewonnen = 3

#1.7 Make a list of all matches where player 6 won

-- select w.wedstrijdnr,w.teamnr,w.spelersnr, w.gewonnen, w.verloren
-- from wedstrijden as w
-- where w.gewonnen = 3 and w.spelersnr = 6


#1.8 Give an overview of all matches from player 112 and calculate for each of those matches with
#how many sets he won or lost (fig. 1.9)

-- select w.wedstrijdnr,w.teamnr,w.spelersnr, w.gewonnen, w.verloren, abs(w.gewonnen-w.verloren) as verschil
-- from wedstrijden as w
-- where  w.spelersnr = 112

#1.9 Make a list of all the fines that were paid (fig. 1.10)

-- SELECT * FROM database_tennis.boetes;

#1.10 Include in the list from the previous exercise also the name of the player (name and first
#letter(s) in one column). (The screen shot doesn’t show all the rows)

-- select b.betalingsnr,b.spelersnr,b.datum, b.bedrag, s.naam
-- from boetes as b , spelers as s
-- where b.spelersnr = s.spelersnr
-- #inner join spelers as s using (spelersnr)

#1.11 Find the largest and smallest amount of all the fines.

-- select spelersnr, min(bedrag) as minimum , max(bedrag) as maximum 
-- from boetes

#2.1 Give an overview of all board member who are currently in function. Show their function.
#Give also their names (name and initials in one column).

-- select concat(s.naam,"  ", s.voorletters), bl.functie
-- from bestuursleden as bl,spelers as s
-- where bl.spelersnr = s.spelersnr and bl.EIND_DATUM is null

#2.2 Make a list of all female players that do not live in Leiden.

-- select naam, geslacht, plaats
-- from spelers
-- where geslacht = "v" and plaats <> "leiden"

#2.3 What was the average fine amount paid? How many fines were paid since the club was
#founded?

-- select format(avg(bedrag),0), count(bedrag)
-- from boetes

#2.4 Give an overview of all fines bigger than € 30. Show the amount in eurocent. Also provide
#the number and name of the player who got fined

-- select b.spelersnr,s.naam, round(b.bedrag*100, 0) as bedrag_in_centen
-- from boetes as b, spelers as s
-- where b.spelersnr = s.spelersnr and b.bedrag > 30

#2.5 let’s start from the previous exercise: a list of all the players that got fined more than € 30.
#The difference is: this time we only want a list of players (not a list of fines). A player that is
#more than once on this list (e.g. Cools has a fine of 75 and one of 100) will only appear in
#one row on your overview

-- select b.spelersnr,s.naam #, format(b.bedrag*100, 0) as bedrag
-- from boetes as b, spelers as s
-- where b.spelersnr = s.spelersnr and b.bedrag > 30
-- group by s.spelersnr 

#2.6 Make a list of all matches played by members of team number 2 and where our player won.
#Include the winning player’s number and also the number of the captain of the team

-- select w.teamnr, w.spelersnr, t.spelersnr as captain
-- from wedstrijden as w, teams as t
-- where w.teamnr= t.teamnr and w.teamnr = 2 and w.gewonnen = 3

#2.7 Make a list of all competition players. Not all players in our club play in a competition. But
#those who want to play in official matches, need to be a member of the national tennis
#association (we don’t show the complete output in fig 2.7)

-- select s.spelersnr, concat(s.naam," ", s.voorletters)
-- from spelers as s
-- where s.bondsnr > 0

#2.8 Show the overview in the previous exercise, but only for the female players.

-- select s.spelersnr, concat(s.naam," ", s.voorletters)
-- from spelers as s
-- where s.bondsnr >  0 and geslacht = "v"


#2.9 Show name and initials, team, division for the captains of every team.

-- select s.naam, s.voorletters, t.spelersnr, t.divisie
-- from teams as t, spelers as s
-- where t.spelersnr = s.spelersnr

#2.10 Limit the previous query to the female captains

-- select s.naam, s.voorletters, t.spelersnr, t.divisie
-- from teams as t, spelers as s
-- where t.spelersnr = s.spelersnr and s.geslacht = "v"
