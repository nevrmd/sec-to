while True:
    secs = int(input("Seconds: "))
    print(f"{secs//3600} hours {(secs % 3600) // 60} minutes {secs % 60} seconds")