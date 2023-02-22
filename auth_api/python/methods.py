from flask import abort
import mysql.connector
import jwt
import hashlib
import hmac

global secret
secret = 'my2w7wjd7yXF64FIADfJxNs1oupTGAuW'

# These functions need to be implemented
class Token:

    def generate_token(self, username, password):
        mydb = mysql.connector.connect(
            host="sre-bootcamp-selection-challenge.cabf3yhjqvmq.us-east-1.rds.amazonaws.com",
            user="secret",
            password="jOdznoyH6swQB9sTGdLUeeSrtejWkcw",
            database="bootcamp_tht"
        )
        
        mycursor = mydb.cursor()
        sql = "SELECT role, salt, password as encrypted FROM users WHERE username= %s"
        
        mycursor.execute(sql, (username, ))
        myresult = mycursor.fetchone()
                        
        mycursor.close()
        mydb.close()
       
        if myresult and myresult[2]==hashlib.sha512(bytes(password+myresult[1], 'utf-8')).hexdigest(): 
            message = { 'role': myresult[0]}
            return jwt.encode(message, secret)     
        else:
            abort(403) 

class Restricted:

    def access_data(self, authorization):
        if jwt.decode(authorization, key=secret, algorithms=['HS256', ])["role"] in ['admin', 'editor']:
            return 'You are under protected data'
        else:
            return 'Restricted'
