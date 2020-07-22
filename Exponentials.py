import tensorflow as tf
import pandas as pd
import numpy as np


def average_exp(X):

  L = []
  for i in range(1, X.shape[1]):
    L.append(X[0, i]/X[0, i-1])
  # print(L)
  return sum(L)/len(L)


def approx(val1, val2):
  if abs(abs(val1) - abs(val2))/(abs(val1) + abs(val2)) <= 1e-2:
    return True
  return False

def checkpattern(file, column):
  """
  This function checks if the sequence has a pattern.
  Inputs:
  file: csv file having a column "Sequence"
  column : The column having the pattern
  Outputs : 
  isPattern: Boolean variable telling wether or not exponential pattern exists
  """

  df = None
  model = tf.keras.models.load_model("intbeingsExponential")
  try:
    df = pd.read_csv(file)
  except:
    pass
  
  try:
    X = df[column].values.astype('float')
  except:
    pass



  first10 = X[:10].reshape(1,10)
  last10 = X[-10:].reshape(1,10)

  first_isexp = model.predict(first10)
  last_isexp = model.predict(last10)
  if (first_isexp[0][0] <=0.7):
    return False

  else:
    print(average_exp(first10), average_exp(last10))
    if approx(average_exp(first10), average_exp(last10)):
      return (True, average_exp(first10))
    return False
    