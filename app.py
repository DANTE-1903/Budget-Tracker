from flask import Flask, request

app = Flask(__name__)

budget = None

expenses = []

error_message = ""


@app.route("/", methods=["GET", "POST"])
def home():
    global budget,error_message


    if request.method == "POST":
        item = request.form.get("item").lower()
        cost = int(request.form.get("cost"))
        if cost > budget:
            error_message = "Budget not enough!!"
        else:
            error_message = ""
            budget = budget - cost
            expenses.append(f"{item} - {cost}")

    formatted_history = "<br>".join(expenses)


    return f"""<!DOCTYPE html>
<html>
<head>
    <title>Expense Tracker</title>
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
            gap: 100px;
            color: #fff;
        }}
        .glass-container {{
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 20px;
            padding: 30px;
            width: 380px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            margin-bottom: 20px;
        }}
        h1 {{
            margin-top: 0;
            font-size: 22px;
            text-align: center;
            letter-spacing: 1px;
        }}
        h2 {{
            color: #00f2fe;
            text-align: center;
            font-size: 20px;
            margin-bottom: 25px;
        }}
        input {{
            width: 100%;
            padding: 12px;
            margin: 8px 0;
            background: rgba(255, 255, 255, 0.07);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 8px;
            color: #fff;
            font-size: 15px;
            box-sizing: border-box;
        }}
        input::placeholder {{
            color: rgba(255, 255, 255, 0.4);
        }}
        input:focus {{
            outline: none;
            border-color: #00f2fe;
            background: rgba(255, 255, 255, 0.12);
        }}
        button {{
            width: 100%;
            padding: 12px;
            background: linear-gradient(135deg, #00c6ff, #0072ff);
            border: none;
            border-radius: 8px;
            color: white;
            font-size: 15px;
            font-weight: bold;
            cursor: pointer;
            margin-top: 15px;
            transition: opacity 0.2s;
        }}
        button:hover {{
            opacity: 0.9;
        }}
        h3 {{
            font-size: 16px;
            margin-top: 20px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            padding-bottom: 5px;
        }}
        p {{
            color: rgba(255, 255, 255, 0.8);
            font-size: 14px;
            word-break: break-all;
        }}
    </style>
</head>
<body>

    <div class="glass-container">
        <h1>Expense Tracker</h1>
        <h2>Remaining: {budget}</h2>

        <p style="color: #ff4d4d; font-weight: bold; text-align: center;">{error_message}</p>
        
        <form method="POST">
            <input type="text" name="item" placeholder="Expense name" required>
            <input type="number" name="cost" placeholder="Cost" required>
            <button type="submit">Add Expense</button>
        </form>
    </div>

    <div class="glass-container">
        <h3>EXPENSE HISTORY</h3>
        <p>{formatted_history}</p>     
    </div>
</body>
</html>"""
if __name__ == "__main__":
    app.run(debug=True)


