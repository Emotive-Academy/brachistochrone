import sys

def main():
    if sys.argv[1:]:
        print("Hello, {}!".format(sys.argv[1]))
    else:
        print("Hello, world!")

if __name__ == "__main__":
    main()
