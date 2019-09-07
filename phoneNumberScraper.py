import requests, bs4, os, sys

def facebookLogin(email, pwd):
    headers = {
        'host':'m.facebook.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0/8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive'
    }

    session = requests.Session();
    r = session.get('https://m.facebook.com', headers=headers, allow_redirects=False)
    bs = bs4.BeautifulSoup(r.text, "html.parser")
    f = open('temp.html', 'w')
    f.write(bs.prettify())
    f.close()
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    action_url = soup.find('form', id='login_form')['action']
    inputs = soup.find('form', id='login_form').findAll('input', {'type': ['hidden', 'submit']})
    post_data = {input.get('name'): input.get('value') for input in inputs}
    post_data['email'] = email
    post_data['pass'] = pwd.upper()
    z = session.post(action_url, data=post_data, headers=headers, allow_redirects=True)
    


myLinkFile = open(sys.argv[1])
myProfileLinks = myLinkFile.readlines()
myLinkFile.close()
myNumFile = open(sys.argv[2], 'a')
for i in range(len(myProfileLinks)):
    if myProfileLinks[i][-1] == '\n':
        myProfileLinks[i] = myProfileLinks[i][0:-1]
    
    myPage = request.get(myProfileLinks[i])

    try:
        myPage.raise_for_status()
        print('getting phone number')
    except Exception as exc:
        print('There was a problem: %s' % (exc))

    myBS = bs4.BeautifulSoup(myPage.text)
    myElements = myBS.select('div > span')
    for x in range(len(myElements)):
        temp = myElements[x].getText()
        if temp[0] == '0' && temp[1] == '1':
            myNumFile.write(myElements[x] + '\n')
        #if ends here
    #nested for ends here
#parent for ends here
myNumFile.close()
