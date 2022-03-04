# Health Management System
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client.

def getdate():
    import datetime
    return datetime.datetime.now()




def client(v):
    if (v==1):
        c=int(input("\nPress: 1 for Exercise \t 2 for Food\n"))
        if (c==1):
            exrcse=input("Write Exercise Name: ")
            with open("gv_exrcse.txt","a") as f:
                # f.write(str([str(getdate())])+": "+exrcse+"\n")
                f.write(str(getdate())+" : "+exrcse+"\n")
            print("Successfully written")
        elif(c==2):
            food=input("Write Food Name: ")
            with open("gv_food.txt","a") as f:
                f.write(str(getdate())+" : "+food+"\n")
            print("Successfully written")
        else:
            print("Invalid Command!!")


    elif(v==2):
        c=int(input("\nPress: 1 for Exercise \t 2 for Food\n"))
        if(c==1):
            exrcse=input("Enter Exercise Name: ")
            with open("bnshj_exrcse.txt","a") as f:
                f.write(str(getdate())+" : "+exrcse+"\n")
            print("Successfully written")
        elif(c==2):
            food=input("Enter Food Name: ")
            with open("bnshj_food.txt","a") as f:
                f.write(str(getdate())+" : "+food+"\n")
            print("Successfully written")
        else:
            print("Invalid Command!!")


    elif(v==3):
        c=int(input("\nPress: 1 for Exercise \t 2 for Food\n"))
        if(c==1):
            exrcse=input("Enter Exercise Name: ")
            with open("bdl_exrcse.txt","a") as f:
                f.write(str(getdate())+" : "+exrcse+"\n")
            print("Successfully written")
        elif(c==2):
            food=input("Enter Food Name: ")
            with open("bdl_food.txt","a") as f:
                f.write(str(getdate())+" : "+food+"\n")
            print("Successfully written")
        else:
            print("Invalid Command!!")


    else:
        print("Invalid Command!!")




def retrive(v):
    if (v==1):
        c=int(input("\nPress: 1 for Exercise \t 2 for Food\n"))
        if (c==1):
            print("\n\t  EXERCISE LOG")
            with open("gv_exrcse.txt") as f:
                for contents in f:
                    print(contents)
        elif(c==2):
            print("\n\t  FOOD LOG")
            with open("gv_food.txt") as f:
                for contents in f:
                    print(contents)
        else:
            print("Invalid Command!!")
    

    elif(v==2):
        c=int(input("\nPress: 1 for Exercise \t 2 for Food\n"))
        if(c==1):
            print("\n\t  EXERCISE LOG")
            with open("bnshj_exrcse.txt") as f:
                for contents in f:
                    print(contents)
        elif(c==2):
            print("\n\t  FOOD LOG")
            with open("bnshj_food.txt") as f:
                for contents in f:
                    print(contents)
        else:
            print("Invalid Command!!")
            

    elif(v==3):
        c=int(input("\nPress: 1 for Exercise \t 2 for Food\n"))
        if(c==1):
            print("\n\t  EXERCISE LOG")
            with open("bdl_exrcse.txt") as f:
                   for contents in f:
                    print(contents)
        elif(c==2):
            print("\n\t  FOOD LOG")
            with open("bdl_food.txt") as f:
                for contents in f:
                    print(contents)
        else:
            print("Invalid Command!!")


    else:
        print("Invalid Command!!")




print("\n\t\t\tHealth Management System\n\n")
while(True):
    a=int(input("\nPress: 1 to Enter the data \t 2 to Retrieve the data \t 3 to Quit the program\n"))
    if (a==1):
        b=int(input("\nPress: 1 for Gaurav \t 2 for Banshaj \t  3 for Badal \n"))
        client(b)

    elif(a==2):
        b=int(input("\nPress: 1 for Gaurav \t 2 for Banshaj \t  3 for Badal \n"))
        retrive(b)
    elif(a==3):
        print("Program terminated!!")
        quit()
    else:
        print("Enter the Valid Command.")