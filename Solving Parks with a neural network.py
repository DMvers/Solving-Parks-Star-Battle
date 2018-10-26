#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 17:33:02 2018

@author: david
"""

from __future__ import absolute_import, division, print_function

import tensorflow as tf
from tensorflow import keras
import numpy as np
import generateparkproblems



tf.enable_eager_execution()

#Load data
sols, probs = zip(*generateparkproblems.genprobs(101000)) 
probdata = np.array(probs)
soldata = np.array(sols)

#Create model
model = keras.Sequential()
model.add(keras.layers.Dense(16,input_dim = 16))
model.add(keras.layers.Dense(320,activation=tf.nn.relu))
model.add(keras.layers.Dense(16, activation=tf.nn.sigmoid))
model.summary()
model.compile(optimizer=tf.train.AdamOptimizer(),
              loss='mean_absolute_error',
              metrics=['accuracy'])

print(probdata)
print(soldata)

#Run model
history = model.fit(probdata[1:100000],
                    soldata[1:100000],
                    epochs=100,
                    batch_size=200,
                    validation_data=(probdata[100000:101000],soldata[100000:101000]),
                    verbose=1)

#Results
results = model.evaluate(probdata, soldata)

print(results)

for layer in model.layers:
    print(layer.output_shape)
    
#print(model.predict(probdata[0:24]))
sample = np.reshape(model.predict(probdata[0:1]),(4,4))
print(np.matrix.round(sample))
print(np.reshape(soldata[0:1],(4,4)))

sample = np.reshape(model.predict(probdata[1005:1006]),(4,4))
print(np.matrix.round(sample))
print(np.reshape(soldata[5:6],(4,4)))

sample = np.reshape(model.predict(probdata[1018:1019]),(4,4))
print(np.matrix.round(sample))
print(np.reshape(soldata[0:1],(4,4)))