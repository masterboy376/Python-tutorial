# def soldier(dir, file(dictionary), format) 
import os
def soldier(path, file, format):
    i = 1
    os.chdir(path)
    files = os.listdir(path)
    with open(file) as f:
        fileListToNotChange = f.read().split("\n")
    for file in files:
        if file not in fileListToNotChange:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1] == format:
            os.rename(file, f'{i}{format}')
            i+=1

soldier(r"C:\Users\maste\Desktop\python tutorial\test", "main.txt", ".png")            