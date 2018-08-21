
i = 0
while i != 3:
    #Choosing the search
    print "-------------------------------------------------------------"
    print("\nChoose your search options:")
    print("1. Keyword Search \n2. IFS \n3. Exit\n");

    i=input();
    if i == 1:
        print "You choose Keyword Search"
        from key import keyword
        keyword()
    elif i == 2:
        print "Your choice is IFS"
        from ifs import IFS
        IFS()
    elif i == 3:
        print "Exiting...!!"
    else:
        print "Invalid Choice..... TRY AGAIN....!!"
