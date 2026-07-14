import mysql.connector
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pwprachi1!",
        database="FoodOrderingDB"
    
    )
    print("Connected to mysql Successfully!")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Users")

    rows = cursor.fetchall()

    print(rows)
    

except mysql.connector.Error as err:
    print("connection failed:" , err)

from flask import Flask, request
app= Flask(__name__)
users = ["Prachi", "Sandhya" , "Rahul"]
@app.route('/users', methods=['GET'])
def get_users():

    cursor.execute("SELECT * FROM Users")

    users = cursor.fetchall()

    return {"users": users}
@app.route('/users', methods=['POST'])
def add_users():

    data = request.get_json()

    cursor.execute(
        "INSERT INTO Users (Name, City, Phone) VALUES (%s, %s, %s)",
        (data["name"], data["city"], data["phone"])
    )

    connection.commit()

    return {"message": "User added successfully!"}
@app.route('/users' , methods= ['DELETE'])
def delete_users():
    data= request.get_json()
    if data["name"] not in users:
        return{ "error": "user not found"}, 404
    users.remove(data["name"])
    return{ "messgae": "user removed" , "users": users}, 200
@app.route('/users' , methods=['PUT'])
def put_users():
    data= request.get_json()
    index = users.index(data["old_name"])
    users[index] = data["new_name"]
    return{ "message": "user replaced" , "users" : users}
app.run(debug =True)

              


