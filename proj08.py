##############################################################
    #  Computer Project #8
    #
    #  Open file function
    #   Takes input for what file
    #       Try/ except to see if file opens
    #           returns file and returns cities
    #  Read file function
    #   Iterate through csv file
    #       Assign varibles to value in file, make it a list,int or a string
    #   Append tuple to list
    #   Add list to dictionary
    #   return dictionary
    #  Read file discount function
    #   Iterate through csv file
    #       Assign varible to value in file
    #   Add value to dictionary
    #   return dictionary
    #  In year function
    #   Iterate through dictionary
    #   returns the list of games that year
    #  by genre function
    #   Iterate through dictionary
    #   returns the list of games in that genre
    #  by dev function
    #   Iterate through dictionary
    #   returns the list of games in by that developer 
    #  per discount function
    #   Iterate through both dictionaries
    #       See what game is in both
    #   returns the list of calculated prices
    #  by dev by year function
    #   Iterate through both dictionaries
    #       see what game is in both and sort by price
    #   returns the list of games by that developer and in that year
    #  by genre no disc function
    #   Use prevoiusly defined genre function to get names of games
    #   Iterate through dictonary
    #       When game is not in dictionary sort by price
    #   return list of games in a genre sorted by price
    #  by dev with disc function
    #   Use prevoiusly defined dev function to get names of games
    #   Iterate through dictonary
    #       When game is in dictionary sort by price
    #   return list of games by a developer sorted by price
    #  Main function
    #   Define menu options 
    #   If statement for error message
    #       print error statement and menu options
    #   Intiate while loop for when the option is not 7
    #       Initiate if loop for every option
    #           Call necessay functions to the main function in each option
    #           Print statemnets for options
    #           Print menu options 
    #    Display closing message
##############################################################

import csv
from operator import itemgetter


MENU = '''\nSelect from the option: 
        1.Games in a certain year 
        2. Games by a Developer 
        3. Games of a Genre 
        4. Games by a developer in a year 
        5. Games of a Genre with no discount 
        6. Games by a developer with discount 
        7. Exit 
        Option: '''
        
def open_file(s):
    """
    Checks for if file user inputted is a vaild file

    Parameters
    ----------
    s : str
        The file name the user inputs.

    Returns
    -------
    File pointer
        The file that open is returned and opened.

    """
    while 1==1:
        file = input('\nEnter {} file: '.format(s))
        try:
            #looks to see if the file can open 
            data_fp = open(file, encoding="utf-8")
            return data_fp
        except:
            #if the file is not found return the function to reask for file
            print('\nNo Such file')
            return open_file(s)

def read_file(fp_games):
    """
    Reads the file and assigns a value to a varible

    Parameters
    ----------
    fp_games : File
        The file that all the values are assigned from.

    Returns
    -------
    read_dict : Dict
        A dict with a list that contains all of the varibles.

    """
    read_dict = {}
    reader = csv.reader(fp_games)
    next(reader)
    #iterate through each line in file 
    for line in reader:
        support = []
        modes = 0
        list_of_data = []
        #Decalare varibles and assign to lines
        name = str(line[0])
        date = str(line[1])
        dev = line[2].split(";")
        genres = line[3].split(";")
        player_modes = line[4].split(";")
        mode = player_modes[0].lower()
        #See if multi-player is in the modes
        #Convert price from rupees to dollar
        if "multi-player" in mode:
            modes = 0
        else:
            modes = 1
        price = line[5].replace(",","")
        try:
            price = float(price)
            price = price*0.012
        except:
            price = 0.0
        over_reviews = str(line[6])
        reviews = int(line[7])
        positive = int(line[8].replace("%",""))
        #Change number to type of support
        windows = line[9]
        if windows == "1":
            support.append("win_support")
        mac = line[10]
        if mac == "1":
            support.append("mac_support")
        lin = line[11]
        if lin == "1":
            support.append("lin_support")
        
        #Create a list and add it to the dictionary
        list_of_data = [date,dev,genres,modes,price,over_reviews,reviews,positive,support]
        read_dict[name]=list_of_data
    return read_dict
        
def read_discount(fp_discount):
    """
    Takes the data from dicount file and rounds values

    Parameters
    ----------
    fp_discount : file
        The file that contains all the data.

    Returns
    -------
    Discount_dict : Dict
        A dictionary that contains the value associated with it.

    """
    #Iterate through the file
    Discount_dict = {}
    reader = csv.reader(fp_discount)
    next(reader)
    for line in reader:
        #Rounds the value
        name = line[0]
        discount = line[1]
        discount = float(discount)
        discount = round(discount,2)
        Discount_dict[name] = discount
    return Discount_dict

def in_year(master_D,year):
    """
    Finds the game that are made in the same year that the year was inputted

    Parameters
    ----------
    master_D : Dict
        The dictionary that all the data is being pulled from.
    year : int
        The year that the user inputted.

    Returns
    -------
    year_list : list
        A list that contains all the games that were made in the inputted year.

    """
    year_list = []
    #Iterate through the dictionary
    #Check if year is the same year as year inputted
    for key, List in master_D.items():
        date = List[0].split("/")
        year1 = int(date[2])
        if year1 == year:
            year_list.append(key)
        year_list = sorted(year_list)
    return year_list

def by_genre(master_D,genre): 
    """
    Looks through list and gives back games with genre inputted

    Parameters
    ----------
    master_D : Dict
        The dictionary that all the data is being pulled from.
    genre : str
        The genre to search for in data.

    Returns
    -------
    genre_list_new : List
        List of game names returned with genre search for.
    """
    genre_list = []
    precent_list = []
    genre_list_new = []
    #Iterate through the dictionary
    #Check if genre is the same genre as genre inputted
    #Sort the list by creating tuple and sort
    for key, List in master_D.items():
        game_genre = List[2]
        if genre in game_genre:
            precent = int(List[7])
            precent_list.append(precent)
            name_precent = (key,precent)
            genre_list.append(name_precent)
        genre_list = sorted(genre_list, key = itemgetter(1), reverse = True)
    #Remove precent from tuple and make new list
    for tuplex in genre_list:
        genrenew = tuplex[0]
        genre_list_new.append(genrenew)
        
    return genre_list_new
        
def by_dev(master_D,developer): 
    """
    Looks through list and gives back games with developer inputted

    Parameters
    ----------
    master_D : Dict
        The dictionary that all the data is being pulled from.
    developer : str
        A name of a developer to search through data.

    Returns
    -------
    dev_list_new : List
        The list returned sorted by year and with the same developer.

    """
    dev_list = []
    year_list = []
    dev_list_new = []
    #Iterate through the dictionary
    #Check if dev is the same dev as dev inputted
    #Sort the list by creating tuple and sort
    for key, List in master_D.items():
        dev_genre = List[1]
        if developer in dev_genre:
            year = (List[0].split("/"))
            year = int(year[2])
            year_list.append(year)
            name_year = (key,year)
            dev_list.append(name_year)
        dev_list = sorted(dev_list, key = itemgetter(1), reverse = True)
    #Remove year from tuple and make new list
    for tuplex in dev_list:
        devnew = tuplex[0]
        dev_list_new.append(devnew)
        
    return dev_list_new

def per_discount(master_D,games,discount_D): 
    """
    A function that returns the discounted price

    Parameters
    ----------
    master_D : Dict
        The dictionary that all the data is being pulled from.
    games : Dict
        The list of games searching for.
    discount_D : Dict
        The dictionary with the disocounted values.

    Returns
    -------
    discount_per : List
        A list of the dicounted prices.

    """
    #Iterate through each list and dictionary
    #if the games match up then calculate discounted price, if not use orginal price
    discount_per = []
    for name in games:
        for key, List in master_D.items():
            if key == name:
                price = float(List[4])
                for game, value in discount_D.items():
                    if name == game:
                        d_prices = 0
                        discount_price = value
                        #Math for the price
                        d_prices = (1-(discount_price/100))*price
                        if d_prices not in discount_per:
                            d_prices = round(d_prices, 6)
                            discount_per.append(d_prices)
                        break
                #Used to see if the game is not in discounted dictionary
                else:
                    if price not in discount_per:
                        discount_per.append(price)
    return discount_per
            

def by_dev_year(master_D, discount_D, developer, year):
    """
    This takes in a game developer and year and sorts in by price

    Parameters
    ----------
    master_D : Dict
        The dictionary that all the data is being pulled from.
    discount_D : Dict
        The dictionary with the disocounted values.
    developer : str
        Name of developer to search for.
    year : int
        The year inputted so search for.

    Returns
    -------
    dev_list_year_new : List
        The sorted list of game names.

    """
    dev_list_year = []
    dev_list_year_new = []
    #iterate through the master list
    #Check to see if devolper and year inputted is the same
    for key, List in master_D.items():
        dev = List[1]
        year1 = (List[0].split("/"))
        year1 = int(year1[2])
        if developer in dev and year1 == year:
            #Call price discount function to get prices
            #Create tuple with associated name and price and sort
            price_list = per_discount(master_D, [key], discount_D)
            price = price_list[0]
            name_price = (key, price)
            if name_price not in dev_list_year:
                dev_list_year.append(name_price)
                
    dev_list_year = sorted(dev_list_year, key=itemgetter(1))
    #remove price from list
    for tuplex in dev_list_year:
        devnew = tuplex[0]
        dev_list_year_new.append(devnew)
    return dev_list_year_new


def by_genre_no_disc(master_D,discount_D,genre):
    """
    Sorts genre with no discount returns the games

    Parameters
    ----------
    master_D : Dict
        The dictionary that all the data is being pulled from.
    discount_D : Dict
        The dictionary with the disocounted values.
    genre : str
        Genre to search for.

    Returns
    -------
    list_genre_new : List
        the list of sorted games by genre and price returned.

    """
    genre_list_new = by_genre(master_D, genre)
    list_genre = []
    list_genre_new = []
    #Iterate through the names in genre list
    #if name does not exist in discount dict
    #then sort by price
    for name in genre_list_new:
        if name not in discount_D.keys():
            price = float(master_D[name][4])
            name_price = (name, price)
            if name_price not in list_genre:
                list_genre.append(name_price)
    list_genre = sorted(list_genre, key=itemgetter(1))

    #Removes price from list
    for tuplex in list_genre:
        gennew = tuplex[0]
        if gennew not in list_genre_new:
            list_genre_new.append(gennew)
    return list_genre_new

def by_dev_with_disc(master_D,discount_D,developer):
    """
    Sorts developer with discount returns the games

    Parameters
    ----------
    master_D : Dict
        The dictionary that all the data is being pulled from.
    discount_D : Dict
        The dictionary with the disocounted values.
    developer : str
        The developer to search for in file.

    Returns
    -------
    dev_with_disc_new : List
        the list of sorted games by developer and price returned.

    """
    dev_with_disc = []
    dev_with_disc_new = []
    dev_list_new = by_dev(master_D, developer)
    #Iterate through the names in developer list
    #if name does not exist in discount dict
    #then sort by price
    for name in dev_list_new:
        if name in discount_D.keys():
            price = float(master_D[name][4])
            name_price = (name,price)
            dev_with_disc.append(name_price)
        dev_with_disc = sorted(dev_with_disc, key=itemgetter(1))
    #Remove price from list
    for tuplex in dev_with_disc:
        devnew = tuplex[0]
        if devnew not in dev_with_disc_new:
            dev_with_disc_new.append(devnew)
    return dev_with_disc_new

def main():
    """
    The user imputs option and prints respective option    

    Returns
    -------
    None.

    """
    #Call all necessary functions to begin(both read files and open file)
    games_fp = open_file("games")
    discount_fp = open_file("discount")
    option = input(MENU)
    codes = ("1","2","3","4","5","6","7")
    read_dict = read_file(games_fp)
    Discount_dict = read_discount(discount_fp)
    
    #While option is not equal to exit number
    #Error checks and calls a function for each option
    while option != "7":
        #Error checking
        if option not in codes:
            print("\nInvalid option")
            option = input(MENU)
        if option == "1":
            #Error checking for year
            year = (input('\nWhich year: '))
            while True:
                try:
                    year = int(year)
                    break
                except:
                    #print statements
                    print("\nPlease enter a valid year")
                    year = (input('\nWhich year: '))
                    continue
            #Call function in each option
            year_list = in_year(read_dict, year)
            #Error checking to see if list is empoty
            if len(year_list)==0:
                print("\nNothing to print")
            else:
                print("\nGames released in {}:".format(year))
                print(", ".join(year_list))
            option = input(MENU)
            
        if option == "2":
            developer = (input('\nWhich developer: '))
            dev_list = by_dev(read_dict, developer)
            
            if len(dev_list)==0:
                print("\nNothing to print")
            else:
                print("\nGames made by {}:".format(developer))
                print(", ".join(dev_list))
            option = input(MENU)
            
        if option == "3":
            genre = (input('\nWhich genre: '))
            genre_list = by_genre(read_dict, genre)
            if len(genre_list)==0:
                print("\nNothing to print")
            else:
                print("\nGames with {} genre:".format(genre))
                print(", ".join(genre_list))
            option = input(MENU)
        
        if option == "4":
            developer = (input('\nWhich developer: '))
            year = (input('\nWhich year: '))
            while True:
                try:
                    year = int(year)
                    break
                except:
                    print("\nPlease enter a valid year")
                    year = (input('\nWhich year: '))
                    continue
                
            by_year_dev = by_dev_year(read_dict, Discount_dict, developer, year)
            if len(by_year_dev)==0:
                print("\nNothing to print")
            else:
                print("\nGames made by {} and released in {}:".format(developer, year))
                print(", ".join(by_year_dev))
            option = input(MENU)
            
        if option == "5":
            genre = (input('\nWhich genre: '      ))
            genre_list = by_genre_no_disc(read_dict, Discount_dict, genre)
            if len(genre_list)==0:
                print("\nNothing to print")
            else:
                print("\nGames with {} genre and without a discount:".format(genre))
                print(", ".join(genre_list))
            option = input(MENU)
        
        if option == "6":
            developer = (input('\nWhich developer: '))
            dev_list = by_dev_with_disc(read_dict, Discount_dict, developer)
            if len(dev_list)==0:
                print("\nNothing to print")
            else:
                print("\nGames made by {} which offer discount:".format(developer))
                print(", ".join(dev_list))
            option = input(MENU)
    #Closing message    
    print("\nThank you.")

if __name__ == "__main__":
    main()