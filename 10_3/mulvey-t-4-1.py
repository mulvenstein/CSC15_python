#file : mulvey-t-4-1
#purpose : using functions, generate and print a users ID
# author :tom mulvey
#date : 10/3
#vers .0.1

def getLoginID(firstName, lastName, IDNum, ls):
    #print("vars sent fine test")
    fName = firstName[0]
    lName = lastName[0:5]
    ID = IDNum[-2:]
    print(fName, lName, ID) #test to see if man. correct
    ls.append(fName)
    ls.append(lName)
    ls.append(ID)
    return ls

def main():
	
    firstName = input("What is your first name? : ")
    lastName = input("What is your last name? : ")
    IDNum = input("What is your ID number ? : ")#Does not need to be an int
    #todo : figure out better variable names. can reuse firstName, lastName
    #and IDnum, but I dont like to use same var names in dif scopes :(
    lst = []
    getLoginID(firstName, lastName, IDNum, lst)
    print("Id is : ", lst[0]+lst[1]+lst[2])
    return
#---#
main()

''''
fix var nams,
although id nnum doesnt need to be an int, maybe i
should use modular for it.

''''
