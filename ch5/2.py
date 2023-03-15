min_value = max_value = None

while True:
    n = input('> ')

    if n == "done":
        break
    
    try:
        n = float(n)
    except:
        print("Enter a number!")
        continue

    if not min_value or n < min_value:
        min_value = n

    if not max_value or n > max_value:
        max_value = n

print(f"Max: {max}")
print(f"Min: {min}")
