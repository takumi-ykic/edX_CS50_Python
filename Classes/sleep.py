def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    # flock = []
    # for i in range(n):
    #     flock.append("Sheep" * i)
    # return flock

    for i in range(n):
        yield "sheep" * i

if __name__ == "__main__":
    main()
