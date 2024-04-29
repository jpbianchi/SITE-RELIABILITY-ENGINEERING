from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'happy' 


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == password == 'admin':
            session['username'] = username
            return redirect('/products')
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html', error=None)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')


@app.route('/products')
def products():
    if 'username' in session:
        return render_template('products.html', username=session['username'])
    else:
        return redirect('/')

    
@app.route('/purchase', methods=['GET'])
def purchase():
    try:
        # Retrieve the username from the session
        username = session.get('username')
        if username:
            print('Processing payment for user:', username)
            # Render the purchase.html template with the username
            return render_template('purchase.html', username=username)
        else:
            return "Invalid request: Missing 'username' in session data", 400
    except Exception as e:
        print('Error processing payment:', str(e))
        return "An error occurred while processing the payment", 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


