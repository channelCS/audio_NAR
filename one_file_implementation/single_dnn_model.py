# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 03:28:50 2018

@author: channelCS
"""

#Our files
import config as cfg

#Python modules
import time
import csv
import cPickle

#Data managing modules
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cross_validation import KFold
from sklearn.metrics import classification_report, accuracy_score

#Deep Learning Modules
from keras.models import Sequential
from keras.layers import Dense,Dropout
from keras.layers.advanced_activations import LeakyReLU
from keras.utils import to_categorical


np.random.seed(1234)

def get_dimension(feature):
        return {
            "cqt"               :80,
            "logmel_kong"       :40,
            "logmel_lib_delta"  :60,
            "mel"               :40,
         }.get(feature, 1000) 


def prepare_model():
    model = Sequential()
    model.add(Dense(input_neurons, input_dim = dimension2, activation=act1))
    lr=LeakyReLU(alpha=.001)
    model.add(lr)
    model.add(Dropout(dropout))
    model.add(Dense(input_neurons, activation=act2))
    model.add(Dropout(dropout))
    model.add(Dense(input_neurons, activation=act3))
    model.add(Dropout(dropout))
    model.add(Dense(num_classes, activation=act4))
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    
    return model

input_neurons=200
dropout=0.1
act1='linear'
act2='relu'
act3='sigmoid'
act4='softmax'
epochs=20
batchsize=20
agg_num=10
hop=10
feature="mel"
num_classes=4

dimension1 = get_dimension(feature)
dimension2 = dimension1*10


tr_X=np.load('features/mel_tr_X.npy')
tr_y=np.load('features/tr_y.npy')


tr_X=tr_X.reshape(tr_X.shape[0],tr_X.shape[1]*tr_X.shape[2])

kf = KFold(len(tr_X),2,shuffle=True,random_state=42)
results=[]    
for train_indices, test_indices in kf:
    train_x = [tr_X[ii] for ii in train_indices]
    train_y = [tr_y[ii] for ii in train_indices]
    test_x  = [tr_X[ii] for ii in test_indices]
    test_y  = [tr_y[ii] for ii in test_indices]
    train_y = to_categorical(train_y,num_classes=4)
    test_y = to_categorical(test_y,num_classes=4) 
    
    train_x=np.array(train_x)
    train_y=np.array(train_y)
    test_x=np.array(test_x)
    test_y=np.array(test_y)
    print "All arrays loaded"
    
    #get compiled model
    lrmodel=prepare_model()
    #see the model
    print lrmodel.summary()
    #fit the model
    lrmodel.fit(train_x,train_y,batch_size=batchsize,epochs=epochs,verbose=1)
    
    #make prediction
    pred=lrmodel.predict(test_x, batch_size=32, verbose=0)

    pred = [ii.argmax()for ii in pred]
    test_y = [ii.argmax()for ii in test_y]

    results.append(accuracy_score(pred,test_y))
    print accuracy_score(pred,test_y)
    jj=str(set(list(test_y)))
    print "Unique in test_y",jj
print "Results: " + str( np.array(results).mean() )
print classification_report(np.array(test_y),pred).split('\n')


