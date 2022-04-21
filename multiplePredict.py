# multivariate output stacked lstm example
from numpy import array
from numpy import hstack
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from encodings import utf_8
import csv

line_numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
i = 0
 
# split a multivariate sequence into samples
def split_sequences(sequences, n_steps):
	X, y = list(), list()
	for i in range(len(sequences)):
		# find the end of this pattern
		end_ix = i + n_steps
		# check if we are beyond the dataset
		if end_ix > len(sequences)-1:
			break
		# gather input and output parts of the pattern
		seq_x, seq_y = sequences[i:end_ix, :], sequences[end_ix, :]
		X.append(seq_x)
		y.append(seq_y)
	return array(X), array(y)

in_seq1 = []
in_seq2 = []
in_seq3 = []
in_seq4 = []
in_seq5 = []
in_seq6 = []
in_seq7 = []
in_seq8 = []
in_seq9 = []
in_seq10 = []
in_seq11 = []
in_seq12 = []

#print(str(line_numbers[x]))
with open("AnomalyDetection/FormattedData/trainTest.csv", 'rt', encoding="utf_8") as f:
    mycsv = csv.reader(f)
    mycsv = list(mycsv)
    for row in mycsv:
        value1 = float(mycsv[i][line_numbers[0]])
        value2 = float(mycsv[i][line_numbers[1]])
        value3 = float(mycsv[i][line_numbers[2]])
        value4 = float(mycsv[i][line_numbers[3]])
        value5 = float(mycsv[i][line_numbers[4]])
        value6 = float(mycsv[i][line_numbers[5]])
        value7 = float(mycsv[i][line_numbers[6]])
        value8 = float(mycsv[i][line_numbers[7]])
        value9 = float(mycsv[i][line_numbers[8]])
        value10 = float(mycsv[i][line_numbers[9]])
        value11 = float(mycsv[i][line_numbers[10]])
        value12 = float(mycsv[i][line_numbers[11]])
        in_seq1.append(value1)
        in_seq2.append(value2)
        in_seq3.append(value3)
        in_seq4.append(value4)
        in_seq5.append(value5)
        in_seq6.append(value6)
        in_seq7.append(value7)
        in_seq8.append(value8)
        in_seq9.append(value9)
        in_seq10.append(value10)
        in_seq11.append(value11)
        in_seq12.append(value12)
        
        #if len(in_seq1) and len(in_seq2) == 2484 - 1:
            #break
        i = i + 1

in_seq1 = array(in_seq1)
in_seq2 = array(in_seq2)
in_seq3 = array(in_seq3)
in_seq4 = array(in_seq4)
in_seq5 = array(in_seq5)
in_seq6 = array(in_seq6)
in_seq7 = array(in_seq7)
in_seq8 = array(in_seq8)
in_seq9 = array(in_seq9)
in_seq10 = array(in_seq10)
in_seq11 = array(in_seq11)
in_seq12 = array(in_seq12)
out_seq = array([in_seq1[i]+in_seq2[i]+in_seq3[i]+in_seq4[i]+in_seq5[i]+in_seq6[i]+in_seq7[i]+in_seq8[i]+in_seq9[i]+in_seq10[i]+in_seq11[i]+in_seq12[i] for i in range(len(in_seq1))])
# convert to [rows, columns] structure
in_seq1 = in_seq1.reshape((len(in_seq1), 1))
in_seq2 = in_seq2.reshape((len(in_seq2), 1))
in_seq3 = in_seq3.reshape((len(in_seq3), 1))
in_seq4 = in_seq4.reshape((len(in_seq4), 1))
in_seq5 = in_seq5.reshape((len(in_seq5), 1))
in_seq6 = in_seq6.reshape((len(in_seq6), 1))
in_seq7 = in_seq7.reshape((len(in_seq7), 1))
in_seq8 = in_seq8.reshape((len(in_seq8), 1))
in_seq9 = in_seq9.reshape((len(in_seq9), 1))
in_seq10 = in_seq10.reshape((len(in_seq10), 1))
in_seq11 = in_seq11.reshape((len(in_seq11), 1))
in_seq12 = in_seq12.reshape((len(in_seq12), 1))
out_seq = out_seq.reshape((len(out_seq), 1))
# horizontally stack columns
dataset = hstack((in_seq1, in_seq2, in_seq3, in_seq4, in_seq5, in_seq6, in_seq7, in_seq8, in_seq9, in_seq10, in_seq11, in_seq12, out_seq))
# choose a number of time steps
n_steps = 3      
# convert into input/output
X, y = split_sequences(dataset, n_steps)
# the dataset knows the number of features, e.g. 2
n_features = X.shape[2]
# define model
model = Sequential()
model.add(LSTM(100, activation='relu', return_sequences=True, input_shape=(n_steps, n_features)))
model.add(LSTM(100, activation='relu'))
model.add(Dense(n_features))
model.compile(optimizer='adam', loss='mse')
# fit model
model.fit(X, y, epochs=400, verbose=0)
# demonstrate prediction
c = len(in_seq12) - 1
L1 = [in_seq1[c-2], in_seq2[c-2], in_seq3[c-2], in_seq4[c-2], in_seq5[c-2], in_seq6[c-2], in_seq7[c-2], in_seq8[c-2], in_seq9[c-2], in_seq10[c-2], in_seq11[c-2], in_seq12[c-2], in_seq1[c-2] + in_seq2[c-2] + in_seq3[c-2] + in_seq4[c-2] + in_seq5[c-2] + in_seq6[c-2] + in_seq7[c-2] + in_seq8[c-2] + in_seq9[c-2] + in_seq10[c-2] + in_seq11[c-2] + in_seq12[c-2]]
L2 = [in_seq1[c-1], in_seq2[c-1], in_seq3[c-1], in_seq4[c-1], in_seq5[c-1], in_seq6[c-1], in_seq7[c-1], in_seq8[c-1], in_seq9[c-1], in_seq10[c-1], in_seq11[c-1], in_seq12[c-1], in_seq1[c-1] + in_seq2[c-1] + in_seq3[c-1] + in_seq4[c-1] + in_seq5[c-1] + in_seq6[c-1] + in_seq7[c-1] + in_seq8[c-1] + in_seq9[c-1] + in_seq10[c-1] + in_seq11[c-1] + in_seq12[c-1]]
L3 = [in_seq1[c-2], in_seq2[c], in_seq3[c], in_seq4[c], in_seq5[c], in_seq6[c], in_seq7[c], in_seq8[c], in_seq9[c], in_seq10[c], in_seq11[c], in_seq12[c], in_seq1[c] + in_seq2[c] + in_seq3[c] + in_seq4[c] + in_seq5[c] + in_seq6[c] + in_seq7[c] + in_seq8[c] + in_seq9[c] + in_seq10[c] + in_seq11[c] + in_seq12[c]]
x_input = array([L1, L2, L3])
x_input = x_input.reshape((1, n_steps, n_features))
yhat = model.predict(x_input, verbose=0)
print(yhat)