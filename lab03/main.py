MillieSeconds = 10000123
hours = int(MillieSeconds / 3600000)
MillieSecondsLeft = MillieSeconds % 3600000
minutes = int(MillieSecondsLeft / 60000)
SecondsLeft = MillieSeconds % 60000
seconds = int(SecondsLeft % 1000)
MillieSeconds = int(MillieSecondsLeft % 1000)


print("Lab03, 80 point version")
print("Starting MillieSeconds: ", MillieSeconds)
print("Hours: ", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)
print("MillieSecond:", MillieSeconds)