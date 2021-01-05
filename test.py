from dbmanage import database
dbmanage = database()
dbmanage.manage.execute("INSERT INTO item (id,title,authors,date_added,date_published,notes,publisher,sourcedist,tags,path)\nVALUES (?,?,?,?,?,?,?,?,?,?)", (0, "Perfectly Generic Document, The Cultured Placeholder", "Perfectly Generic Author", "2021-12-31 00:00:00.000", "2020-12-31 00:00:00.000", "", 291, 432, "generic", "/dev/null"))
dbmanage.manage.commit()
dbmanage.close()