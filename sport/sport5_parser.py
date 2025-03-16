import requests
from bs4 import BeautifulSoup

class TeamData:
    def __init__(self, rank, name, games, wins, draws, losses, ratio, difference, points):
        self.rank = rank
        self.name = name
        self.games = games
        self.wins = wins
        self.draws = draws
        self.losses = losses
        self.ratio = ratio
        
        self.difference = difference
        self.points = points

    def __str__(self):
        return f"Rank: {self.rank}, Name: {self.name}, Points: {self.points}"

def parse_sport5_table(url):
    response = requests.get(url)
    response.raise_for_status()  # raise exception for bad status codes (4xx or 5xx)

    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('div', {'class': 'score-list'}).find_all('table')[0]
   

    if not table:
        return None

    team_data_list = []
    rows = table.find_all('tr')[1:]  # skip header row

    for row in rows:
        cells = row.find_all('td')
        if len(cells) == 9:
            rank = cells[0].text.strip()
            name = cells[1].text.strip()
            games = cells[2].text.strip()
            wins = cells[3].text.strip()
            draws = cells[4].text.strip()
            losses = cells[5].text.strip()
            ratio = cells[6].text.strip()

            difference = cells[7].text.strip()
           
            points = cells[8].text.strip()

            team_data = TeamData(rank, name, games, wins, draws, losses, ratio, difference, points)
            team_data_list.append(team_data)

    return team_data_list

if __name__ == "__main__":
    url = "https://www.sport5.co.il/liga.aspx?FolderID=44"
    teams = parse_sport5_table(url)

    if teams:
        for team in teams:
            print(team)
    else:
        print("Could not find table")