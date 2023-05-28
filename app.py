
import pickle
import sys
import numpy as np
from sklearn.linear_model import LogisticRegression

# # Load the pickle file 
# with open('./model.pkl', 'rb') as model_pkl:
#     model = pickle.load(model_pkl)
    
# Import Flask for creating API
from flask import Flask, request
    
# Initialise a Flask object
app = Flask(__name__)

# Create an API endpoint for predicting
@app.route('/predict')
def predict_cancer():
    # Read all necessary request parameters
    s1 = request.args.get('s1')
    
    #prediction for unseen data
    # unseen_data = np.array([[s1]]).astype(np.float64)
    
    result = s1+'_aagya_see'
    
    # return the result
    return 'Predicted result for observation  is: ' + str(result)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)