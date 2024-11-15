import requests
import os
from bs4 import BeautifulSoup
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
BLUE = "\033[0;34m"
MAGENTA = "\033[0;35m"
CYAN = "\033[0;36m"
WHITE = "\033[0;37m"
RESET = "\033[0m"
BANNER = (
    f"{RESET}°{RED}██████████████████████████████████████████████████████████ \n"
    f" {RED}███████████▄─█▀▀▀█─▄██─▄▄▄▄██▄─▄─▀██─▄▄─██─▄─▄─███████████ \n"
    f" {WHITE}████████████─█─█─█─███▄▄▄▄─███─▄─▀██─██─████─█████████████ \n"
    f" ▀▀▀▀▀▀▀▀▀▀▀▀▄▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▀▄▄▄▄▀▀▀▄▄▄▄▀▀▀▄▄▄▀▀▀▀▀▀▀▀▀▀▀▀ \n"
    f" {CYAN}_________________________{RED}[ {GREEN}HAIFIL{RED} ]{CYAN}_______________________{RESET}"
)
os.system("clear")
print(BANNER)
print("")
link = input(f"{YELLOW}INPUT LINK TO ANALYSIS{WHITE}:{GREEN} ")
url = link
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    quotes = soup.find_all('span', class_='text')
    print(f"{YELLOW}SCRAPING DONE{WHITE}: ${CYAN}")
    for quote in quotes:
        print(quote.get_text(strip=True))
else:
    print(f"""
{RED}FAILED TO ACCESS WEBSITES{WHITE}: {YELLOW}{response.status_code}""")
import csv
with open('quotes.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Kutipan'])
    for quote in quotes:
        writer.writerow([quote.get_text(strip=True)])

print(f"""
{GREEN}FILE HAS BEEN SAVE IN {WHITE}quotes.csv""")