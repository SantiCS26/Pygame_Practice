from colorama import Fore, Style

name = (input (Fore.LIGHTYELLOW_EX + "Hello and welcome to \"An Ordinary Day at School\", what would you like to be reffered as throughout the journey that awaits you?\n" + Fore.LIGHTMAGENTA_EX))

#Lists all of the rules and tips for the game
print ("\n" + Fore.LIGHTBLUE_EX + "Hello " + name + ", and welcome to \"An Ordinary Day at School\"!\n" + Fore.LIGHTCYAN_EX + "\nInstructions/Tips:\n-Type \"Inventory\" or \"I\" to check your inventory\n-Descisions affect your reputation which can limit what options are available to you\n-There is a health and PVE system, be sure to not let your health drop\n-Food heals health")
print (Fore.LIGHTRED_EX + "\n-Make sure you enter the number of whatever answer you choose")