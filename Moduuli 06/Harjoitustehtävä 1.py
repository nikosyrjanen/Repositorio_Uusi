import random

def heita_noppa():
    return random.randint(1,6)

def main():
    silmaluku = 0
    while silmaluku !=6:
        silmaluku = heita_noppa()
        print(silmaluku)

if __name__ == "__main__":
    main()