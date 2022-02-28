
from numpy import array
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
import csv
from encodings import utf_8

line_number1 = 1
i = 0
raw_seq = []  # array som holder på alle verdiene fra en kolonne av ILS loggdata
 
# split a univariate sequence into samples
def split_sequence(sequence, n_steps):
	X, y = list(), list()
	for i in range(len(sequence)):
		# find the end of this pattern
		end_ix = i + n_steps
		# check if we are beyond the sequence
		if end_ix > len(sequence)-1:
			break
		# gather input and output parts of the pattern
		seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
		X.append(seq_x)
		y.append(seq_y)
	return array(X), array(y)
 
# define input sequence
with open("logTestClean.csv", 'rt', encoding="utf_8") as f:
    mycsv = csv.reader(f)
    mycsv = list(mycsv)
    for row in mycsv:
        value = mycsv[i][line_number1]
        num = float(value.replace(",", "."))
        raw_seq.append(num)
        if len(raw_seq) == 2486: # velg hvor i loggen den skal slutte, slik at man kan sammenligne faktisk data med prediksjon
            break
        i = i + 1


# choose a number of time steps
n_steps = 3
# split into samples
X, y = split_sequence(raw_seq, n_steps)
# reshape from [samples, timesteps] into [samples, timesteps, features]
n_features = 1
X = X.reshape((X.shape[0], X.shape[1], n_features))
# define model
model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(n_steps, n_features)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')
# fit model
model.fit(X, y, epochs=200, verbose=0)
# demonstrate prediction
x_input = array([1.16, 1.16, 0.47]) # de 3 siste verdiene fra "raw_seq". Sjekk loggen for å finne de
x_input = x_input.reshape((1, n_steps, n_features))
yhat = model.predict(x_input, verbose=0)
print(yhat)
#print(raw_seq[i])