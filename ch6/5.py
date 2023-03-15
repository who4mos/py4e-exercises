STR = 'X-DSPAM-Confidence:0.8475'

colon = STR.find(':')

value = STR[colon+1:]
value = float(value)

print(value)
