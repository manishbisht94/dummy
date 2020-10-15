import psycopg2
from error_pricing_error import error
# error = [1,2,3,4,5,6,7,8,9,10]

try:
    conn = psycopg2.connect("dbname='compucom' user='odoo' host='localhost' password='aDC0MuZsqXnRceuDcWfQ'")
except:
    print("I am unable to connect to the database")

print("""UPDATE webhook_data SET state = 'error' WHERE id IN {}""".format(tuple(error)))
cur = conn.cursor()
cur.execute("""UPDATE webhook_data SET state = 'error' WHERE id IN {}""".format(tuple(error)))
conn.commit()



