from time import sleep
from flask import Flask
from flask_socketio import SocketIO
import coordiante_reader as cm


app = Flask(__name__)
sio = SocketIO(app, cors_allowed_origins='*')


def forever_thread():
    #   This thread should run forever in the background and be able to
    #   send messages to all clients every one second
    files = ['cords/line1.csv', 'cords/line2.csv', 'cords/line3.csv']
    while True:
        for file_path in files:     #   run through all the 3 provided csv files, then restart it from the beginning
            csv_data = cm.read_csv(file_path)
            csv_data_keys = list(csv_data.keys())   #   list of the csv keys (not hard coded for flexibility)
            csv_length = len(csv_data[csv_data_keys[0]])    #   get the number of "rows" for the first key
            for row_index in range(csv_length):    #    go through the lenght of the csv file
                coordinate = {}
                for key in csv_data_keys:         #     build up the coordinate      
                    coordinate[key] = csv_data[key][row_index]
                sleep(1)
                sio.emit("ship_data", coordinate) #     send the new coordinate through the websocket for the Express js backend
        
if __name__ == '__main__':
    sio.start_background_task(forever_thread)
    sio.run(app, debug=True)