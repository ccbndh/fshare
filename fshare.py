from urlparse import urljoin
from bs4 import BeautifulSoup
import requests

url = 'https://www.fshare.vn/login/'
username = 'share@linksvip.net'
password = '18065226f'

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

headers = { 'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.10 Safari/537.36',
                    'referer': url }


response = session.post(url, data=data, headers=headers)
response = session.get('https://www.fshare.vn/file/FFNQHWVDW6VN/', allow_redirects=False, timeout=(0.1, 10.0))


if response.headers['location']:
	print response.headers['location']
else:
	print '403'
# print soup

