l1 = ['bhindi', 'aloo', 'chopsticks', 'chowmein']

# i=1
# for item in l1:
#     if i%2 is not 0:
#         print(f"jarvis please buy {item}");
#     else:
#         print(f"jarvis please dont buy {item}")
#     i+=1

for index, item in enumerate(l1):
    if index%2== 0 :
        print(f"jarvis please buy {item}");
    else:
        print(f"jarvis please dont buy {item}");

        
