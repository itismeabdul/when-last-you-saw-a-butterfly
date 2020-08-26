import numpy as np
import scipy.special as sigmoid

correct = 0
wrong = 0
numtest  = 0

class NeuralNetwork:
	
	def __init__(self, inputNodes, hiddenNodes, outputNodes, learningRate):
		self.inNodes = inputNodes
		self.hNodes = hiddenNodes
		self.oNodes = outputNodes
		self.lRate = learningRate
		self.ihw = ((np.random.rand(self.hNodes,self.inNodes))-0.5)
		self.how = ((np.random.rand(self.oNodes,self.hNodes))-0.5)
		self.Actfunc = lambda x : sigmoid.expit(x)
	
	def train(self, inputlist, targetlist):

			inputs = np.array(inputlist, ndmin = 2).T
			targets = np.array(targetlist, ndmin = 2).T
			hiddenlayin = np.dot(self.ihw,inputs)
			hiddenlayout = self.Actfunc(hiddenlayin)
			outlayin = np.dot(self.how,hiddenlayout)
			outlayout = self.Actfunc(outlayin)
			
			outerror = targets - outlayout
			hiddenerror = np.dot(self.how.T,outerror)
			self.how += self.lRate * np.dot((outerror * outlayout * (1.0 - outlayout)), np.transpose(hiddenlayout))
			self.ihw += self.lRate * np.dot((hiddenerror * hiddenlayout * (1.0 - hiddenlayout)), np.transpose(inputs))
			pass
		
	def query(self, inputlist):
		
		inputs = np.array(inputlist, ndmin = 2).T
		hiddenlayin = np.dot(self.ihw,inputs)
		hiddenlayout = self.Actfunc(hiddenlayin)
		outlayin = np.dot(self.how,hiddenlayout)
		outlayout = self.Actfunc(outlayin)
		return outlayout
		pass
	#def print(self):
#		print(self.inNodes,self.hNodes,self.oNodes,self.lRate)
#		print(self.ihw)
#		print(self.how)
	
n = NeuralNetwork(784, 100, 10, 0.5)
with open('/storage/emulated/0/Download/mnist_test.csv') as data2:
	data2 = data2.readlines()
	data2 = data2[:10]
	print('output before training')
	print()
	for data_2 in data2:
		numtest +=1
		trueval = int(data_2[0])
		allvalues2 = data_2.split(',')
		test = np.asfarray(allvalues2)
		test = test[1:]
		test = (test / 255 * 0.99) + 0.01
		ans = n.query(test)
		ans = np.argmax(ans)
		print('true value: ', trueval, 'network value :', ans)
		if ans == trueval:
			correct +=1
		
		else:
			wrong += 1
		
print()	
print('out of',numtest)
print('correct:', correct)
print('wrong:', wrong)
print(correct+wrong)
print()
print()

with open('/storage/emulated/0/Download/mnist_train.csv', 'r') as data:
	data = data.readlines()
	alldata = data[:600]
	print('training starting')
	print()
	for i in range(5):
		for record in alldata:
			allvalues = record.split(',')
			data = np.asfarray(allvalues)
			data = data[1:]
			data = (data / 255.0 * 0.99) + 0.01
			
			onodes = 10
			targets = np.zeros(onodes) +0.01
			targets[int(allvalues[0])] = 0.99
			n.train(data,targets)
		print(i+1,'epoch finished')
	print()
		
with open('/storage/emulated/0/Download/mnist_test.csv') as data2:
	data2 = data2.readlines()
	data2 = data2[:10]
	correct = 0
	wrong = 0
	numtest = 0
	print('output after training')
	print()
	for data_2 in data2:
		numtest +=1
		trueval = int(data_2[0])
		allvalues2 = data_2.split(',')
		test = np.asfarray(allvalues2)
		test = test[1:]
		test = (test / 255 * 0.99) + 0.01
		ans = n.query(test)
		ans = np.argmax(ans)
		print('true value: ', trueval, 'network value :', ans)
		if ans == trueval:
			correct +=1
		
		else:
			wrong += 1
		
print()	
print('out of',numtest)
print('correct:', correct)
print('wrong:', wrong)
print('total tested:',correct+wrong)
print()
print()
	
	