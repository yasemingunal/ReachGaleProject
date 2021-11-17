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
    print(notClickedEmails)
    return notClickedEmails


'''
    for email in notClickedEmails:
        value_dic[email] = value_dic.get(email, 0) + 1
    sortedDic = [(k, value_dic[k]) for k in value_dic]
    sortedDic.sort(key=lambda x: x[1], reverse=True)

'''
#print("SORTED DIC: ", sortedDic)


def main():
    emailsOpened = get_emails("Gale30DayOpened.txt")
    emailsClicked = get_emails("Gale30DayClicked.txt")
    non_clickers = compare_emails(emailsOpened, emailsClicked)


if __name__ == "__main__":
    main()