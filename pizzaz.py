import sys



def make_movie_dict(title, year, running_time, time, room_num): #create the dictionary of movie data
    movies={}
    movies["title"] = title
    movies["year"] = year
    movies["running_time"] = running_time
    movies["time"] = time
    movies["room_num"] = room_num
    return movies
def collection(): #collection of datas
    movies = []
    movies.append(make_movie_dict("The Shining", 1980, "2h 26m", 1000, "Room 1"))
    movies.append(make_movie_dict("Your Name", 2016, "1h 52m", 1300, "Room 1"))
    movies.append(make_movie_dict("Fate/Stay Night: Heaven's Feel - III. Spring Song", 2020, "2h 0m", 1500, "Room 1"))
    movies.append(make_movie_dict("The Night Is Short, Walk on Girl", 2017, "1h 32m", 1730, "Room 1"))
    movies.append(make_movie_dict("The Truman Show", 1998, "1h 47m", 1930, "Room 1"))
    movies.append(make_movie_dict("Genocidal Organ", 2017, "1hr 55m", 2145, "Room 1"))
    
    movies.append(make_movie_dict("Jacob's Ladder", 1990, "1h 56m", 1000, "Room 2"))
    movies.append(make_movie_dict("Parasite", 2019, "2h 12m", 1215, "Room 2"))
    movies.append(make_movie_dict("The Dark Knight", 2008, "2h 32min", 1445, "Room 2"))
    movies.append(make_movie_dict("Blade Runner 2049", 2017, "2h 44m", 1745, "Room 2"))
    movies.append(make_movie_dict("The Mist", 2007, "2h 6m", 2100, "Room 2"))
    movies.append(make_movie_dict("Demon Slayer: Mugen Train", 2020, "1h59min", 2320, "Room 2"))
    
    movies.append(make_movie_dict("The Matrix", 1999, "2h 16m", 1000, "Room 3"))
    movies.append(make_movie_dict("Inception", 2010, "2h 42m", 1130, "Room 3"))
    movies.append(make_movie_dict("Shutter Island", 2010, "2h 19m", 1430, "Room 3"))
    movies.append(make_movie_dict("Soul", 2020, "1hr 40m", 1700, "Room 3"))
    movies.append(make_movie_dict("Mrs. Brown", 1997, "1h 41min", 1900, "Room 3"))
    movies.append(make_movie_dict("Peppa Pig: Festival of Fun", 2019, "1h 8min", 2100, "Room 3"))
    movies.append(make_movie_dict("Titanic", 1997, "3h 30min", 2215, "Room 3"))
    return movies
def intro_greet(): #greeting message
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~ Welcome to Pizzaz cinema ~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

def print_movie_info(movie): #printing movie information
    time = str(movie["time"]) # 1930 -> 19:30
    time = time[0] + time[1] + ":" + time[2] + time[3]
    print("{0}. {1}. {2}. {3}. {4}".format(movie["title"], movie["year"], movie["running_time"],time, movie["room_num"] ))

def invalid_switch_input(): #print error messages
    print("\nSorry. This program does not recognise the switch options. ")
    print("\nBye.")
    exit()
def invalid_time_input(): #print error messages
    print("\nSorry. This program does not recognise the time format entered.")
    print("\nBye.")
    exit()
    
def movie_after_time(movies, time):
    #invalid time option if there is no ":" in "time" variable.
    
    time = time.split(":")
    n_time = int(time[0]+time[1])
    
    # print(n_time) ->test
    # print(movies) ->test
    for movie in movies:
        movie_time = movie["time"]
        if movie_time >= n_time:
            print_movie_info(movie)
    print("\nBye.")
    exit()
            
    
def valid_movie_checker(movies, n_movie):
    n_movie_lower = n_movie.lower()
    for movie in movies:  # 
        movie_lower = movie['title'].lower()
        if len(movie_lower.split('.')) == 3: # exception for the movie "Fate/Stay...."
            split_list = movie_lower.split('.')

            #print(split_list[0] + split_list[1])
            #exit(1)
            # valid
            # Fate/Stay Night: Heaven's Feel - III. Spring Song.
            # Fate/Stay Night: Heaven's Feel - III
            # Fate/staY Night: HEAVEN's Feel - iii. Spring Song
            if n_movie_lower == movie_lower.split('.')[0] or n_movie_lower == (movie_lower.split('.')[1]).lstrip():
                return True
            elif n_movie_lower == movie_lower:
                return True
            elif n_movie_lower == split_list[0] +'.'+ split_list[1]:
                return True
        else:
                if n_movie_lower == movie_lower:
                    return True
    return False

def seat_num_manage(movies): #movies = collection, valid_n_movie
    if sys.argv[1] == "--book":
        movie_info = movies_popcorn_ask(movies) #movie title n popcorn size
        valid_n_movie = movie_info[0]
        popcorn_size = movie_info[1]
        cnt = 0
        
    else:
        valid_n_movie = movies_ask_group(movies) #just a movie title
        cnt = 0
        
    
    #seat number total num
    #add one
    #create seat num ticket
    
    
    for i in range(len(movies)): #possible seats by room number
        if valid_n_movie.upper() == (movies[i]["title"]).upper(): #find room number by title
            room_num = int(movies[i]["room_num"][5]) 
            # print(rooom_num) -> test successful
    total_seat_num = total_seat_calc(room_num)
    
    if sys.argv[1]== "--book":
        cnt +=1
        total_seat_num -= 1
        # print(total_seat_num) -> test
        print("\nThe seat number for person 1 is #17")
        itemised_detail(valid_n_movie,movies,1,popcorn_size)
    
        
    elif sys.argv[1]=="--group":
        while True: #to get valid amount of ppl (ppl > 1)
            num_ppl = int(input("\nHow many persons will you like to book for? "))
            if num_ppl <=1:
                while True: 
                    response = input("Sorry, you must have at least two customers for a group booking. Enter Y to try again or N to quit. ")
                    if response.upper() == "Y" or response.upper() == "N":
                        if response.upper() == "N":
                            print("\nBye.")
                            exit()
                        else:
                            break               
            else:
                break
        # print(total_seat_num) -> test
        cnt += num_ppl
        if total_seat_num-num_ppl<0: #not enough space to hold num_ppl
            print(f"Sorry, we do not have enough space to hold {num_ppl} people in the theater room of {total_seat_num} seats. ", end="")
            exceed_num_err =input("Enter Y to try a different movie name or N to quit. ")
            while True:
                if exceed_num_err.upper() == "Y" or exceed_num_err.upper() == "N":
                    break
            if exceed_num_err.upper() == "Y":
                seat_num_manage(movies)
            else:
                print("\nBye.")
                exit()
        # total_seat_num -= num_ppl #test
        # print(total_seat_num) #test
        print("")
        collection_popcorn = [] 
        j=1
        for i in range(1, num_ppl+1): #collection of popcorn sizes
            collection_popcorn.append(order_popcorn_group(num_ppl,j)) #list for size of popcorns
            j +=1
        
        print("")
        for i in range(1,num_ppl+1): #seat number printing with (2N-1)
            seq_seat = 2 * i - 1
            print("The seat number for person {} is #{}".format(i,seq_seat))
        itemised_detail(valid_n_movie,movies,num_ppl,collection_popcorn)

def movies_popcorn_ask(movies): #for book switch
    while True:    
        n_movie=input("\nWhat is the name of the movie you want to watch? ")

        if not valid_movie_checker(movies, n_movie):
          while True:
            i = input("\nSorry, we could not find that movie. Enter Y to try again or N to quit. ")
            if i.upper()=="N":
                print("\nBye.")
                exit()
            elif i.upper() == 'Y':
                break  
        else:
            # if user type valid movie title...
            valid_n_movie = n_movie
            break
    pop_corn_info = order_popcorn()
    return (valid_n_movie, pop_corn_info)

def movies_ask_group(movies): #for group switch #it only asks for the movie title
    while True:    
        n_movie=input("\nWhat is the name of the movie you want to watch? ")

        if not valid_movie_checker(movies, n_movie):
            while True:
                i = input("\nSorry, we could not find that movie. Enter Y to try again or N to quit. ")
                if i.upper()=="N":
                    print("\nBye.")
                    exit()
                elif i.upper() == 'Y':
                    break  
        else:
            # if user type valid movie title...
            valid_n_movie = n_movie
            break
    return (valid_n_movie)
    

def order_popcorn(): #book switch
    while True:
        i = input("\nWould you like to order popcorn? Y/N ")
        if i.upper() == "N" or i.upper() == "Y":
            break
    if i.upper() == "Y":
        while True:
            i_size = input("You want popcorn. What size Small, Medium or Large? (S/M/L) ")
            if i_size.upper() == "S" or i_size.upper() == "M" or i_size.upper() == "L":
                return i_size.upper()
                
    else:
        return None
  
def order_popcorn_group(num_ppl,j): #group switch
    while j<=num_ppl:
        i = input("For person {}, would you like to order popcorn? Y/N ".format(j)) #print several times depends on the number of ppl.
        if i.upper() == "N" or i.upper() == "Y":
            break
    if i.upper() == "Y":
        while True:
            i_size = input("Person {} wants popcorn. What size Small, Medium or Large? (S/M/L) ".format(j))
            if i_size.upper() == "S" or i_size.upper() == "M" or i_size.upper() == "L":
                return i_size.upper()
                
    else:
        return None #put nothing once user dont want popcorn
        
        

#function will use popcorn_size_info = movie_info[1] ->size

      
def total_seat_calc(room_num): #available seat calculater by substituting the room number
    if room_num == 1:
        total_allowed_seat = 35
    elif room_num == 2:
        total_allowed_seat = 136
    else:
        total_allowed_seat = 42
    cnt = 0
    i = 1
    while i <= total_allowed_seat:
        cnt+=1
        i +=2 #considering the social distancing
    return cnt

def itemised_detail(valid_n_movie,movies, num_ppl,popcorn_size): #receipt 
    # if num_ppl is 1 then run only once but its not loop
    
    
    for i in range(len(movies)): #using title of movie, find the time
        if (movies[i]["title"]).upper() == valid_n_movie.upper():
            # (testing) movie_time = str(movies[i]["time"])
            # (testing) print("movie time is {}:{}.".format(movie_time[0:2],movie_time[2:4])) movie time check

            movie_time = (movies[i]["time"])
            # print(movie_time)
            
    if num_ppl == 1: # book switch
        cst_t = ticket_price(movie_time) #cst_t = cost of ticket
        cst_p = popcorn_price(popcorn_size) #cst_p = cost of popcorn
        
        total_cost = cst_t +cst_p
        print("\nFor 1 person, the initial cost is ${:.2f}".format(total_cost))
        
        if cst_t == 13.00:    
            print(" Person 1: Ticket before 16:00".ljust(35, ' ') + "$" + "{:.2f}".format(cst_t).rjust(5, ' '))
        else:
            print(" Person 1: Ticket from 16:00".ljust(35, ' ') + "$" + "{:.2f}".format(cst_t).rjust(5, ' '))
        
        if popcorn_size == "S":
            print(" Person 1: Small popcorn".ljust(35, ' ') + "$" + "{:.2f}".format(cst_p).rjust(5, ' '))
        elif popcorn_size == "M":
            print(" Person 1: Medium popcorn".ljust(35, ' ') + "$" + "{:.2f}".format(cst_p).rjust(5, ' '))
        elif popcorn_size == "L":
            print(" Person 1: Large popcorn".ljust(35, ' ') + "$" + "{:.2f}".format(cst_p).rjust(5, ' '))
        final_price = group_discount(total_cost, cst_t, popcorn_size, num_ppl) #!

    else: # group switch
        t_cst_t = num_ppl * ticket_price(movie_time) # total cost of ticket
        t_cst_p = 0 # total cost of popcorn
        
        for i in range(len(popcorn_size)):
            t_cst_p += popcorn_price(popcorn_size[i])
        total_cost = t_cst_t + t_cst_p
        
        print("\nFor {} persons, the initial cost is ${:.2f}".format(num_ppl, total_cost))
        
        for i in range(1, num_ppl+1):
            cst_t = ticket_price(movie_time)
            if cst_t == 13.00:
                print(" Person {}: Ticket before 16:00".format(i).ljust(34, ' ') + '$' + '{:.2f}'.format(cst_t).rjust(5, ' '))
                i-=1
                popcorn_receipt(popcorn_size,i)
            else:
                print(" Person {}: Ticket from 16:00".format(i).ljust(34, ' ') + '$' + '{:.2f}'.format(cst_t).rjust(5, ' '))
                i-=1
                popcorn_receipt(popcorn_size,i)
        final_price = group_discount(total_cost, cst_t, popcorn_size, num_ppl) #!
    
    payment(final_price)    
            
            ##function works (but sequence is not)
            
                
            #popcorn_price




def ticket_price(movie_time): #ticket prices depends on the time
    
    if movie_time < 1600:
        cost_ticket = 13.00
        # print(f"Ticket before 16:00: {cost_ticket}")
    else:
        cost_ticket = 15.00
        # print(f"Ticket from 16:00: {cost_ticket}")
    return cost_ticket

def popcorn_price(popcorn_size): #return to the price of popcorn depends on the size
    cost_popcorn = None
    if popcorn_size == "S":
        cost_popcorn = 3.50
    elif popcorn_size == "M":
        cost_popcorn = 5.00
    elif popcorn_size == "L":
        cost_popcorn =7.00
    elif popcorn_size == None:
        cost_popcorn = 0.00
    return cost_popcorn

def popcorn_receipt(popcorn_size, i): #print prompt of receipt
    
    # while i <= len(popcorn_size):
    #     # cst_p = popcorn_price(popcorn_size)
    if popcorn_size[i] == None:
        return None
        # break
    elif popcorn_size[i] == "S":
        print(" Person {}: Small popcorn".format(i+1).ljust(34, ' ') + '$' + '{:.2f}'.format(3.50).rjust(5, ' '))
        # break
    elif popcorn_size[i] == "M":
        print(" Person {}: Medium popcorn".format(i+1).ljust(34, ' ') + '$' + '{:.2f}'.format(5.00).rjust(5, ' '))
        # break
    elif popcorn_size[i] == "L":
        print(" Person {}: Large popcorn".format(i+1).ljust(34, ' ') + '$' + '{:.2f}'.format(7.00).rjust(5, ' '))
        # break
        
def group_discount(total_cost, cst_t, popcorn_size, num_ppl): #group discount for group switch
    if total_cost<=100: #dont need to divide the book n the group switch as the book switch would never exceed 100.
        print("") #new line
        print(" No discounts applied".ljust(34, ' ') + '$' + '{:.2f}'.format(0.00).rjust(5, ' ')) #!
        t_d_cst_t = 0
        t_d_cst_p = 0
    else:
        #group discount applied
        t_d_cst_t = 0 #total discounted cost of tickets
        t_d_cst_p = 0 #total discounted cost of popcorns
        
        cnt_p = 0 #count of popcorn
        
        
        
        
        for _ in range(num_ppl):
            d_cst_t = cst_t * 0.1
            t_d_cst_t += d_cst_t
            
        for i in range(len(popcorn_size)):
            if popcorn_size[i] == None:
                continue
            else:
                if popcorn_size[i] == "S":
                    cst_p = 3.50
                elif popcorn_size[i] == "M":
                    cst_p = 5.00
                elif popcorn_size[i] == "L":
                    cst_p = 7.00
                cnt_p +=1
                d_cst_p = cst_p * 0.2
                t_d_cst_p += d_cst_p
                
        print("") #new line
        
        print(" Discount applied tickets x{}".format(num_ppl).ljust(35, ' ') + '-$' + '{:.2f}'.format(t_d_cst_t).rjust(5, ' ')) #!
        print(" Discount applied popcorn x{}".format(cnt_p).ljust(35, ' ') + '-$' + '{:.2f}'.format(t_d_cst_p).rjust(5, ' ')) #!
    final_price = total_cost-t_d_cst_t-t_d_cst_p
    print("\nThe final price is ".ljust(35, ' ') + '$' + '{:.2f}'.format(final_price).rjust(5, ' ')) #!
    return final_price

def payment(final_price): #payment process
    #user input
    #find the remainder 
    #seperate remaining cost.
    print("")
    while True:
        user_pay = float(input("Enter the amount paid: $"))
        if not payment_check(user_pay, final_price):
            continue
        
        change = user_pay - final_price
        print("Change: ${:.2f}".format(change))
        break
    change_cnt(change)
    
    print("\nBye.")
    exit()
        
        
            
        

def payment_check(user_pay, final_price): #check if payment is valid
    int_user_pay = int(user_pay)
    cents = int((user_pay*1000.0 - int_user_pay*1000.0)) // 10 #because of approximation, multipled 1000 and divided 10 and make cents as integer
    

    if cents % 5 != 0:
        print("The input given is not divisible by 5c. Enter a valid payment.")
        return False
    change = user_pay - final_price
    if change < 0:
        print("The user is ${:.2f} short. Ask the user to pay the correct amount.".format(final_price-user_pay))
        return False
    return True

def change_cnt(change): #change count #count of changes
    key_list = [100, 50, 20, 10, 5, 2, 1]
    #dollars
    change_dict = {}
    change_dict[100]= None
    change_dict[50] = None
    change_dict[20] = None
    change_dict[10] = None
    change_dict[5]  = None
    change_dict[2]  = None
    change_dict[1]  = None

    cent_key_list = [50, 20, 10, 5]
    #cents
    change_cent_dict = {}
    change_cent_dict[50] = None
    change_cent_dict[20] = None
    change_cent_dict[10] = None
    change_cent_dict[5] = None
    paper_money = int(change)
    cent = int((change*1000.0 - paper_money*1000.0)) //10
    for key in key_list:
        change_dict[key] = int(change // key)
        
        change -= change_dict[key] * key

    for key in cent_key_list:
        change_cent_dict[key] = cent // key
        
        cent -= change_cent_dict[key] * key

    for key in key_list:
        if change_dict[key] != 0:
            print(" $" + "{}".format(key).rjust(2, " ") + ": {}".format(change_dict[key])) #print dollar quantities
    for key in cent_key_list:
        if change_cent_dict[key] != 0:
            print(" {}c: {}".format(key, change_cent_dict[key])) #print cents quantities




def main():
    if len(sys.argv) >=2:
        user_input = sys.argv[1]
    
    else:
        if len(sys.argv) == 1:
            intro_greet()
            print("\nUsage: python3 pizzaz.py [ --show <timenow> | --book | --group ]")
            exit()
        intro_greet()
        invalid_switch_input()
    movies = collection()

    if user_input == "--show":  # show
        
        if len(sys.argv) == 3:
            #need to consider the sys.argv[2] is numeric.
            
            if ":" in sys.argv[2]: #sys.argv[2].isnumeric() or 
                time=sys.argv[2]
                if not time[0].isnumeric():
                    intro_greet()
                    invalid_time_input()
                elif time[2] != ":":
                    intro_greet()
                    invalid_time_input()
                elif len(time) != 5:
                    intro_greet()
                    invalid_time_input()
                elif int(time[0] + time[1]) >= 24 or int(time[0] + time[1]) < 0:
                    intro_greet()
                    invalid_time_input()
                elif int(time[3] + time[4]) >=60 or int(time[3] + time[4]) < 0:
                    intro_greet()
                    invalid_time_input()
                
                       
            else:
                intro_greet()
                invalid_time_input() 
        else:
            intro_greet()
            invalid_switch_input()     
        intro_greet()
        print("")
        movie_after_time(movies, time)
    
    
    
    elif user_input == "--book":    # book
        intro_greet()
        if len(sys.argv) != 2:
            invalid_switch_input()
            
        # movies_popcorn_ask(movies) # if seat_num_manage function valid this will be useless
        seat_num_manage(movies)
        

        
    elif user_input == "--group":   # group
        intro_greet()
        if len(sys.argv) != 2:
            invalid_switch_input()
        seat_num_manage(movies)
        
        # seat_num_create()
        
        
        
    
    else:
        intro_greet()
        invalid_switch_input()
    
if __name__ == '__main__':
    main()

