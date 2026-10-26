from flask import Flask, request, render_template, session  #import flask to run the web server and 'request' to catch form data sent by the user

app = Flask(__name__) #initialize flask application

app.secret_key = "secret_key 1903" #global lists for budget, expenses and error messages

@app.route("/", methods=["GET", "POST"]) #it tells flask to run this function when visiting the homepage, looking out for both page loads (GET) and form submissions (POST) 
def home():
    if "budget" not in session:
        session["budget"] = 0
    if "expenses" not in session:
        session["expenses"] = []
    if "error_message" not in session:
        session["error_message"] = ""
        


    if request.method == "POST":  #this line runs whenever a user clicks any submit button on the website

        if session["budget"] == 0:
            session["budget"] = int(request.form.get("budget"))
        else:
            item = request.form.get("item").lower()
            cost = int(request.form.get("cost"))
            
            if cost > session["budget"]:
                session["error_message"] = "Budget not enough!!"
            else:
                session["error_message"] = ""
                session["budget"] = session["budget"] - cost

                temp_expenses = session["expenses"]
                temp_expenses.append(f"{item}-{cost}")
                session["expenses"] = temp_expenses

    formatted_history = "<br>".join(session["expenses"])

    if session["budget"] == 0:
        return render_template("setup.html")
    else:
        return render_template("dashboard.html",
                                budget = session["budget"],
                                error_message = session ["error_message"],
                                formatted_history=formatted_history)

if __name__ == "__main__":
    app.run(debug=True)