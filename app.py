from flask import Flask, request  #import flask to run the web server and 'request' to catch form data sent by the user

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
        return f"""<!DOCTYPE html>
        <html>
            <head>
                <title>Set Budget</title>
                <style>
                    body {{
                        margin: 0;
                        padding: 0;
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        background: linear-gradient(135deg, #1f4068, #162447, #1b1b2f);
                        height: 100vh;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                        color: #fff;
                    }}
                    .glass-container {{
                        background: rgba(255, 255, 255, 0.05);
                        backdrop-filter: blur(12px);
                        -webkit-backdrop-filter: blur(12px);
                        border: 1px solid rgba(255, 255, 255, 0.1);
                        border-radius: 16px;
                        padding: 30px;
                        width: 350px;
                        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
                        box-sizing: border-box;
                    }}
                    h1 {{
                        text-align: center;
                        font-size: 24px;
                        margin-bottom: 20px;
                    }}
                    input {{
                        width: 100%;
                        padding: 12px;
                        margin: 10px 0;
                        background: rgba(255, 255, 255, 0.07);
                        border: 1px solid rgba(255, 255, 255, 0.2);
                        border-radius: 8px;
                        color: #fff;
                        font-size: 15px;
                        box-sizing: border-box;
                    }}
                    button {{
                        width: 100%;
                        padding: 12px;
                        margin-top: 10px;
                        background: #00b4d8;
                        border: none;
                        border-radius: 8px;
                        color: #fff;
                        font-weight: bold;
                        font-size: 15px;
                        cursor: pointer;
                    }}
                </style>
            </head>
            <body>
                <div class="glass-container">
                    <h1>Set Your Budget</h1>
                    <form method="POST">
                        <input type="number" name="budget" placeholder="Enter starting budget" required>
                        <button type="submit">Start Tracking</button>
                    </form>
                </div>
            </body>
        </html>"""
    else:
        return f"""<!DOCTYPE html>
        <html>
            <head>
                <title>Expense Tracker Dashboard</title>
                <style>
                    body {{
                        margin: 0;
                        padding: 0;
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        background: linear-gradient(135deg, #1f4068, #162447, #1b1b2f);
                        min-height: 100vh;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                        gap: 100px;
                        color: #fff;
                    }}
                    .glass-container {{
                        background: rgba(255, 255, 255, 0.05);
                        backdrop-filter: blur(12px);
                        -webkit-backdrop-filter: blur(12px);
                        border: 1px solid rgba(255, 255, 255, 0.1);
                        border-radius: 16px;
                        padding: 30px;
                        width: 380px;
                        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
                        box-sizing: border-box;
                    }}
                    h1, h2 {{
                        text-align: center;
                    }}
                    .remaining {{
                        text-align: center;
                        color: #00f0ff;
                        font-weight: bold;
                        margin-bottom: 20px;
                    }}
                    input {{
                        width: 100%;
                        padding: 12px;
                        margin: 10px 0;
                        background: rgba(255, 255, 255, 0.07);
                        border: 1px solid rgba(255, 255, 255, 0.2);
                        border-radius: 8px;
                        color: #fff;
                        font-size: 15px;
                        box-sizing: border-box;
                    }}
                    button {{
                        width: 100%;
                        padding: 12px;
                        margin-top: 10px;
                        background: #00b4d8;
                        border: none;
                        border-radius: 8px;
                        color: #fff;
                        font-weight: bold;
                        font-size: 15px;
                        cursor: pointer;
                    }}
                    .error {{
                        color: #ff6b6b;
                        text-align: center;
                        font-size: 14px;
                        margin-top: 10px;
                    }}
                </style>
            </head>
            <body>
                <div class="glass-container">
                    <h1>Expense Tracker</h1>
                    <div class="remaining">Remaining: {budget}</div>
                    <form method="POST">
                        <input type="text" name="item" placeholder="Expense name" required>
                        <input type="number" name="cost" placeholder="Cost" required>
                        <button type="submit">Add Expense</button>
                    </form>
                    <div class="error">{error_message}</div>
                </div>

                <div class="glass-container">
                    <h3 style="margin-top: 0; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 10px;">EXPENSE HISTORY</h3>
                    <div>{formatted_history}</div>
                </div>
            </body>
        </html>"""

if __name__ == "__main__":
    app.run(debug=True)