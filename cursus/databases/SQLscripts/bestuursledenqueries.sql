#Actieve bestuursleden
-- (select bl.spelersnr 
-- from bestuursleden as bl
-- where bl.eind_datum is null)

#case bestuursleden
-- select bl.spelersnr,case
-- 			when bl.eind_datum is null then 'actief'
--             else '-'
--             end as bestuurslid
-- from bestuursleden as bl

# count (distinct,field)
-- select count( distinct w.spelersnr) as aantal_spelers_dat_wedstrijden_speelt
-- from wedstrijden as w

-- -gebruik zo nodig if in de select clause
-- -on of using niet vergeten
-- -niet vergeten te sorteren
-- -sum,count,avg enzovoort werken niet in where clause ==> having (opgepast eerst group by!)
-- -volledige left join (alleen A)  met Bkey "is null" in where clause



