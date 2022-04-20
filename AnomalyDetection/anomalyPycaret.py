from pycaret.datasets import get_data
from pycaret.anomaly import *

import pandas as pd

data = pd.read_csv('FormattedData/train.csv')
data_unseen = pd.read_csv('FormattedData/test.csv')

data.reset_index(drop=True, inplace=True)
data_unseen.reset_index(drop=True, inplace=True)

print('Data for Modeling: ' + str(data.shape))
print('Unseen Data For Predictions: ' + str(data_unseen.shape))

exp_ano101 = setup(data, normalize = True, 
                   ignore_features = ['Timestamp'],
                   session_id = 123)


#Create model: IFOREST
#iforest = create_model('iforest')
#iforest_results = assign_model(iforest)
#iforest_results.head()

#Create model: CLUSTER
#cluster = create_model('cluster')
#cluster_results = assign_model(cluster)
#cluster_results.head()


#Create model: KNN
#knn = create_model('knn')
#knn_results = assign_model(knn)
#knn_results.head()

#Save model
#save_model(knn,'AnomalyDetection/Models/KNN100322CN_GP03')


#saved_knn = load_model('SavedModels/KNN100322CN_GP03')

#Load model
saved_iforest = load_model('SavedModels/IFOREST100322CN_GP03_new')


#Predict on test data
unseen_predictions = predict_model(saved_iforest, data=data_unseen)
unseen_predictions.head()

unseen_predictions.to_csv('FormattedData/resultsIFOREST.csv')
#print(unseen_predictions)


#Plot results
plot_model(saved_iforest, plot = 'umap')

