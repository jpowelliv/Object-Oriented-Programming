#Joeph Powell IV
#CIS 225-01
#10.05.18
#listmod.py


def toNumbers(strList):
        varb = int(strList[0])
        for i in range(len(strList)):
                strList[i] = int(strList[i])

def main():
        strList=["23", "45"]
        print("list before call", strList)
        for v in range(len(strList)):
                print(strList[v],"is a", type(strList[v]))

        toNumbers(strList)

        print("list after call", strList)
        for u in range(len(strList)):
                print(strList[u],"is a", type(strList[u]))

		
main()
