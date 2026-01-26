dt = input("Enter date in the format MMDDYYYY: ")

if dt[0] == "0":

    if dt[1] == "1":

        a = "January"

    elif dt[1] == "2":

        a = "February"

    elif dt[1] == "3":

        a = "March"

    elif dt[1] == "4":

        a = "April"

    elif dt[1] == "5":

        a = "May"

    elif dt[1] == "6":

        a = "June"

    elif dt[1] == "7":

        a = "July"

    elif dt[1] == "8":

        a = "August"

    elif dt[1] == "9":

        a = "September"

    elif dt[1] == "10":

        a = "October"

elif dt[0] == "1":

    if dt[1] == "1":

        a = "November"

    elif dt[1] == "2":

        a = "December"

print(a," ", dt[2],dt[3],",", " ", dt[4:], sep = "")
