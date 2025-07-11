import mysql.connector

# Connect to server
cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="thomas",
    password="Th0M4s!",
    database="db_spesa")

nome_utente = input("inserisci nome utente:")

# Get a cursor
cur = cnx.cursor()

cnx.autocommit = True

# Execute a query
cur.execute("INSERT INTO utenti(nome) VALUES (%s);", [nome_utente])

for row in cur:
    print(f"{row}")

# Close connection
cnx.close()