import csv
import smtplib

lookup = {}
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
    print(lookup)
    reader = file_open_read("exam.csv")
    # for line in file_open_read():
    #     print(line)

    print(lookup)
    for key, value in lookup.items():
        print(key, value["Last name"], value["First name"])
        smtpsend(
            key,
            f"{value['Last name']} {value['First name']}",
        )


def smtpsend(email_reciever: str, name: str = "defaultName"):
    from_addr = "khaal.moham1@ifjabalial.com"
    msg = f"Hello {name}"
    server = smtplib.SMTP("localhost", port=1025)
    server.set_debuglevel(1)
    server.sendmail(from_addr, email_reciever, msg)
    server.quit()


def file_open_read(filename):
    with open(filename, newline="") as file:
        rows = csv.DictReader(file, fieldnames=fieldnames)
        for row in rows:
            lookup[row["Email"]] = {
                "First name": row["First name"],
                "Last name": row["Last name"],
                "socres": [
                    row["Problem 1 score"],
                    row["Problem 2 score"],
                    [row["Problem 3 score"]],
                ],
                "comments": [
                    row["Problem 1 comments"],
                    row["Problem 2 comments"],
                    [row["Problem 3 comments"]],
                ],
            }
        return lookup


if __name__ == "__main__":
    main()
