import carball
import gzip
from carball.json_parser.game import Game
from carball.analysis.analysis_manager import AnalysisManager
from carball.analysis.utils.pandas_manager import PandasManager
from carball.analysis.utils.proto_manager import ProtobufManager

filepath = "D:\Thesis\Champion - Grand Champion\Batch 8/"
# with open('replaynames.txt') as f:
for lines in open('replaynames-batch-8.txt'):
    try:
        lines = lines.strip("\n")
        # print(lines)
        analysis_manager = carball.analyze_replay_file(filepath +
                                                       lines)  # Change the replay file name based on the downloaded replay
        proto_game = analysis_manager.get_protobuf_data()
        _json = carball.decompile_replay(filepath + lines)  # same here
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

    except Exception as e:
        errorMessage = "Replay " + lines + " has failed: " + str(e)
        print(errorMessage)
        try:
            with open('errorfile-batch-8.txt', 'a') as errors:
                errors.write(errorMessage)
        except Exception as nofile:
            pass
        pass
    dataframe.to_csv(filepath + lines + '.csv')
