import numpy as np

GunNames=["P18C","P92","P1911","Revolver","AKM","GROZA","M16A4","M416","SCAR-L","M249","UZI","UMP-9","Tommy Gun","Vector","VSS","Mini-14","SKS","MK14 EBR","Kar98k","M24","AWM","S686/pellet","S1897/pellet","S12K/pellet","S686/total","S1897/total","S12K/total"]
DPS=[317,215,318,115,480,600,547,477,427,587,479,380,442,564,442,440,611,667,38,47,71,125,33,88,1125,300,792]
FireRate=[1000,444,545,150,600,750,800,698,625,800,1250,652,697,1091,698,600,667,667,32,33,32,300,80,240,300,80,240]

print("Total Count: Gun Names: "+str(len(GunNames))+" DPS: "+str(len(DPS))+" FireRate: "+str(len(FireRate)))

Wdps=30

while(Wdps>1 or Wdps<0):
    Wdps=float(input("Enter the weight for Damage per shot(bet 0 and 1) "))
    if(Wdps>1 or Wdps<0):
        print("The entered value is not correct")

Wfr=1-Wdps

print("The Fire rate weight is "+str(Wfr*100)+ " and the damage per second is "+str(Wdps*100))

arr=np.random.randint(len(DPS), size=(25, 2))

def calObjFunc(a):
    func=np.empty(shape=25 , dtype=float)
    for i in range(0,25,1):
        func[i] = ( Wfr * ( FireRate[ a[i][0] ]+ FireRate[ a[i][1] ] ) + Wdps *  ( DPS[ a[i][0] ]+ DPS[ a[i][1] ] ) )
    return func

def mutate(a,m):
    randpos=np.random.choice(50,m,replace=False)
    randarr=np.zeros(shape=(25,2),dtype=int)
    for i in range(0,m,1):
        randarr[ int(randpos[i] / 2) , randpos[i] % 2] = 1 # the mask for mutation
    randvalue=np.random.randint(len(DPS),size=m ) #new random values
    c=0
    for i in range(0,25,1):
        for j in range(0,2,1):
            if(randarr[i][j] == 1 ):
                a[i][j] = randvalue[c]
                c+=1
    return a

def maxPos(a):
    return a.tolist().index(max(a))

def crossover(a):
    func= calObjFunc(a)
    funcCopy = np.copy(func)
    funcCopy.sort()
    mid= funcCopy[12] #finding the mid element the values greater than mid are good ones

    permute= np.random.permutation( np.delete( np.arange(25) , maxPos(func ) ) )
    randmask=permute[:12] # left ones cross-over
    randmask2=permute[-12:] #right ones cross-over

    a2=np.zeros(shape=(12,2),dtype=int)
    for i in range(0,12): # performing cross-over
        a2[i][0] = a[ randmask[i] , 0]
        a2[i][1] = a[ randmask2[i] , 1]

    c=0 #replacing the bad ones
    for i in range(0,25,1):
        if(func[i] < mid ):
            a[i] = a2[c]
            c+=1

    return a, funcCopy[24]

def main(a):
    noofitr= int(input("Enter no of times to iterate "))
    i,diff,countDiff=0,0,0
    mutation = 10 # the number of mutations initially 20%
    print("Initial mutation is 20%")
    while(i < noofitr):
        arrCopy = np.copy(a)
        arnew , oldmax = crossover(a)
        armut = mutate(arnew , mutation )
        newmax = np.amax( calObjFunc(armut) )

        if( newmax < oldmax): #ignoring if mutation destroys the best
            a = np.copy(arrCopy)
            i-=1
            print("Cancelling Iteration")
        else :
            a=np.copy(armut)
            print("The maximum fitness value iteration no "+str(i)+ " is " + str(newmax) +" mutaion % "+ str( int( (mutation/50)*100) ) )

        diff = int((newmax - oldmax) * 10000)
        if (diff <= 500 and diff >= 0):
            if (mutation != 30):
                print("Changing mutation to 60%")
            mutation = 30  # 60% mutation
        elif (diff <= 5000 and diff >= 0):
            if (mutation != 15):
                print("Changing mutation to 40%")
            mutation = 15  # 40% mutation

        i+=1
        if(diff == 0):
            countDiff+=1
        if(countDiff >10):
            print("Terminating for no change in maxima for last 10 iteration ")
            break

    finalFitness = calObjFunc(a)
    print("\n\nYour final best combination is "+GunNames[ a[maxPos(finalFitness)][0] ] +" and "+ GunNames[ a[maxPos(finalFitness)][1] ]  + " score : "+str(np.amax(finalFitness)) )
    finalFitness2 = np.delete( finalFitness , maxPos(finalFitness))
    pos2 = finalFitness.tolist().index(max(finalFitness2.tolist()))
    print("Your second best combination is " + GunNames[ a[pos2][0] ] + " and " + GunNames[
        a[pos2][1] ]+ " score : "+str(np.amax(finalFitness2)) )


main(arr)

