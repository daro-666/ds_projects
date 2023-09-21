from flask import Flask
from utils import nmf_predict, nmf_preds_to_list ,user_val_str_to_flt
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommender')
def recommender():
    user_str = dict(request.args)
    user_flt = user_val_str_to_flt(user_str)
    output = nmf_predict(user_flt)
    output_list = nmf_preds_to_list(output)
    return render_template('recommendations.html', movies=output_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
