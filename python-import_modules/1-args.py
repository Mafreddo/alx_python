import sys
if __name__ == "__main__":
    """Demonstrate the usage of the add function."""
    argv = sys.argv[1:]
    n_args = len(argv)
    if n_args == 0:
        print("0 arguments.")
    elif n_args == 1:
        print("1 argument:")
        print("1: {}".format(argv[0]))
    else:
        print("{} arguments:".format(n_args))
        for i, arg in enumerate(argv):
            print("{}: {}".format(i+1, arg))
