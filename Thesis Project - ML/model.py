import carball
import gzip
from carball.json_parser.game import Game
from carball.analysis.analysis_manager import AnalysisManager
from carball.analysis.utils.pandas_manager import PandasManager
from carball.analysis.utils.proto_manager import ProtobufManager


filepath = "D:\Thesis\Supersonic Legend/5ac409d0-e8a0-4435-8604-56833c1394f2.replay"

analysis_manager = carball.analyze_replay_file(filepath)  # Change the replay file name based on the downloaded replay
proto_game = analysis_manager.get_protobuf_data()
_json = carball.decompile_replay(filepath)  # same here
game = Game()
game.initialize(loaded_json=_json)

analysis_manager = AnalysisManager(game)
analysis_manager.create_analysis()

# return the proto object in python
proto_object = analysis_manager.get_protobuf_data()

# return the proto object as a json object
json_oject = analysis_manager.get_json_data()

# return the pandas data frame in python
dataframe = analysis_manager.get_data_frame()

with open('output.pts', 'wb') as fo:  # Change output.pts to different name everytime, based on the replay
    analysis_manager.write_proto_out_to_file(fo)

# write pandas dataframe out as a gzipped numpy array
with gzip.open('output.gzip', 'wb') as fo:  # Change output.pts to different name everytime, based on the replay
    analysis_manager.write_pandas_out_to_file(fo)

# --------------- Once the replay is parsed and saved locally, no need to run the code above -----------------#

# read proto from file
with open('output.pts', 'rb') as f:
    proto_object = ProtobufManager.read_proto_out_from_file(f)

# read pandas dataframe from gzipped numpy array file
with gzip.open('output.gzip', 'rb') as f:
    dataframe = PandasManager.read_numpy_from_memory(f)



'''filepath= "D:\Thesis\Silver-Gold\Batch 1\csv/"
df = pd.read_csv(filepath + "0ff0ad34-2122-4524-b026-f55f21c6fc3f.replay.csv", header=[0,1], index_col=0, low_memory=False)


nonPlayers = ["ball", "game"]
df = df.drop(columns=nonPlayers)

#Collecting all columns

columns = list(df.columns)

#TODO: Combine all pos_x, pos_y etc values in one table, one for each column.

#print(columns[1][1])
#print(df[columns[1]])
pos_x=[]
label = ["silver-gold" for i in range(len(columns), 9)]
for i in range(len(columns)):
#print(df[columns[i]])
if columns[i][1] == "pos_x":
for j in range(len(df[columns[i]])):
    #pos_x.insert(j,df[columns[i][j]])
    print(df[columns[i]][j])
#pos_x.append()

#print(pos_x)'''

