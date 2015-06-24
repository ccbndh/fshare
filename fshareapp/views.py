from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

url = 'https://www.fshare.vn/login/'
username = 'share@linksvip.net'
password = '18065226f'


def index(request):

    session = requests.Session()

    # getting csrf value

    response = session.get(url)
    soup = BeautifulSoup(response.content)

    form = soup.form
    csrf = form.find('input', attrs={'name': 'fs_csrf'}).get('value')

    # logging in
    data = {
        'LoginForm[email]': username,
        'LoginForm[password]': password,
        'fs_csrf': csrf
    }

    headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.10 Safari/537.36',
    'referer': url}



    res = ''
    try:
        response = session.post(url, data=data, headers=headers)
        response = session.get(request.POST['url'], allow_redirects=False, timeout=(1.0, 10.0))
        res = response.headers['location']
    except:
        res = "Can't get link"


    return render(request, "index.html", {
        'res': res,
    })