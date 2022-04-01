# imports
from rich import print

while True:
    # taking seconds by input()
    while True:
        try:
            seconds = int(input("Seconds: "))
            break
        except:
            print("[bold red]It isn't a number!")

    # calculating
    # if the number of seconds is less than a minute
    if seconds < 60:
        print(f"[italic yellow]{seconds} second(s).")

    # if the number of seconds is less than a hour
    elif seconds < 3600:
        minutes = seconds // 60
        seconds -= (minutes * 60)
        print(f"[italic cyan]{minutes} minute(s) [italic yellow]{seconds} second(s)." if seconds != 0 else f"[italic cyan]{minutes} minute(s).")
    
    # if the number of seconds is greater than a hour
    elif seconds >= 3600:
        hours = seconds // 60 // 60
        minutes = (seconds - (hours * 60 * 60)) // 60
        seconds = seconds - ((hours * 60 * 60) + (minutes * 60))
        if seconds != 0 and minutes != 0: print(f"[italic red]{hours} hour(s) [italic cyan]{minutes} minute(s) [italic yellow]{seconds} second(s).")
        elif seconds == 0 and minutes == 0: print(f"[italic red]{hours} hour(s).")
        elif seconds == 0: print(f"[italic red]{hours} hour(s) [italic cyan]{minutes} minute(s).")
        elif minutes == 0: print(f"[italic red]{hours} hour(s) [italic yellow]{seconds} second(s).")
