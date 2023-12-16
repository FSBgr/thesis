import carball
import pandas as pd
import json

analysis = carball.analyze_replay_file("D:\Thesis\Supersonic Legend/f2c69ed4-84ba-474a-bfb3-bda2fe5e557c.replay") # Insert replay path here
#analysis = carball.analyze_replay_file("D:\Thesis\Supersonic Legend/8aa7ef32-2b6b-4bc2-8120-22ca488669ba.replay")


dropColumns = {'cameraSettings', 'partyLeader', 'loadout',
               'isBot'}  # irrelevant columns, not needed to analyze gameplay. Loadout is the skins and cosmetics of the player.
analysis = json.dumps(analysis.get_json_data()['players'], indent=4)
with open("players.json", "w") as file:
    file.write(analysis)

df = pd.read_json('players.json')
try:
    df.drop(dropColumns, inplace=True, axis=1)
except Exception as e:
    pass
df.to_csv("players.csv", index=0)

playerStats = json.dumps(df.loc(1)['stats'].to_dict())

with open("playerstats.json", "w") as stats:
    stats.write(playerStats)

statsdf = pd.read_json('playerstats.json')
statsdf.to_csv("playerstats.csv")

stats = {'boost', 'distance', 'possession', 'positionalTendencies', 'averages', 'hitCounts', 'controller', 'speed',
         'relativePositioning', 'perPossessionStats', 'kickoffStats', 'ballCarries'}

statsList = []

try:
    for i in stats:
        for j in range(len(statsdf.columns)):
            if type(statsdf.loc[i][j]) == float:
                continue
            statsList.append(statsdf.loc[i][j]) # Values for each category per player.
            statsListDf = pd.DataFrame(statsList, index=None)
            statsListDf.to_csv("statsListDf.csv")
except Exception as e:
    pass


csv1 = pd.read_csv('players.csv')
csv1.drop({'stats'}, inplace=True, axis=1)
csv2 = pd.read_csv('statsListDf.csv')
csv2 = csv2.iloc[:, 1:]  # Skipping the "Unnamed" column of the statsList csv
drops = {'carryStats', 'averageCounts', 'isBot', 'isKeyboard'}
try:
    csv2.drop(drops, inplace=True, axis=1)
except Exception as e:
    pass

merged = pd.concat([csv1, csv2])
merged.to_csv('merged.csv')


print(merged.columns)