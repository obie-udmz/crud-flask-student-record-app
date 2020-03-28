from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL



app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)



@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM record")
    data = cur.fetchall()
    cur.close()




    return render_template('index2.html', record=data )



@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        student_id = request.form['student_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['dob']
        amount_due = request.form['amount_due']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO record (student_id, first_name, last_name, dob, amount_due) VALUES (%s, %s, %s, %s, %s)", (student_id, first_name, last_name, dob, amount_due))
        mysql.connection.commit()
        return redirect(url_for('Index'))




@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM record WHERE student_id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))





@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['student_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['dob']
        amount_due = request.form['amount_due']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE record
               SET first_name=%s, last_name=%s, dob=%s, amount_due=%s
               WHERE student_id=%s
            """, (first_name, last_name, dob, amount_due, id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))









if __name__ == "__main__":
    app.run(debug=True)
