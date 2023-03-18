import datetime

print(datetime.datetime.now().strftime('%H:%M:%S'))

hora_actual = datetime.datetime.now()
print(hora_actual.hour)

hora_casa = datetime.time(19, 00)
if hora_actual.hour >= hora_casa.hour:
    print("Hora de irse a casa")
else:
    print("A currar")