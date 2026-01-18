import os  # get passwords
import pandas as pd
from sqlalchemy import create_engine # to connect to sql server/db
from dotenv import load_dotenv

# Load DB info
load_dotenv()

USER = os.getenv("DB_USER")
PASS = os.getenv("DB_PASS")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DB   = os.getenv("DB_NAME")

# Debug print
print(USER)
print(PASS)
print(HOST)
print(PORT)
print(DB)

table_name = 'planet_osm_line'

# 1. Create the connection engine
conn_str = f"postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}"
engine = create_engine(conn_str)

print("Connecting to the database...")

# 2. Use Pandas to read the table
try:
    query = f"SELECT osm_id, name FROM {table_name} WHERE name IS NOT NULL LIMIT 100"
    df = pd.read_sql(query, engine)

    print(f"Success! Pulled {len(df)} rows from {table_name}.")
    
    # 3. Peek at the data
    print("\nHere is a preview of the data:")
    print(df.head()) # Shows the first 5 rows

except Exception as e:
    print(f"An error occurred: {e}")





