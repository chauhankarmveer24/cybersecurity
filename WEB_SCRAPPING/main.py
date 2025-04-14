from bs4 import BeautifulSoup

with open() as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    tag = soup.find_all('h5')
    print(tag)