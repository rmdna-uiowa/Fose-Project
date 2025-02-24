from flask import Flask, jsonify, request
from models import mysql

app = Flask(__name__)

# just an example but tbh idk
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (data['name'], data['email']))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'User added successfully!'}), 201

if __name__ == '__main__':
    app.run(debug=True)