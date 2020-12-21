# Author: DevHyperCoder
# Email: arduinoleo88@gmail.com

from bs4 import BeautifulSoup
from os import path

# VARIABLES
MAIN_DIR = ""
HTML_FILE = ""
CSS_LINK_FILE = ""
JS_LINK_FILE = ""


def main():
    print('Link Extractor')

    if not MAIN_DIR or not HTML_FILE or not CSS_LINK_FILE or not JS_LINK_FILE:
        print("Please edit the script and put correct values :)\nExiting")
        print(path.expanduser(path.join(MAIN_DIR,HTML_FILE)))
        exit()

    file_path = path.expanduser(path.join(MAIN_DIR,HTML_FILE))
    file = open(file_path)
    page_content = file.read()

    soup = BeautifulSoup(page_content)

    css_link_path = path.expanduser(path.join(MAIN_DIR,CSS_LINK_FILE))
    css_link_file = open(css_link_path, "w+")
    for link in soup.find_all('link'):
        print(link.get('href'))
        css_link_file.write(link.get('href') + '\n')
    css_link_file.close()

    js_link_path = path.expanduser(path.join(MAIN_DIR,JS_LINK_FILE))
    js_link_file = open(js_link_path, "w+")
    for link in soup.find_all('script'):
        print(link.get('src'))
        js_link_file.write(link.get('src') + '\n')
    js_link_file.close()


if __name__ == '__main__':
    main()
