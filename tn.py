import mysql.connector


def conDB():
    mydb = mysql.connector.connect(
        host="localhost",
        user="api",
        password="12345",
        database="api"
    )
    return mydb

class Con:
    def gettn():
        mydb = mysql.connector.connect(
            host="localhost",
            user="api",
            password="12345",
            database="api"
        )
        mycursor = mydb.cursor()
        sql = "SELECT * FROM tn"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def getTnid():
        mydb = mysql.connector.connect(
            host="localhost",
            user="api",
            password="12345",
            database="api"
        )
        mycursor = mydb.cursor()
        sql = "SELECT * FROM tn WHERE id =(SELECT MIN(id) FROM tn)"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def getbyid(id):
        mydb = conDB()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM tn WHERE id = {}".format(id)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def insert_tn(name,hardware):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "INSERT INTO tn (name,hardware,status,value) VALUES ('{}','{}','off',0)".format(name,hardware)
        mycursor.execute(sql)
        mydb.commit()
        ID = mycursor.lastrowid
        mycursor.close()
        mydb.close()
        return ID
    
    def update_tn(id,status):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE tn SET status = '{}' WHERE id = {}".format(status,id)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return sql

        
    def delete_tn(name):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "DELETE FROM tn WHERE name = '{}'".format(name)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True
    
    def select_tn(id):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM tn WHERE id = {}".format(id)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data



