# Author: Eric Fahy
# Date Created: 5/4/2022
# Date Last Modified: 5/4/2022
import psycopg2
import os

conn = psycopg2.connect(user=os.environ['USER'],
                        password=os.environ['PASSWORD'],
                        host=os.environ['HOST'],
                        port=os.environ['PORT'],
                        database=os.environ['DBNAME'])
print("Database Connected....")
cur = conn.cursor()

# cur.execute("DROP TABLE Test;")
# conn.commit()

print("Please enter an option")
print("1. View Table (Not implemented)")
print("2. Add Expense (Not implemented)")
print("3. Change Value (Not implemented)")
print("4. Delete Expense (Not implemented)")

#print(os.environ['DBNAME'])

#print(type(os.environ['DBNAME']))

# option = input()
