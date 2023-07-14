import pymysql

dataBase = pymysql.connect(
	host = "localhost" ,
	user = "root" ,
	password = "123456789" ,
	)

cursorObject = dataBase.cursor()

create_database_query = "CREATE DATABASE IF NOT EXISTS djangocrm"
cursorObject.execute(create_database_query)

use_database_query = "USE djangocrm"
cursorObject.execute(use_database_query)


dataBase.commit()
cursorObject.close()
dataBase.close()

print("All done !!")
