x=int(input("voer aantal flesjes in:"))
for i in range (x,0,-1):
    if i==2:
        break
    print(f"{i} flesjes met bier op de muur, {i} flesjes met bier.")
    print(f"Open er een, drink hem meteen, {i-1} flesjes met bier op de muur.")
print("2 flesjes met bier op de muur, 2 flesjes met bier.")
print("Open er een, drink hem meteen, 1 flesje met bier op de muur.")
print("1 flesje met bier op de muur, 1 flesje met bier.")
print("Open er een, drink hem meteen, 0 flesjes met bier op de muur.")