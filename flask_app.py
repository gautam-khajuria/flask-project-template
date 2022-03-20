from flask import Flask, escape, render_template, request

app = Flask(__name__)

purchase_server_working = True
website_title = "EGrocery"

@app.route('/server-status')
def get_server_status():
    pur_ser_str = "ERROR RETRIEVING STATUS"

    if purchase_server_working == True:
        pur_ser_str = "OK"
    else:
        pur_ser_str = "DOWN"

    return f"""
    <h1>Server Status</h1>
    <h4>Website Server: OK</h4>
    <h4>Purchase Server: {pur_ser_str}</h4>"""

@app.route('/')
def home():
    return render_template('index.html', title=website_title, pur_ser=purchase_server_working)

@app.route('/order', methods=['POST', 'GET'])
def order():
    if request.method == 'POST':
        form_data = request.form
        name = escape(form_data['name'])
        order = escape(form_data['order'])

        return render_template('order.html', name=name, order=order, valid=True)

    return render_template('order.html', valid=False)




