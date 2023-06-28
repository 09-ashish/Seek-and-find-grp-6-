from flask import Flask,render_template,request
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="little_tots"
)
mycursor = mydb.cursor()



app=Flask(__name__)
@app.route('/')
def intro():
    return render_template('intro.html')
#if("__main__"==__name__):
#    app.run()

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/submit-signup',methods=['post'])
def submit_signup():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    password = request.form['pass']
    query="INSERT INTO signup (first_name,last_name,email,password) values (%s,%s,%s,%s)"
    data=(fname,lname,email,password)
    mycursor.execute(query,data)
    mydb.commit()
    mycursor.close()
    mydb.close()
    return render_template('login.html')

@app.route('/login')
def login():  
    return render_template('login.html')


@app.route('/submit-login',methods=['GET'])
def signin():
    email=request.args.get('email')
    password=request.args.get('pass')
    query=("select password from signup where email=%s")
    data=[email]
    mycursor.execute(query,data)
    check=mycursor.fetchone()
    if check is not None:
        stored_password = check[0]
        if password == stored_password:
            return render_template('index.html')
        else:
            return render_template('login.html', msg= "invalid password or email")




@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/intro')
def back():
    return render_template('intro.html')

@app.route('/index')
def welcome():
    return render_template('index.html')



if("__main__"==__name__):
    app.run(debug=True)








#change form in html file
#action- eg /submit-signup...... 
#rquest.form
#query=select password from table name where email = %s; 
#data =[email]
