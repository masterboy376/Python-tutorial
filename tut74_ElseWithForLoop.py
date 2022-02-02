khana = ['roti','dal','chawal','sabji']
for item in khana:
    if item == 'paratha':
        break
else:
    print('paratha not found')
#normal behaviour: if the for loop completed without any break (not continue) only then the below else will run