import numpy as np
from sklearn import preprocessing

def create_x(dic):
    X = np.concatenate([[e for e in k] for k in dict])
    return np.array([e.reshape((28,28)) for e in X])
    
    
def y_encoder(y):
    le = preprocessing.LabelEncoder()
    le.fit(list(set(y)))
    print(le.classes_)
    return le.transform(y)

def create_y(dic):
    y = []
    for k in dic:
        y.append(np.repeat(k, len(dic[k])))
    return y_encoder(np.concatenate(y))