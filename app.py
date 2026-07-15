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
@app.route('/users', methods=['DELETE'])
def delete_users():

    data = request.get_json()

    cursor.execute(
        """
        DELETE FROM Users
        WHERE UserID = %s
        """,
        (data["id"],)
    )
    if cursor.rowcount == 0:
      return {"error": "User not found"}, 404

    connection.commit()

    return {"message": "User deleted successfully"}
@app.route('/users' , methods=['PUT'])
def put_users():
    data= request.get_json()
    cursor.execute(
    """
    UPDATE Users
    SET Name=%s, City=%s, Phone=%s
    WHERE UserID=%s
    """,
    (
        data["name"],
        data["city"],
        data["phone"],
        data["id"]
    )
)


    connection.commit()
    return {"message": "User updated successfully"}
app.run(debug =True)

              


