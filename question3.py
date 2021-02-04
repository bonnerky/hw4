def name_gen(firstname,lastname):
    if (firstname.find(' ') != -1 or lastname.find(' ') != -1):
        return ("please input just your first and last name")
    elif (firstname.isalpha() and lastname.isalpha()):
        return(firstname + ' ' + lastname)
    else:
        return("Name includes illegal characters")


#firstname = input("first name?")
#lastname = input("first name?")
#name_gen(firstname,lastname)