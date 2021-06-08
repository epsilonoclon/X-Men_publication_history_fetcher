import requests
from bs4 import BeautifulSoup

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def find_list():
	list_items = soup.find(class_="field field-name-field-pub-issues field-type-text-long field-label-above").find_all('li')
	for e in list_items:
		print(f"{bcolors.OKCYAN}   ",e.text,end='\n')
	print(f"{bcolors.ENDC}",'\n\n')

def find_events():
	list_items = soup.find(class_="field field-name-field-pub-events field-type-text-long field-label-above").find_all('li')
	for e in list_items:
		print(f"{bcolors.OKGREEN}   ",e.text,end='\n')
	print(f"{bcolors.ENDC}",'\n\n')

def find_appearance():
	list_items = soup.find(class_="view-content").find_all('td')
	for e in list_items:
		print(f"{bcolors.WARNING}",e.text,end='\n')
	print(f"{bcolors.ENDC}",'\n\n')


f = open("xmen.out", "r")
print(f"{bcolors.FAIL}",f.read(),f"{bcolors.ENDC}")
print("               Welcome to Cerebro",'\n', "Please Specify which year would you like to access: ")

year = input();

URL = f"https://uncannyxmen.net/publication-history/{year}"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

print('\n')
print(f"{bcolors.BOLD}","Comics released this year:",f"{bcolors.ENDC}", end='\n'*2)

find_list()

print(f"{bcolors.BOLD}","Important events that occured this year",f"{bcolors.ENDC}", end='\n'*2)

find_events()

print(f"{bcolors.BOLD}","First Appearances: ",f"{bcolors.ENDC}",end='\n'*2)

find_appearance()


