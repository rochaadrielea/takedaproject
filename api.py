from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Utility function to fetch data from the database
def query_db(query):
    conn = sqlite3.connect("manufacturing.db")
    result = conn.execute(query).fetchall()
    conn.close()
    return result

# Endpoint to retrieve all data
@app.route("/data", methods=["GET"])
def get_data():
    query = "SELECT * FROM manufacturing_data"
    rows = query_db(query)
    return jsonify([dict(zip(["Process_ID", "Step", "Duration", "Defect_Rate", "Production_Yield", "Recommendation"], row)) for row in rows])

# Endpoint to retrieve recommendations
@app.route("/recommendations", methods=["GET"])
def get_recommendations():
    query = "SELECT Process_ID, Recommendation FROM manufacturing_data"
    rows = query_db(query)
    return jsonify([{"Process_ID": row[0], "Recommendation": row[1]} for row in rows])

if __name__ == "__main__":
    app.run(debug=True)
