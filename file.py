import random
import queue

lambd = 1 #arrival rate poisson
miu = 1.5  #service rate for queue1
miu2 = 1.3  #service rate for queue2

q = queue.queue()   #setup queue L1
q2 = queue.queue() # setup queue L2

# Compute time of next arrival poisson distributed.
nextArrival = random.expovariate(lambd)

# Compute time of next completed service.
nextService = nextArrival + random.expovariate(miu)


def generate():     #generate random chance
    x = random.random()
    if x < 0.3:
        return True    #leave 
    else:
        return False    #go to L2 queue

counter = 0     #job number in Queue 1 (L1)
counterQ2 = 0   #job number in Queue 2 (L2)

#Jobs = 0;
while counter <= 100:
     
    # Next event is an arrival.
    while nextArrival < nextService:
        # Simulate an arrival
        q.enqueue(nextArrival)
        counter = counter + 1  
        nextArrival += random.expovariate(lambd)
          
        print ("next Arrival in Q1 (time): ",nextArrival, "for job: ",counter)
        
    # Next event is a service completion.
    arrival = q.dequeue()
    wait = nextService - arrival
    #wcounter +=1
    print ("waiting time Q1:",wait, "for job: ",counter)
    
    nextArrivalQ2 = nextService
    nextServiceQ2 = nextArrival + random.expovariate(miu2)
    p = generate() # p determine leave the system or go to queue L2
    
    if(p):      #if probability = 0.3 go to L2 
        #c= 1
        if nextArrivalQ2 < nextServiceQ2:
            q2.enqueue(nextArrivalQ2)
            #nextArrivalQ2 += random.expovariate(lambd)
            counterQ2 = counter    
            print ("Arrival in Q2 (time): ",nextArrivalQ2, "for job: ",counterQ2)
        
        #job reveive service S2 in L2    
        arrivalQ2 = q2.dequeue()
        waitQ2 = nextServiceQ2 - arrivalQ2
    
        print ("waiting time Q2:",waitQ2, "for job: ",counterQ2)
        q.enqueue(arrivalQ2)        #return to queue1 L1s
        
    # Update the queue.
    if q.isEmpty():
        nextService = nextArrival + random.expovariate(miu)
    else:
        nextService = nextService + random.expovariate(miu)
