from flask import Flask,render_template,request
import pickle


app = Flask(__name__)

model = pickle.load(open("possum.pkl","rb"))

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/possum" , methods = ["GET","POST"])
def possum():
    case = int(request.form.get("case"))
    site = int(request.form.get("site"))
    Pop = int(request.form.get("Pop"))
    age = float(request.form.get("age"))
    skullw = float(request.form.get("skullw"))
    taill = float(request.form.get("taill"))
    footlgth = float(request.form.get("footlgth"))
    earconch = float(request.form.get("earconch"))
    eye = float(request.form.get("eye"))
    belly = float(request.form.get("belly"))

    result = model.predict([[case,site,Pop,age,skullw,taill,footlgth,earconch,eye,belly]])
    outcome = result[0]
    if outcome == 1:
        return "posssum is fuck"
    else:
        return "possum is non fcuk"




if __name__=="__main__":
    app.run(debug=True,port=8080,host="0.0.0.0")
