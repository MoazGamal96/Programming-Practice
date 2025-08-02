
import requests
from bs4 import BeautifulSoup
import csv

# fetching url
date = input("pleas enter a date in the following formate MM/DD/YY: ")
page = requests.get(f"https://www.yallakora.com/match-center/?{date}")

def main (page):
    src= page.content
    soup = BeautifulSoup(src, "lxml")
    matches_details = []

    championships = soup.find_all("div", {'class': 'matchCard'})

    def get_match_info(championships):
        championship_title = championships.contents[1].find('h2').text.strip()
        all_matches = championships.contents[3].find_all('div', {'class':'teamsData'})
        number_of_matches = len(all_matches)

        for i in range(number_of_matches):
            #get teams names
            team_A = all_matches[i].find('div',{'class': 'teamA'}).text.strip()
            team_B = all_matches[i].find('div',{'class': 'teamB'}).text.strip()
            
            #get teams score
            match_result = all_matches[i].find('div',{'class' : 'MResult'}).find_all('span',{'class':'score'})
            score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"
            
            # get match time
            match_time = all_matches[i].find('div',{'class': 'MResult'}).find('span', {'class':'time'}).text.strip()
            
            #add match info to matches_details
            matches_details.append({"نوع البطولة":championship_title, "الفريق الأول":team_A,"الفريق الثاني":team_B,
            "النتيجة":match_result, "الوقت":match_time})
    #get all matches in championships 
    for i in range(len(championships)):
        get_match_info(championships[i])
    #get every key from matches_details for all valius
    keys = matches_details[0].keys()
    
    with open('D:/programing/pyproject/matches-details.csv','w') as output_file:
       dic_writer = csv.DictWriter(output_file, keys)
       dic_writer.writeheader()
       dic_writer.writerows(matches_details)
       print('file created')



main (page)   