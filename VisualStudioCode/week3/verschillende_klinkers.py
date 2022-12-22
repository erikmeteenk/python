# https://dodona.ugent.be/nl/courses/1721/series/18978/activities/1014821966
x=input("voer een regel tekst in:")
cnt=0
if "a" in x or "A" in x:
    cnt +=1
if "e" in x or "E" in x:
    cnt +=1
if "i" in x or "I" in x:
    cnt +=1
if "o" in x or "O" in x:
    cnt +=1
if "u" in x or "U" in x:
    cnt +=1
if cnt > 1:
    print("The sentence contains",cnt,"different vowels.")
if cnt < 1:
    print("The sentence contains no vowels.")
if cnt == 1:
    print("The sentence contains only 1 different vowel.")