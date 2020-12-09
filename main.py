from Database import DBManager

def mainMenu():

    #menu options, dictionary
    mainMenuList = {}
    mainMenuList[''] = '\n========[MAIN MENU]========'
    mainMenuList['A'] = 'View Existing Properties'
    mainMenuList['B'] = 'Add New Property'
    mainMenuList['C'] = 'New Transaction'
    mainMenuList['D'] = 'View Transaction History'
    mainMenuList['E'] = 'Exit'

    menuOptions = mainMenuList.keys()
    menuValues = mainMenuList.values()
    sorted(menuOptions)
    print(menuOptions)

    menuKeys = []
    for options in menuOptions:
        menuKeys.append(options)

    while True:

        for options in menuOptions:
            print(options, mainMenuList[options])

        userInput = input('\nSelect an option from the Main Menu: ')

        if userInput == menuKeys[1]:
            #this is to view existing properties, not setting code to parse through the database table yet
            pass

        elif userInput == menuKeys[2]:
            newaddress = input('Enter the new property\'s address: ')
            PID = input('Enter the appropriate Property ID for {0}: '.format(newaddress))
            menuManager.addProperties(PID, newaddress)
            #may need to add way to parse through existing pidTable to check if property address already exists
            #if property already exists, auto prompt an error that it's there

        elif userInput == menuKeys[3]:
            #placeholder for new transaction
            pass

        elif userInput == menuKeys[4]:
            #placeholder for viewing all existing transaction
            pass

        elif userInput == menuKeys[5]:
            #exiting the program
            print('Exiting...')
            break




menuManager = DBManager()
if menuManager.setUpDB():
    mainMenu()