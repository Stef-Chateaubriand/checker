from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__) 



   # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def primeiro():
    return render_template('index.html', rows=int(8), columns=int(8), color1 = "pink", color2 = "black")

@app.route('/<int:x>')#esse e o primeiro que foi feito, pra gente conseguir entender 
def home2(x):
    return render_template('index.html', rows = int(x), columns=int(8), color1 = "pink", color2 = "black")


@app.route('/<int:x>/<int:y>')
def home3(x, y):
    return render_template('index.html', rows = int(x), columns=int(y), color1 = "pink", color2 = "black")


@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def home4(x,y,color1,color2):
    return render_template('index.html', rows = int(x), columns=int(y),color1 = color1, color2 = color2)

    
    
   
if __name__=="__main__":      
    app.run(debug=True)