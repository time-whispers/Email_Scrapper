import re, urllib.request, time

emailRegex = re.compile(r'''(([a-zA-Z0-9_.+]+@[a-zA-Z0-9_.+]+))''', re.VERBOSE) #example: #something-.+_@somedomain.com

#Extracting Emails
def extractEmailsFromUrlText(urlText):
    extractedEmail = emailRegex.findall(urlText)
    allemails = []
    for email in extractedEmail:
        allemails.append(email[0])
    lenh = len(allemails)
    print("\t Number of Emails: %s\n"%lenh)
    seen = set()
    for email in allemails:
        if email not in seen: #faster than 'word not in output'
            seen.add(email)
            emailFile.write(email+"\n") #appending Emails to a filearea

#HTML Page Read Function
def htmlPageRead(url, i):
    try:
        start = time.time()
        headers = { 'User-Agent' : 'Mozilla/5.0' }
        request = urllib.request.Request(url, None, headers)
        response = urllib.request.urlopen(request)
        urlHtmlPageRead = response.read()
        urlText = urlHtmlPageRead.decode()
        print("%s.%s\t Fetched in: %s" % (i, url, (time.time() - start)))
        extractEmailsFromUrltext(urlText)
    except:
        pass

#Emails Leeching Function
def emailLeechFunc(url, i):
    try:
        htmlPageRead(url, i)
    except urllib.error.HTTPError as err:
        if err.code == 404:
            try:
                url = 'http://webcache.googleusercontent.com/search?q=cache:'+url
                htmlPageRead(url, i)
            except:
                pass
            else:
                pass

#TODO: Open a file for reading urls
start = time.time()
urlFile = open("urls.txt", 'r')
emailFile = open("emails.txt", 'a')
i = 0

#Iterate Opened File for getting Single Url
for urlLink in urlFile.readlines():
    urlLink = urlLink.strip('\'"')
    i = i+1
    emailLeechFunc(urlLink, i)
print("Elapsed Time: %s" % (time.time() - start))

urlFile.close()
emailFile.close()
    
