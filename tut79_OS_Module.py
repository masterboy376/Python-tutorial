import os
from tkinter import Variable

print(dir(os))

# see and change current working directory 
# print(os.getcwd())
# os.chdir('C://')#try to keep working directly in which you are working becoz fill module search in current directory
# print(os.getcwd())

# see files in current working directory 
# print(os.listdir())
# print(os.listdir('C://'))

# creating new folder in current working directory 
# os.mkdir('hello_os_module1')
# os.makedirs('hello_os_module2/hihihi')

# renaming 
# os.rename('text.txt', 'textFile.txt')
# os.rename('hello_os_module2', 'hello_os_module_sec')

# reading environment Variable 
# print(os.environ.get('Path'))

#joing two paths correctly
# print(os.path.join("c:/", "/textFile.text"))# in optimal way

# check whether the given path exists or not 
# print(os.path.exists("C://"))
# print(os.path.exists("q://"))

#whether the path is of file or not
# print(os.path.isfile('C://Program Files'))
# print(os.path.isdir('C://Program Files'))

