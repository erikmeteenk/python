select FROM_UNIXTIME(dateTime,'%d-%m-%Y') as date, format((min -32)*5/9,1) as minimum, format((max-32)*5/9,1) as maximum from archive_day_outtemp

