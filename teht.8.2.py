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

maakoodi = input("Kirjoita maakoodi")

sql = "select type, count (*) from airport where iso_country = '" + maakoodi + "' group by type"

kursori = yhteys.cursor()
kursori.execute(sql)

tulos = kursori.fetchall()
for rivi in tulos:
    print(f"{rivi[0]}, {rivi[1]}")