import mysql.connector


'''
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="longteset",
)

mycursor = mydb.cursor(dictionary=True)

#sql = "SELECT name,hw_name,status,value,id FROM hard_ware"
sql = "SELECT * FROM hard_ware"


mycursor.execute(sql)

data = mycursor.fetchall()

for i in data:
    print(i)
'''
def conDB():
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="longteset",
        ) 
    return mydb

class Con:
    def selectid(ID):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True) 
        sql = "SELECT * FROM hard_ware WHERE id = {}".format(ID)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def getname():
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True) 
        sql = "SELECT name FROM hard_ware"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data
    
    def inserthw(name,hw_name):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True) 
        sql = "INSERT INTO hard_ware(name,hw_name,status,value)VALUES('{}','{}','OFF',0)".format(name,hw_name)
        mycursor.execute(sql)
        mydb.commit()
        ID = mycursor.lastrowid
        mycursor.close()
        mydb.close()
        return ID

    def updatehw(ID,status):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True) 
        sql = "UPDATE hard_ware SET status = '{}' WHERE id = {}".format(status,ID)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True

    def deleteehw():
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True) 
        sql = "DELETE FROM hard_ware WHERE id = 113"
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True

    def selectminhw():
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True) 
        sql = "SELECT * FROM hard_ware WHERE id = (SELECT MIN(id) FROM hard_ware)"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data
        



