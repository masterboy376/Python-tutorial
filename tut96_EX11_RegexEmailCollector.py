string = "sdoisg gisgj8t34 4 dg 4n  @ igsg igg igdghnpodf jh gkgni dg44koimfjsf@dghs.fg sufgsgkg djkdjs 3dsgfh@g4g.com"

def emailCollector(s):
    import re 
    emails = re.findall(r'[0-9a-zA-Z%.]+@[0-9a-zA-Z%.]+[.][0-9a-zA-Z.]+', s)
    print(emails)
    with open('email.txt', 'r+') as f:
        for email in emails:
            f.write(str(email)+'\n')

emailCollector(string)