from flask import Flask, request, render_template  #import flask to run the web server and 'request' to catch form data sent by the user

app = Flask(__name__) #initialize flask application

budget = 0         #global lists for budget, expenses and error messages
expenses = []
error_message = ""

@app.route("/", methods=["GET", "POST"]) #it tells flask to run this function when visiting the homepage, looking out for both page loads (GET) and form submissions (POST) 
def home():
    global budget, error_message #allows python to modify global variables in the function

    if request.method == "POST":  #this line runs whenever a user clicks any submit button on the website

        if budget == 0:
            budget = int(request.form.get("budget"))
        else:
            item = request.form.get("item").lower()
            cost = int(request.form.get("cost"))
            
            if cost > budget:
                error_message = "Budget not enough!!"
            else:
                error_message = ""
                budget = budget - cost
                expenses.append(f"{item} - {cost}")

    formatted_history = "<br>".join(expenses)

    if budget == 0:
        return render_template("setup.html")
    else:
        return render_template("dashboard.html",
                                budget=budget,
                                error_message=error_message,
                                formatted_history=formatted_history)


if __name__ == "__main__":
    app.run(debug=True)