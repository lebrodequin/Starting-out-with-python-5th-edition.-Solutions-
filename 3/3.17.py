print ('Reboot the computer and try to connect.')
yes_or_no = input ('Did that fix the problem? ')
if yes_or_no == 'no': 
    print ('Reboot the router and try to connect.')
    yes_or_no = input ('Did that fix the problem? ')
    if yes_or_no == 'no': 
        print ('Make sure the cables between the router and modem are plugged in firmly.')
        yes_or_no = input ('Did that fix the problem? ')
        if yes_or_no == 'no': 
            print ('Move the router to a new location.')
            yes_or_no = input ('Did that fix the problem? ')
            if yes_or_no == 'no': 
                print ('Get a new router.')