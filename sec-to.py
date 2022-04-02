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
    hours = seconds // 60 // 60
    minutes = (seconds - (hours * 60 * 60)) // 60
    seconds = seconds - ((hours * 60 * 60) + (minutes * 60))

    # conditions
    if seconds != 0 and minutes != 0 and hours != 0:
        print(f"[italic red]{hours} hour(s) [italic cyan]{minutes} minute(s) [italic yellow]{seconds} second(s).")

    elif seconds == 0 and minutes == 0:
        print(f"[italic red]{hours} hour(s).")

    elif hours == 0 and minutes == 0:
        print(f"[italic yellow]{seconds} second(s).")

    elif hours == 0 and seconds == 0:
        print(f"[italic cyan]{minutes} minute(s).")

    elif seconds == 0:
        print(f"[italic red]{hours} hour(s) [italic cyan]{minutes} minute(s).")

    elif minutes == 0:
        print(f"[italic red]{hours} hour(s) [italic yellow]{seconds} second(s).")

    elif hours == 0:
        print(f"[italic cyan]{minutes} minute(s) [italic yellow]{seconds} second(s).")
