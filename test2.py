from dbmanage import database
dbmanage = database()
data = dbmanage.manage.cursor().execute("SELECT " + "title" + " FROM item").fetchall()
print(data)