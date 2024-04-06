#All necessary imports
import uvicorn
from fastapi import FastAPI
from winefeatures import WineFeature
import pickle
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier


#Create the app object
app = FastAPI()
wine_classifier = pickle.load(open('wine_class_prediction.pkl', 'rb'))


#index route opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message':'Welcome to the Wine Prediction site'}

#Prediction functionality
@app.post('/predict')
def predictWineClass(data:WineFeature):
    data = data.dict()
    alcohol = data['alcohol']
    malic_acid = data['malic_acid']
    ash = data['ash']
    alcalinity_of_ash = data['alcalinity_of_ash']
    magnesium = data['magnesium']
    total_phenols = data['total_phenols']
    flavanoids = data['flavanoids']
    nonflavanoid_phenols = data['nonflavanoid_phenols']
    proanthocyanins = data['proanthocyanins']
    color_intensity = data['color_intensity']
    hue = data['hue']
    od280_od315_of_diluted_wines = data['od280_od315_of_diluted_wines']
    proline = data['proline']
    arr = np.array([[alcohol, malic_acid, ash, alcalinity_of_ash, magnesium, total_phenols, flavanoids, nonflavanoid_phenols, proanthocyanins, color_intensity, hue, od280_od315_of_diluted_wines, proline]])    
    pred = wine_classifier.predict(arr)
    #return {'Class of the Wine is:{}'.format(pred)}
    return 'Class of the Wine is:{}'.format(pred)

#Run the API with uvicorn
#API will run on http://127.0.0.1:8000
if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
#uvicorn <app/filename>:<app/object_name> --reload