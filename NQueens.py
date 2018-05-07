
n = int(input("Enter the no of queens:"))
board =[[],[],[],[]]
resList=[]
def findQP(count):
    global n,resList,board
    if(count==0):
        return 1
    elif(count<0):
        return 0
    for k in range(0, n):
        if k not in board[0]:
            for l in range(0, n):
                if l not in board[1]:

                    if (l - k) not in board[2] and (l + k) not in board[3]:

                        board[0].append(k)
                        board[1].append(l)
                        board[2].append(l - k)
                        board[3].append(k + l)
                        res = findQP(count - 1)

                        if (res == 0):
                            board[0].pop()
                            board[1].pop()
                            board[2].pop()
                            board[3].pop()

                        elif res==1:
                            resList+=[(k,l)]
                            return 1
    else:
        return 0


def makeMatrix():
    a = [0] * n
    for i in range(n):
        a[i] = [' x '] * n
    for i in resList:
        a[i[0]][i[1]]="(*)"

    print ()
    print ("Points",end=":")
    for point in resList:
        print ("(",point[0]+1,",",point[1]+1,")",end=" ")
    print ("\n")
    for i in range(n):
        #print ("|", end="\t")
        for j in range(n):
            print (a[i][j],end="\t")
        print ()


if(findQP(n)):

    #print (resList)
    makeMatrix()

else:
    print ("No")
    
