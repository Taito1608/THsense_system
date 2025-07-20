from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def display_csvdata():
    print("Hello! (to Terminal)")
    
    return render_template("index.html") 

# Flaskアプリケーションを起動
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)