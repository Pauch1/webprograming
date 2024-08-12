airline = {
'cebu pacific': 30,
'emirates': 20,
'jet blue': 27
}
x = "EMirates".lower()
print(airline.get(x, 'None'))