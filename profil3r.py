import sys
from itertools import chain, combinations
from profil3r import core
from profil3r.colors import Colors
from multiprocessing import Process

CONFIG = './config.json'

def print_logo():
    print(Colors.OKGREEN + Colors.BOLD + '''___            ___  _  _  ____     
| . \ _ _  ___ | | '<_>| |<__ / _ _ 
|  _/| '_>/ . \| |- | || | <_ \| '_>
|_|  |_|  \___/|_|  |_||_|<___/|_|  

    ''' + Colors.ENDC)

    print("v1.0.1\n")
    print("You can buy me a coffee at : https://www.buymeacoffee.com/givocefo\n")


# Start the program
if __name__ == "__main__":
    print_logo()

    result = {}

    profil3r = core.Core(CONFIG, sys.argv[1:])
    profil3r.get_permutations()

    # Use command line arguments
    arguments = sys.argv[1:]

    # No argument
    if not len(arguments):
        print('''Profil3r is an OSINT tool that allows you to find potential profiles of a person on social networks, as well as their email addresses. This program also alerts you to the presence of a data leak for the found emails.

    Usage : ./main.py <arguments>
    for exemple : ./main.py john doe
                ./main.py john doe 67''')

    else:
        # Emails
        p1 = Process(target = profil3r.emails)
        p1.start()
        # Facebook
        p2 = Process(target = profil3r.facebook)
        p2.start()
        # TikTok
        p3 = Process(target = profil3r.tiktok)
        p3.start()
        # Twitter
        p4 = Process(target = profil3r.twitter)
        p4.start()