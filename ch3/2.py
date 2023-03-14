try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except:
    print("Error, please enter numeric input")
    quit()
    

if hours > 40:
    pay = 40 * rate + (hours - 40) * 1.5 * rate
else:
    pay = hours * rate

print("Pay:", pay)
