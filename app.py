from flask import Flask, jsonify, request
import psycopg2  
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

def db_connection():
    return psycopg2.connect(
        dbname="TRANSITOPS", 
        user="postgres",       
        password="240307", 
        host="localhost",
        port="5432",  
        cursor_factory=RealDictCursor                    
    )

@app.route('/')
def home():
    return "TransitOps Running..."

@app.route('/dashboard')
def dashboard():
    return jsonify({"active_vehicles": 53, "ongoing_trips": 12, "alerts": 3})

# --- YOUR WORK: VEHICLE REGISTRATION ---
@app.route('/api/vehicles', methods=['POST'])
def add_vehicle():
    data = request.json  # This grabs the data sent by the frontend
    
    try:
        conn = db_connection()
        cur = conn.cursor()
        
        # This inserts the data directly into the database team's table
        # NOTE: Make sure 'vehicles', 'plate_number', 'model', and 'year' match their exact column names!
        cur.execute(
            "INSERT INTO vehicles (plate_number, model, year) VALUES (%s, %s, %s) RETURNING id;",
            (data['plate_number'], data['model'], data['year'])
        )
        
        new_id = cur.fetchone()['id']
        conn.commit() # Saves the changes to the database
        
        cur.close()
        conn.close()
        
        return jsonify({"status": "success", "vehicle_id": new_id, "message": "Vehicle registered in DB!"}), 201
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=8080)

