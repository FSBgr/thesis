import carball
import pandas as pd
import json

filepath = "D:\Thesis\Champion - Grand Champion\All/"


def prepare_for_csv(p_data: list, c_drop: list):
    p_data = p_data.copy()
    # filter bots and drop columns
    for p in p_data:
        for c in c_drop:
            try:
                del p[c]
            except:
                pass
        if p['isBot']:
            p_data.remove(p)
        del p['isBot']

    for p in p_data:
        p['id'] = p['id']['id']
        p_name = p['name']
        if type(p_name) is list:
            p['name'] = p_name[0]
        for s in p['stats']:
            for s2 in p['stats'][s]:
                s2_val = p['stats'][s][s2]
                if type(s2_val) is dict:
                    for s3 in p['stats'][s][s2]:
                        p[('stats', s, s2, s3)] = p['stats'][s][s2][s3]
                else:
                    p[('stats', s, s2)] = p['stats'][s][s2]
        del p['stats']

    return p_data


player_df = pd.DataFrame()

for lines in open('D:\Thesis\Champion - Grand Champion\All/replaynames-Champion-Grand-Champion.txt'):
    try:
        lines = lines.strip("\n")
        # Insert replay path here
        analysis = carball.analyze_replay_file(filepath + lines)

        columns_to_drop = ['titleId', 'cameraSettings', 'loadout', 'partyLeader', 'timeInGame', 'firstFrameInGame']

        player_data = analysis.get_json_data()['players']

        player_data[0].keys()

        csv_player_data = prepare_for_csv(player_data, columns_to_drop)

        # player_df = pd.DataFrame.from_dict(csv_player_data)
        tempDf = pd.DataFrame.from_dict(csv_player_data)
        frames = [player_df, tempDf]
        player_df = pd.concat(frames)

    except Exception as e:
        print(e)
        pass

player_df.to_csv('playerAnalysis-Champion-Grand-Champion-NEW.csv')

# Some further data formatting - not to be considered

'''csv1 = pd.read_csv('playerAnalysis-Champion-Grand-Champion-NEW.csv')
csv2 = pd.read_csv('playerAnalysis-Platinum-Diamond-NEW.csv')
csv3 = pd.read_csv('playerAnalysis-Supersonic-Legend-New.csv')
csv4 = pd.read_csv('playerAnalysis-Silver-Gold-NEW.csv')

h1 = list(csv1.columns.values)
h2 = list(csv2.columns.values)
h3 = list(csv3.columns.values)
h4 = list(csv4.columns.values)

counter = 0
missingCols = []
for i in h2:
    if i not in h1:
        missingCols.append(i)
        counter += 1

print(missingCols, "   ", counter)

#csv2toDrop = {missingCols}
csv2.drop([missingCols])

csvMerge = pd.concat([csv1, csv2], axis=0, ignore_index=True)
csvMerge = pd.concat([csvMerge, csv3], axis=0, ignore_index=True)
csvMerge = pd.concat([csvMerge, csv4], axis=0, ignore_index=True)

csvMerge.to_csv("finalAnalysis.csv")'''

'''df = pd.read_csv("finalAnalysis.csv")
df.fillna(df.mean().round(1), inplace=True)
df.to_csv("finalAnalysis-1.csv")
print(df.columns.values)'''