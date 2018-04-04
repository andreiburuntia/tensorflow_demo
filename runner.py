import subprocess
import os

batch_sizes=[30,50,100,150,200,300,500]
steps=[100,200,500,1000,3000,10000]
epochs=[1,2,3,4]

results={}

for epoch in epochs:
    for step in steps:
        for batch_size in batch_sizes:
            print('python cnn_mnist.py '+' '+str(batch_size)+' '+str(step)+' '+str(epoch))
            cmd = ['python cnn_mnist.py', str(batch_size), str(step), str(epoch)]
            os.system('python cnn_mnist.py '+' '+str(batch_size)+' '+str(step)+' '+str(epoch))