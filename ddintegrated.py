# import psql adapter + gui
import psycopg2

# connect to database
conn = psycopg2.connect("dbname=test user=postgres")

# open cursor to perform database operations
cur = conn.cursor()

# form the query
query = f"SELECT *" \
        f"FROM {option1_value} AS o1 JOIN {option2_value} o2 ON class_code" \
        f"WHERE "

# Execute a query
cur.execute("QUERY")

# Retrieve query results
records = cur.fetchall()

