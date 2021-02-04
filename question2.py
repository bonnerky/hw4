def average_val(mylist):
    total = float(0)
    if (len(mylist) == 0):
        return ("empty list")
    else:
        for x in mylist:
            if (isinstance(x,float) or isinstance(x,int)):
                total = total+x
            else:
                return("bad input") 
    
    return(total/len(mylist))


#mylist = [2.4, 3, 8, 3.98, 6]
#average_val(mylist)