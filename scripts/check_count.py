import sqlite3

conn = sqlite3.connect(r"C:\Users\Nimit\OneDrive\Desktop\Ola Project\db\ola_analytics.db")
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM raw_data")
print(cur.fetchone())
conn.close()
