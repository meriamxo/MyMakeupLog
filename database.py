

import sqlite3
import csv

conn = sqlite3.connect("makeup.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS makeup_log (
    Date TEXT,
    MakeupType TEXT,
    TimeSpentMinutes INTEGER,
    ProductsUsed INTEGER,
    Occasion TEXT,
    SatisfactionRating INTEGER
)
""")

cursor.execute("DELETE FROM makeup_log")

with open("data/makeup_log.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cursor.execute("""
        INSERT INTO makeup_log VALUES (?, ?, ?, ?, ?, ?)
        """, (
            row["Date"].strip(),
            row["MakeupType"].strip(),
            int(row["TimeSpentMinutes"]),
            int(row["ProductsUsed"]),
            row["Occasion"].strip(),
            int(row["SatisfactionRating"])
        ))

conn.commit()

cursor.execute("SELECT COUNT(*) FROM makeup_log")
print("Total makeup records:", cursor.fetchone()[0])


cursor.execute("SELECT * FROM makeup_log")

for row in cursor.fetchall():
    print(row)

conn.close()

print("Makeup data added successfully")
