from datetime import datetime
import threading
from wscap import getstat


#if __name__ == "__main__":
def checkstarter():
    start=datetime.now()
    print("Start: ",start)
    #lst=[['https://www.google.com/','Google offered',['heyrameee@gmail.com','+917708573709']]]
    lst=[['https://ser.he5.in/','Google offered',['heyrameee@gmail.com','+917708573709']]]
    procs = []
    j=0
    for i in lst:
        proc = threading.Thread(target=getstat, args=(i[0],i[1],i[2]))
        procs.append(proc)
        proc.start()
        procs[j].join()
        j+=1
    end=datetime.now()
    print("End: ",end)
    print("Difference: ",end-start)
