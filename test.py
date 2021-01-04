from dbmanage import database
dbmanage = database()
dbmanage.manage.execute("INSERT INTO item (id,title,authors,date_added,date_published,notes,publisher,sourcedist,tags,path)\nVALUES (?,?,?,?,?,?,?,?,?,?)", (2, "A History of the Perfectly Generic Object, The Cultured Placeholder", "Perfectly Generic Author", "2020-12-31 00:00:00.000", "2020-12-31 00:00:00.000", "", 0, 0, "generic", "/dev/null"))
dbmanage.manage.commit()
dbmanage.close()