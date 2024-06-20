import json
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlsplit, parse_qs
from urllib.parse import urljoin

base_url = "https://dota2.ru/esport/teams/"

uploads_dir = "uploads"

if not os.path.exists(uploads_dir):
    os.makedirs(uploads_dir)

def fetch_page_data(url):
    response = requests.get(url)
    src = response.content
    soup = BeautifulSoup(src, 'lxml')
    return soup


def parse_page_data(soup):
    table_rows = soup.find('table').find_all('tr', class_='title')
    page_org_info = []
    team_base_url = 'https://dota2.ru/esport/team/'
    for row in table_rows:
        current_href = row.find('a').get('href')
        team_url = urljoin(team_base_url, current_href)
        team_response = requests.get(team_url)
        team_soup = BeautifulSoup(team_response.content, 'lxml')
        team_info = team_soup.find('table', class_="cybersport-players-player__table").find_all('tr')
        # print(team_info)
        for info in team_info:
            team_info_country = info.find(id="country")
        
            if team_info_country != None:
                  team_info_country.text.split()
           
        
        # all_team_info = row.find_all('td')
        # name_org = all_team_info[2].find('span').text.strip()
        # image_org = all_team_info[2].find('img')
        # region_name = all_team_info[2].find('span').find('img').get('alt')
        
        # if image_org:
        #     img_url = image_org['src']
        #     fileNameClear = urlparse(os.path.basename(img_url)).path
            
        #     img_filename = f"{fileNameClear}"
        #     img_filepath = os.path.join(uploads_dir, img_filename)
        #     img_response = requests.get(f"https://dota2.ru/{img_url}")
        #     with open(img_filepath, 'wb') as img_file:
        #         img_file.write(img_response.content)
            
        #     page_org_info.append({
        #         'position': all_team_info[0].text.strip(),
        #         'rating': all_team_info[1].text.strip(),
        #         'org_name': name_org,
        #         'image_path': img_filename,
        #         'region_name': region_name
        #     })
    
    return page_org_info

def get_total_pages(soup):
    pagination = soup.find('ul', class_="pagination").find('li', class_="pagination__item pagination__link--right").text.strip()
    return int(pagination)


org_info = []

filename = "data.json"


soup = fetch_page_data(base_url)
total_pages = get_total_pages(soup)
org_info.extend(parse_page_data(soup))
print(total_pages)

for page_num in range(2, 1 + 1):
    page_url = f"{base_url}?page={page_num}"
    soup = fetch_page_data(page_url)
    org_info.extend(parse_page_data(soup))
    


with open(filename, 'w', encoding='utf-8') as file:
    json.dump(org_info, file, ensure_ascii=False, indent=4)

print("Данные успешно записаны в файл", filename)
