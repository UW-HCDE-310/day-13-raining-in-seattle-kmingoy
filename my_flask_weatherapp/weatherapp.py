from flask import Flask
import urllib.request

app = Flask(__name__)

def is_it_raining_in_seattle():
    url = 'https://depts.washington.edu/ledlab/teaching/is-it-raining-in-seattle/'
    with urllib.request.urlopen(url) as response:
        is_it_raining = response.read().decode()

    return is_it_raining == "true"

@app.route('/')
def home():
    # Check if it's raining and set the result
    result = "Yes" if is_it_raining_in_seattle() else "No"
    return result

if __name__ == '__main__':
    app.run(debug=True)

