coins=[1,2,5]

def get(tab,val):
    if tab[val]!=float('inf'):
        return tab[val];
    minV=float('inf')
    for c in coins:
        if val-c>=0:
            nVal=get(tab,val-c)
            if nVal<minV:
                minV=nVal
    tab[val]=minV+1
    return tab[val]

def dynamic(amount):
    tab=[float('inf') for _ in range(amount+1)]
    tab[0]=0
    return get(tab,amount)

class Result:
    amount=0
    coins=[]
    def __init__(self, amountN):
        self.amount=amountN
        self.coins=[0 for _ in range(len(coins))]

def getWithCoins(tab,val):
    if tab[val].amount!=float('inf'):
        return tab[val];
    minV=Result(float('inf'))
    imin = -1
    for i in range(len(coins)):
        if val-coins[i]>=0:
            nVal=getWithCoins(tab,val-coins[i])
            if nVal.amount<minV.amount:
                minV=nVal
                imin=i
    newResult=Result(minV.amount+1)
    for i in range(len(coins)):
        newResult.coins[i]=minV.coins[i]
    newResult.coins[imin]=newResult.coins[imin]+1
    tab[val]=newResult
    return tab[val]
    
def dynamicPrintCoins(amount):
    print("Print dynamic")
    tab=[Result(float('inf')) for _ in range(amount+1)]
    tab[0].amount=0
    r = getWithCoins(tab,amount)
    for i in range(len(coins)):
         print(coins[i],"-",r.coins[i])
    print("Total -",r.amount)

def greedy(amount):
    actual=amount
    numberC=0
    for c in reversed(coins):
        if actual-c>=0:
            numberC=numberC+actual//c
            actual=actual%c
    return numberC

def greedyPrintCoins(amount):
    print("Print greedy")
    actual=amount
    numberC=0
    for c in reversed(coins):
        if actual-c>=0:
            numberC=numberC+actual//c
            print(c,"-",actual//c)
            actual=actual%c
        else:
            print(c,"- 0")
    print("Total -",numberC)

if __name__ == '__main__':
    amount=input("Give an amount: ")
    print("Dynamic: ",dynamic(int(amount)))
    print("Greedy: ",greedy(int(amount)))
    dynamicPrintCoins(int(amount))
    greedyPrintCoins(int(amount))
