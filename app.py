from flask import Flask,render_template, url_for

app = Flask (__name__)

#@app.route('/')
#def main ():
    #return render_template ('main.html')

@app.route ('/about')
def about ():
    return render_template ('about.html')

@app.route ('/contact')
def contact ():
    return render_template ('contact.html')

@app.route ('/services')
def services ():
    return render_template ('services.html')

@app.route ('/')
def index ():
    return render_template ('index.html')

@app.route ('/tutorpage')
def tutorpage ():
    return render_template ('tutorpage.html')

@app.route ('/login')
def login ():
    return render_template ('login.html')

@app.route ('/signin')
def signin ():
    return render_template ('signin.html')

@app.route ('/tutee')
def tutee ():
    return render_template ('tutee.html')

if __name__ == '__main__':
    app.run(debug=True)