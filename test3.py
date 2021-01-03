from dbmanage import database
dbmanage = database()
data = dbmanage.manage.cursor().execute("SELECT " + "*" + " FROM item").fetchall()
print(data)