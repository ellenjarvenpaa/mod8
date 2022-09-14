import mysql.connector

# yhetyden avaus
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='ellenonerva',
         autocommit=True
         )

icao = input("Kirjoita ICAO koodi")
sql = "select name, municipality from airport where ident = '" + icao + "'"

# suoritetaan kysely
kursori = yhteys.cursor()
kursori.execute(sql)

# haetaan ja käsitellään tulosrivit
tulos = kursori.fetchall()
for rivi in tulos:
    print(f"{rivi[0]}, {rivi[1]}")