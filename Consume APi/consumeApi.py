import http.client
import json
from prettytable import PrettyTable

conn = http.client.HTTPSConnection("f1-live-motorsport-data.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "4baf16448dmshc6524f4231d42c6p1f8cc4jsn9143a65f2fac",
    'X-RapidAPI-Host': "f1-live-motorsport-data.p.rapidapi.com"
    }

conn.request("GET", "/drivers/standings/2016", headers=headers)

res = conn.getresponse()
data = res.read()
datafix = json.loads(data.decode('utf-8'))
datafix = datafix['results']

table = PrettyTable()
table.field_names = ["Posisi", "Nama", "Team Name", "Nationality", "Point"]

print("==== F1 Standings Season ====")
print("""
    1. Overall Standings
    2. TOP 5 Standings
    3. TOP 10 Standings
    4. Search Position
        \n""")
menu = int(input('Enter Your Choice : '))
if menu == 1:
        for i in range(len(datafix)):
            table.add_row([datafix[i]['position'],datafix[i]['driver_name'],datafix[i]['team_name'],datafix[i]['nationality'],datafix[i]['points']])
        print("""\n==================== Overall Standings ====================\n""")
        print(table)
elif menu == 2:
        for j in range(5):
            table.add_row([datafix[j]['position'],datafix[j]['driver_name'],datafix[j]['team_name'],datafix[j]['nationality'],datafix[j]['points']])
        print("""\n==================== Top 5 Standings ====================\n""")
        print(table)
elif menu == 3:
        for k in range(10):
            table.add_row([datafix[k]['position'],datafix[k]['driver_name'],datafix[k]['team_name'],datafix[k]['nationality'],datafix[k]['points']])
        print("""\n==================== Top 10 Standings ====================\n""")
        print(table)
elif menu == 4:
        print("\nThere Are 24 Racer")
        choose = int(input('Enter Position : '))
        poss = choose - 1
        table.add_row([datafix[poss]['position'],datafix[poss]['driver_name'],datafix[poss]['team_name'],datafix[poss]['nationality'],datafix[poss]['points']])
        print("""\n==================== Position ====================\n""")
        print(table)