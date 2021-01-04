from dbmanage import database
dbmanage = database()
data = dbmanage.manage.cursor().execute("SELECT " + "*" + " FROM item").fetchall()
print(sorted(data, key = lambda x: x[1]))