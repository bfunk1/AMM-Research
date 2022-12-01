from flask import *
import eth_simulation
import univ2

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template('index.html')
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
    app.config['DEBUG'] = True