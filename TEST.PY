from mysql import connector


con=connector.connect(host="localhost", username="root", password="root", database="store")
cur = con.cursor()
cur.execute("SELECT total_product from goods where id=1")
print (list(cur)[0][0])