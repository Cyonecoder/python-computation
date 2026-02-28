import csv

fieldnames = [
    "Email",
    "Last name",
    "First name",
    "Problem 1 score",
    "Problem 1 comments",
    "Problem 2 score",
    "Problem 2 comments",
    "Problem 3 score",
    "Problem 3 comments",
]


def main():
    reader = file_open_read("exam.csv")
    # for line in file_open_read():
    #     print(line)
    for row in reader:
        print(row)


def file_open_read(filename):
    with open(filename, newline="") as file:
        lines = csv.DictReader(file, fieldnames=fieldnames)

        return list(lines)


if __name__ == "__main__":
    main()
