# importing the necessary dependencies
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import pickle

app = Flask(__name__)  # initializing a flask app


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])  # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            rate_marriage = float(request.form['rate_marriage'])
            age = float(request.form['age'])
            yrs_married = float(request.form['yrs_married'])
            children = float(request.form['children'])
            religious = float(request.form['religious'])
            educ = float(request.form['educ'])
            occupation = str(request.form['occupation'])
            occupation_husb = str(request.form['occupation_husb'])
            filename = 'finalized_model.pickle'
            loaded_model = pickle.load(open(filename, 'rb'))  # loading the model file from the storage
            # predictions using the loaded model file
            prediction = loaded_model.predict(
                [[1, int(occupation[0]), int(occupation[1]), int(occupation[2]), int(occupation[3]), int(occupation[4]),
                  int(occupation_husb[0]), int(occupation_husb[1]), int(occupation_husb[2]),
                  int(occupation_husb[3]), int(occupation_husb[4]),
                  rate_marriage, age, yrs_married, children, religious, educ]])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html', prediction=prediction[0])
        except Exception as e:
            print('The Exception message is: ', e)
            return "something is wrong"
    # return render_template('results.html')
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

