from flask import Flask, request, render_template, redirect, url_for

comments = []

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("home.html", comments=comments)

@app.route("/comments")
def view_comment():
    return render_template("comments.html", comments=comments)

@app.route("/submit", methods=['POST', 'GET'])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        text_comment = request.form["comment"]
        
        if not name or not email or not text_comment:
            return render_template("home.html", comments=comments)
        
        comments.append({"name" : name, "email" : email, "comment" : text_comment})
        
        
    return render_template("home.html", comments=comments)

    
    

if __name__ == "__main__":
    app.run(debug=True)