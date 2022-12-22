
def enrollment_stats(list_of_universities):
    # Variables
    total_students = []
    total_tuition = []
    
    # Iterate through lists, adding values
    for i in range(len(list_of_universities)):
                
        total_students.append (list_of_universities[i][1])
        total_tuition.append (list_of_universities[i][2])
  
    # Return variables
    return total_students, total_tuition

def mean(values):
    
    #Return the mean value in the list `values`
    sum = 0
    for i in values:
        sum +=i
    gemiddelde = (sum/len(values))
    return gemiddelde
    



def median(values):
    #Return the median value of the list `values`
    if len(values)%2 != 0:
        mediaanpos = int(len(values)/2) +1
        mediaan = values[mediaanpos]    
    else:
        mediaanpos = int(len(values)/2)
        med1 = values[mediaanpos]
        med2 = values[mediaanpos+1] 
        mediaan = (med1 + med2)//2
    return mediaan



    
universities = [
    ["California Institute of Technology", 2175, 37704],
    ["Harvard", 19627, 39849],
    ["Massachusetts Institute of Technology", 10566, 40732],
    ["Princeton", 7802, 37000],
    ["Rice", 5879, 35551],
    ["Stanford", 19535, 40569],
    ["Yale", 11701, 40500],
]


totals = enrollment_stats(universities)

print("\n")
print("*****" * 6)
print(f"Total students:   {sum(totals[0]):<,.2f}")
print(f"Total tuition: $ {sum(totals[1]):<,.2f}")
print(f"\nStudent mean:     {mean(totals[0]):,.2f}")
print(f"Student median:   {median(totals[0]):,}")
print(f"\nTuition mean:   $ {mean(totals[1]):,.2f}")
print(f"Tuition median: $ {median(totals[1]):,}")
print("*****" * 6)
print("\n")
