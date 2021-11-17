import re


def get_emails(filepath):
    #finish this
    emails = []
    allEmails = []
    with open(filepath, 'r') as myFile:
        txtFile = myFile.readlines()
        for line in txtFile:
            email = re.findall(r'\w+@([\w\-.]+)', line)
            emails.append(email)
    for email in emails:
        for string in email:
            allEmails.append(string)
    return allEmails


def compare_emails(emailsOpened, emailsClicked):
    value_dic = {}
    notClickedEmails = []
    for email in emailsOpened:
        if email not in emailsClicked:
            notClickedEmails.append(email)
    return notClickedEmails

def main():
    emailsOpened = get_emails("Gale30DayOpened.txt") #change this file name
    emailsClicked = get_emails("Gale30DayClicked.txt") #change this file name
    non_clickers = compare_emails(emailsOpened, emailsClicked)
    print(non_clickers)


if __name__ == "__main__":
    main()
