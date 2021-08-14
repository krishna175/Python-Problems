import time
#
initial = time.time()
i = 0
while(i<10):
    print("PYTHON TUTORIAL")
    time.sleep(2)   # stop running for 2 sec and then run after 2 sec
    i+=1
print("While loop took : ", time.time() - initial)
print("----------------------")

initial2 = time.time()
for i in range(10):
    print("PYTHON TUTORUAL")
print("For loop took : ",time.time()-initial2)

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)
print(time.asctime())






