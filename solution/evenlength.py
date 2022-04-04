#Write a script to enter 5 string in a list and check & print string who's length has even number of character.(without any string function)Do this script using UDF.
def createlist():
    l=[]
    for i in range(5):
        x=input("Enter any string:")
        l.append(x)

def counteven(l):
    count=0
    for i in l:
        if(i%2==0):
            count+=1
    return (count)

createlist()
ans=counteven(l)
print(ans)

