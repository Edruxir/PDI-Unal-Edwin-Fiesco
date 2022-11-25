# -*- coding: utf-8 -*-
"""second_diff_tf.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XVNBuVBQmVeJb12TJsIz3lp28r79NYzf
"""

import matplotlib.pyplot as plt
import tensorflow as tf

x = tf.linspace(-10.0,10.0,201)
with tf.GradientTape() as tape:
    tape.watch(x)
    y = tf.sin(x)

dy_dx= tape.gradient(y,x)

plt.plot(x,y,label='y')
plt.plot(x,dy_dx,label='dy/dx')
plt.legend()

x = tf.linspace(-10.0,10.0,201)
with tf.GradientTape() as tape_0:
  tape_0.watch(x)
  with tf.GradientTape() as tape_1:
    tape_1.watch(x)
    y = tf.sin(x)
  dy_dx= tape_1.gradient(y,x)
d2y_d2x= tape_0.gradient(dy_dx,x)

plt.plot(x,y,label='y')
plt.plot(x,dy_dx,label='dy/dx')
plt.plot(x,d2y_d2x,label='d2y/d2x')
plt.legend()