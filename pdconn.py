import psycopg2
from flask import Flask, jsonify, request

app=Flask(__name__)
#connection parameters
DB_NAME="newlearndb"
DB_USER="vvs_root"
DB_PASSWORD="your-pass"
DB_HOST="localhost"
DB_PORT="5432"
@app.route('/')
def index():
    return jsonify({"msg": "Welcome to the API!"})
def get_conn():
    conn=psycopg2.connect(dbname=DB_NAME, user=DB_USER, host=DB_HOST, password=DB_PASSWORD)
    return conn
    
@app.route('/create_table',methods=['GET'])
def create_table():
    try:
    	conn=get_conn()
    	cursor=conn.cursor()
    	cursor.execute("""create table if not exists employees(
    	id SERIAL PRIMARY KEY, 
    	name varchar(100),
    	age INT,
    	dept VARCHAR(30)
    	); """)
    	conn.commit()
    	cursor.close()
    	conn.close()
    
    	return jsonify({"msg":'Table created successfully!'}),200
    
    except Exception as e:
    	return jsonify({'error':str(e)}),500
 
@app.route('/insert_data',methods=['POST'])
def insert_data():
    data=request.get_json()
    name=data.get('name')
    age=data.get('age')
    dept=data.get('dept')
    try:
    	conn=get_conn()
    	cursor=conn.cursor()
    	cursor.execute("""
    	insert into employees(name,age,dept)
    	values (%s, %s, %s);
    	""",(name,age,dept))
    	conn.commit()
    	cursor.close()
    	conn.close()
    	return jsonify({'msg':f"data for {name} inserted!"}),201
    except Exception as e:
    	return jsonify({'error':str(e)}),500
 
@app.route('/get_emply',methods=['GET'])
def get_emply():
    try:
    	conn=get_conn()
    	cursor=conn.cursor()
    	cursor.execute("select * from employees")
    	emp=cursor.fetchall()
    	cursor.close()
    	conn.close()
    	return jsonify({'emp':emp}),200
    except Exception as e:
    	return jsonify({'error':str(e)}),500
    	
@app.route('/update_emply/<int:id>',methods=['PUT'])
def update_emply(id):
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    dept = data.get('dept')
    try:
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE employees
        SET name=%s, age=%s, dept=%s
        WHERE id=%s;
        """, (name, age, dept, id))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'msg': f"Employee with id {id} updated!"}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    	
@app.route('/del_emply/<int:id>',methods=['DELETE'])
def del_emply(id):
    try:
    	conn=get_conn()
    	cursor=conn.cursor()
    	cursor.execute("""
    	DELETE from employees
    	where id=%s;""",(id,))
    	conn.commit()
    	cursor.close()
    	conn.close()
    	return jsonify({'msg':f'emp with {id} deleted!'})
    except Exception as e:
        return jsonify({'error':str(e)}),500
        
        
@app.route('/change_port',methods=['POST'])    
def change_port():
    global DB_PORT
    np=request.get_json().get('port')
    if np:
    	DB_PORT=np
    	return jsonify({"msg":f"port changed to {np}"}),200
    else:
    	return jsonify({'error':'no port provided!'}),400	
    	
if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)
    
