import numpy as np
from sklearn import datasets
import scipy.special as sigmoid
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

correct = 0
wrong = 0
accu = []
graph = []
class neuralnet:
	def __init__(self, inlay, Hidlay, outlay, learnrate):
		self.inlay = inlay
		self.Hidlay = Hidlay
		self.outlay = outlay
		self.learnrate = learnrate
		self.wih = np.random.rand(self.Hidlay,self.inlay)-0.5
		self.who = np.random.rand(self.outlay,self.Hidlay)-0.5
		self.act = lambda x: sigmoid.expit(x)
	
	def train(self, data ,target):
		global accu
		data = np.array(data, ndmin = 2).T
		target = np.array(target, ndmin = 2).T
		hiddenlay = self.act(np.dot(self.wih,data))
		output = self.act(np.dot(self.who,hiddenlay))
		a = np.argmax(target)
		b = np.argmax(output)
		if a == b:
			accu.append(1)
		else:
			accu.append(0)
		outerror = target - output
		hiddenerr = np.dot(self.who.T, outerror)
		self.who += self.learnrate * np.dot((outerror *output* (1.0 - output)), np.transpose(hiddenlay))
		self.wih += self.learnrate * np.dot((hiddenerr * hiddenlay * (1.0 - hiddenlay)), np.transpose(data))
	
	def debug(self):
		print(self.inlay)
		print(self.Hidlay)
		print(self.outlay)
		print()
		print(self.wih)
		print()
		print()
		print(self.who)
#		hiddenlay = self.act(np.dot(self.wih,self.inlay))
#		output = self.act(np.dot(self.who,hiddenlay))
#		print(ouput)
		
	def test(self,data):
		data = np.array(data,ndmin = 2).T
		hiddenlay = self.act(np.dot(self.wih,data))
		output = np.dot(self.who,hiddenlay)
		output = self.act(output)
		return np.argmax(output)

n = neuralnet(4,900,3,.0099)
data = datasets.load_iris()
x = data.data
y = data.target

xtest, xtrain, ytest, ytrain = train_test_split(x,y, test_size = 0.3, random_state = 1, stratify = y)

for j in range(500):
	for i in range(len(xtrain)):
		target = np.zeros(3)+0.01
		target[ytrain[i]] = 0.99
		inputs = xtrain[i]
		n.train(inputs,target)
	per = sum(accu)/len(accu)
	graph.append(per)
	accu = []
plt.plot(graph)
plt.xlabel('epochs')
plt.ylabel('accuracy')
plt.show()
print()
print()
print()

for i in range(len(xtest)):
	target = ytest[i]
	inputs = xtest[i]
	ans = n.test(inputs)
	if ans == target:
		correct += 1
	else:
		wrong += 1


print('correct:', correct)
print('wrong:', wrong)
print()
print()
print()
print()
	
	
#	