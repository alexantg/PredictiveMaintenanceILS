# multivariate output stacked lstm example
from numpy import array
from numpy import hstack
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from encodings import utf_8
import csv

line_numbers = [1,2,3,4,5,6,7,8]
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

#print(str(line_numbers[x]))
with open("FormattedData/train.csv", 'rt', encoding="utf_8") as f:
    mycsv = csv.reader(f)
    mycsv = list(mycsv)
    for row in mycsv:
        value1 = mycsv[i][line_numbers[0]]
        value2 = mycsv[i][line_numbers[1]]
        num1 = float(value1.replace(",", "."))
        num2 = float(value2.replace(",", "."))
        in_seq1.append(num1)
        in_seq2.append(num2)
        if len(in_seq1) and len(in_seq2) == 2484 - 1:
            break
        i = i + 1

in_seq1 = array(in_seq1)
in_seq2 = array(in_seq2)
out_seq = array([in_seq1[i]+in_seq2[i] for i in range(len(in_seq1))])
# convert to [rows, columns] structure
in_seq1 = in_seq1.reshape((len(in_seq1), 1))
in_seq2 = in_seq2.reshape((len(in_seq2), 1))
out_seq = out_seq.reshape((len(out_seq), 1))
# horizontally stack columns
dataset = hstack((in_seq1, in_seq2, out_seq))
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
b = len(in_seq1) - 1
c = len(in_seq2) - 1
L1 = [in_seq1[b-2], in_seq2[c-2], in_seq1[b-2] + in_seq2[c-2]]
L2 = [in_seq1[b-1], in_seq2[c-1], in_seq1[b-1] + in_seq2[c-1]]
L3 = [in_seq1[b], in_seq2[c], in_seq1[b] + in_seq2[c]]
x_input = array([L1, L2, L3])
x_input = x_input.reshape((1, n_steps, n_features))
yhat = model.predict(x_input, verbose=0)
print(yhat)