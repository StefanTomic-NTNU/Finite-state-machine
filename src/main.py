from kpc import KPC


def main():
    kpc = KPC("password.txt")
    kpc.do_polling()


# The main function may not be called on an OS other than Windows
if __name__ == "__main__":
    main()
