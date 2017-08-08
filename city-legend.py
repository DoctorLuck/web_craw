import requests
from bs4 import BeautifulSoup
import json

# r=requests.get('http://www.ufball.com/match/join_teams_json.htm?divisionId=874902863023837184&page=')
# data=json.loads(r.text)
# print(data['data']['list'])
# print(r.status_code)
team_base_url='http://www.ufball.com/match/join_teams_json.htm?divisionId=874902863023837184&page='     #在此基础上对参赛球队信息进行获取
team_player_base_url='http://www.ufball.com/match/team_players.htm?divisionId=874902863023837184&teamId='   #获取球员的相关信息

def get_team_info(url):
    for i in range(1,11):
        r=requests.get(url+str(i))
        team_data=json.loads(r.text)
        for i in range(len(team_data['data']['list'])):
            teamName = team_data['data']['list'][i]['teamName']
            teamID = team_data['data']['list'][i]['teamId']
            get_team_player_info(teamID,teamName)

def get_team_player_info(ID,name):
    r=requests.get(team_player_base_url+ID)
    soup=BeautifulSoup(r.text,'lxml')
    # playerName=soup.select('span[class~=player-name-value]')
    # print(playerName)
    for player in soup.find_all('div',class_='player-detail'):
        playerName=player.find('span',class_='player-name-value').text
        # print(playerName)
        playerNum=player.find('span',class_='player-num-value').text
        playerAddress=player.find('span',class_='player-address-value').text
        playerAge=player.find('span',class_='player-age-value').text
        playerHeight=player.find('span',class_='player-height-value').text
        playerWeight=player.find('span',class_='player-weight-value').text
        print(name + '  '+playerName + '  ' + playerNum + '  ' + playerAddress +  '  ' + playerAge + ' ' + playerHeight + '  ' + playerWeight + ' ')

get_team_info(team_base_url)
