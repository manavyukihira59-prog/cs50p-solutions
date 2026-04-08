def main():
    time = input("enter: ")
    t = convert(time)

    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")
    else:
        print("Not a valid time")


def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60

main()