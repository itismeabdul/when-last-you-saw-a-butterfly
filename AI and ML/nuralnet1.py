import numpy as np
fw = np.array([[0.2,0.7],[0.9,0.3]])
sw = np.array([[0.1,0.9],[0.3,0.4]])
wcopy = np.array([[0,0],[0,0]])
wcopyadd = np.array([[0],[0]])
sl = None
x = np.array([[2],[4]])
def train(x,y):
	for i in range(100000):
		global fw,sw,sl,wcopy,wcopyadd
		#print('fw:',fw)
#		print()
#		print('sw:',sw)
#		print()
#		print('wcopy:',wcopy)
#		print()
#		print('wcopyadd:',wcopyadd)
#		print()
#		print("______i______")
		sl = 1/(1+(np.exp(-np.dot(fw,x))))
		out = np.dot(sw,sl)
		err = y - out
	#	print('err :',err)
	#	print()
		
		for i in range(len(sw)):
			for j in range(len(sw[i])):
				wcopy[i][j] = (sw[i][j]/sum(sw[i])) * sum(err)
				sw[i][j] = sw[i][j]+((sw[i][j]/sum(sw[i])) * sum(err))
		for i in range(len(wcopyadd)):
			wcopyadd[i] = sum(wcopy[:,i])
		for i in range(len(fw)):
				for j in range(len(fw[i])):
					fw[i][j] = fw[i][j]+((fw[i][j]/sum(fw[i])) * sum(err))
		

	
def test(x):
		global fw,sw,sl,wcopy,wcopyadd
		sl = np.dot(fw,x)
		out = np.dot(sw,sl)
		print(out)
	
train(x,np.array([[3],[4]]))
test(x)
	
				
				
				
			
	
	