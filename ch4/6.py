def computepay(hours, rate):
    if hours > 40:
        pay = 40 * rate + (hours - 40) * 1.5 * rate
    else:
        pay = hours * rate

    print(f"Pay: {pay}")


computepay(45, 10)
