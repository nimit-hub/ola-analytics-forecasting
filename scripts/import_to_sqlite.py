import pandas as pd
import sqlite3

csv_path = r"C:\Users\Nimit\OneDrive\Desktop\Ola Project\data\ncr_ride_bookings.csv  "
db_path = r"C:\Users\Nimit\OneDrive\Desktop\Ola Project\db\ola_analytics.db"

df = pd.read_csv(csv_path)

conn = sqlite3.connect(db_path)

df.to_sql(
    name="raw_data",
    con=conn,
    if_exists="replace",
    index=False,
    chunksize=10000
)

conn.close()

print("Import completed.")
