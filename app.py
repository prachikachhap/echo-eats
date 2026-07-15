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

@app.route("/menu" , methods= ['GET'])
def get_menu():
    cursor.execute("SELECT * FROM Menu")
    menu = cursor.fetchall()
    return {"menu": menu}

@app.route("/menu" , methods= ['POST'])
def add_menu():
    data= request.get_json()
    cursor.execute(
        """
        INSERT INTO Menu (Itemname , Price , Category )
        VALUES(%s,%s,%s)

       """,
       (data["itemname"],
        data["price"],
        data["category"]
        )
    )
    connection.commit()
    return {"message": "Menu item added successfully!"}

@app.route('/menu', methods=['DELETE'])
def delete_menu():

    data = request.get_json()

    cursor.execute(
        """
        DELETE FROM Menu
        WHERE ItemID = %s
        """,
        (data["id"],)
    )

    if cursor.rowcount == 0:
        return {"error": "Menu item not found"}, 404

    connection.commit()

    return {"message": "Menu item deleted successfully"}

@app.route('/menu', methods=['PUT'])
def put_menu():

    data = request.get_json()

    cursor.execute(
        """
        UPDATE Menu
        SET ItemName=%s, Price=%s, Category=%s
        WHERE ItemID=%s
        """,
        (
            data["itemname"],
            data["price"],
            data["category"],
            data["id"]
        )
    )

    if cursor.rowcount == 0:
        return {"error": "Menu item not found"}, 404

    connection.commit()

    return {"message": "Menu item updated successfully"}

app.run(debug =True)

              


