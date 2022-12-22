use database_tennis;
-- #selecteer alle elementen(spelers) van A
-- select A.spelersnr,A.naam
-- from spelers as A

-- #selecteer alleen elementen(spelers) van A die ook voorkomen in B(bestuursleden) = doorsnede
-- select A.spelersnr,A.naam
-- from spelers as A
-- inner join bestuursleden as B on A.spelersnr = B.spelersnr
-- group by A.spelersnr

-- #selecteer alle elementen(spelers) van A + de elementen van B(bestuursleden) 
-- #met een spelersnr dat in A voorkomt A + doorsnede A/B
-- select A.spelersnr,A.naam
-- from spelers as A
-- left join bestuursleden as B on A.spelersnr = B.spelersnr 
-- group by A.spelersnr

-- #selecteer alle elementen(spelers) van A + uitgezonderd de elementen die in B(bestuursleden) 
-- #voorkomen A - doornede A/B (dus alle spelers in A die niet in B zitten)
-- select A.spelersnr,A.naam
-- from spelers as A
-- left join bestuursleden as B on A.spelersnr = B.spelersnr
-- where B.spelersnr is null
-- group by A.spelersnr


-- #selecteer alle elementen(spelers) van A + alle elementen die in B(bestuursleden)
-- #voorkomen full outer join
-- select A.spelersnr,A.naam
-- from spelers as A
-- left join bestuursleden as B on A.spelersnr = B.spelersnr
-- union #all
-- select A.spelersnr,A.naam
-- from spelers as A
-- right join bestuursleden as B on A.spelersnr = B.spelersnr
-- #group by A.spelersnr
