count = 0
total = 0

while True:
    n = input('> ')

    if n == "done":
        break
        
    try:
        n = float(n)
    except:
        print('Enter a number!')
        continue

    count += 1
    total += n

print(f"You've entered {count} numbers")
print(f"The sum of these numbers is {total}")
print(f"And their average is {total/count}")
