import datetime
while(True):
    def gettime():
       return datetime.datetime.now()

    def take(k):
        if k==1:
            a=int(input('''*Press 1 For Food:\n*Press 2 For Exercise:\n'''))
            if a==1:
                c=input("What You Eat Today Rohan?\n")
                with open("rohan-food.txt","a") as f:
                   f.write(str([str(gettime())])+":"+ c +"\n")
          


            if a==2:
                c=input("Rohan What You Done Today?\n")
                with open("rohan-exe.txt","a") as f:    
                   f.write(str([str(gettime())])+":"+ c +"\n")
        
        if k==2:
            a=int(input('''*Press 1 For Food:\n*Press 2 For Exercise:\n'''))
            if a==1:
                c=input("What You Eat Today Rohit?\n")
                with open("rohit-food.txt","a") as f:
                   f.write(str([str(gettime())])+":"+ c +"\n")
            if a==2:
                c=input("Rohit What You Done Today?\n")
                with open("rohit-exe.txt","a") as f:    
                   f.write(str([str(gettime())])+":"+ c +"\n")
        if k==3:
            a=int(input('''*Press 1 For Food:\n*Press 2 For Exercise:\n'''))
            if a==1:
                c=input("What You Eat Today Shubham?\n")
                with open("shubham-food.txt","a") as f:
                   f.write(str([str(gettime())])+":"+ c +"\n")
            if a==2:
                c=input("Shubham What You Done Today?\n")
                with open("shubham-exe.txt","a") as f:    
                    f.write(str([str(gettime())])+":"+ c +"\n")
        

    def retrive(b):
        if b==1:
            c=int(input('''*Press 1 For Food:\n*Press 2 For Exercise:\n'''))
            if c==1:
                with open("rohan-food.txt") as f:
                    for i in f:
                       print(i)
        
            if c==2:
                with open("rohan-exe.txt") as f:
                    for i in f:
                        print(i)

        if b==2:
            c=int(input('''*Press 1 For Food:\n*Press 2 For Exercise:\n'''))
            if c==1:
                with open("rohan-food.txt") as f:
                    for i in f:
                      print(i)
            if c==2:
                with open("rohan-exe.txt") as f:
                    for i in f:
                        print(i)
        if b==3:
            c=int(input('''*Press 1 For Food:\n*Press 2 For Exercise:\n'''))
            if c==1:
                with open("shubham-food.txt") as f:
                    for i in f:
                      print(i)
            if c==2:
                with open("shubham-exe.txt") as f:
                    for i in f:
                        print(i)
    
    print("*****Wellcome To The ICMR Health Managment System*****")
    a=int(input('''*Press 1 For Log: \n*Press 2 for Retrive:\n'''))
    if a==1:
        b=int(input('''*Press 1 For Rohan: \n*Press 2 for Rohit:\n*Press 3 for Shubham:\n'''))
        take(b)
    if a==2:
        b=int(input('''*Press 1 For Rohan.\n*Press 2 for Rohit\n*Press 3 for Shubham:\n'''))
        retrive(b)
    print("***Thanks For Using This Code,Have A Nice Day***\n")