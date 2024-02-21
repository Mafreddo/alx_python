for x in range(100):
    if x < 99:
        print(f"{i:02d}", end=", " if i < 99 else "\n")
    else :
        print('{:02d}'.format(x))