import pickle 

#pickling a python object
# cars = ['tata motors', 'bugatti', 'lamborgini', 'kaush']
# file = "mycar.pkl"
# fileObj= open(file, 'wb')
# pickle.dump(cars, fileObj)
# fileObj.close()

# depickling the python obj
file = "mycar.pkl"
fileObj = open(file, 'rb')
cars = pickle.load(fileObj)
fileObj.close()
print(cars)

# what is pickle.loads( )