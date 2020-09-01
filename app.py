import flask
from flask import request
app = flask.Flask(__name__)
app.config["DEBUG"] = True

from flask_cors import CORS
CORS(app)

# main index page route
@app.route('/')
def home():
    return '<h1>API is working.. </h1>'

@app.route('/Vivek')
def Vivek():
    return '<h1>Aspiring DataScientist TO A DATASCIENTIST .......</h1>'


@app.route('/predict',methods=['GET'])
def predict():
    import joblib
    model = joblib.load('marriage_age_predict_model1.pkl')
    predicted_age_of_marriage = model.predict([[int(request.args['gender']),
                            int(request.args['religion']),
                            int(request.args['caste']),
                            int(request.args['mother_tongue']),
                            int(request.args['country']),
                            int(request.args['height_cms']),
                           ]])
    return str(round(predicted_age_of_marriage[0],2))


if __name__ == "__main__":
    app.run(debug=True)
