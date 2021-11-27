import multiprocessing
import os
import subprocess

def simple_DNS(name):
    ret=subprocess.run(["dnslookup",name,"dns.adguard.com"])
    #print("The process returned with return code" + str(ret))
    print(p1.pid)
    #os.system("nethogs")

def DNS_over_TLS(name):
    ret=subprocess.run(["dnslookup",name,"dns.adguard.com"])
    #print("The process returned with return code" + str(ret))
    #os.system("nethogs")



p1 = multiprocessing.Process(target=simple_DNS, args=("google.com",))
p2 = multiprocessing.Process(target=DNS_over_TLS, args=("google.com",))

# starting process 1
p1.start()
# starting process 2
p2.start()

print("Process 1 id "+str(p1.pid))
print("Process 2 id "+str(p2.pid))

# wait until process 1 is finished
os.system("nethogs")
p1.join()
# wait until process 2 is finished
os.system("nethogs")
p2.join()



# both processes finished
print("Done!")


Ayush Anand,Third year Undergraduate,Computer Science and Engineering,IIT Gandhinagar| Mo: 9472222295
