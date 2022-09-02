# Attendance tracker


def attendanceTracker(inputString):
    abs, late = 0, 0

    for i in range(len(inputString)):
        if inputString[i] == 'A':
            abs += 1
        if inputString[i] == 'L':
            if (i > 0 and inputString[i-1] == 'L'):
                late += 1
            else:
                late = 1

    if (abs > 2 or late >= 3):
        return "False"
    else:
        return "True"


if __name__ == "__main__":
    inputString = input("Enter a attendance String:- ")
    print(attendanceTracker(inputString))