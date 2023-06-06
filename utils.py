import json
import os
import requests


class BackendCommunication:
    def __init__(self, backend_server_url="http://127.0.0.1:8000/api/data"):
        self.backend_server_url = backend_server_url

    def get_bot_response(self, message):

        response = requests.get(self.backend_server_url, json={'content': message})

        if response.status_code == 200:
            data = response.json()
            print(response.json())
            return data['message']
        else:
            print('Error:', response.status_code)


class JsonDatabase:
    def __init__(self, filename):
        self.filename = filename

    def read_from_json(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        return data

    def write_json(self, new_data):
        try:
            with open(self.filename, 'r+') as file:
                file_data = json.load(file)
                file_data["messages"].append(new_data)
                # Sets file's current position at offset.
                file.seek(0)
                # convert back to json.
                json.dump(file_data, file, indent=4)
        except FileNotFoundError:
            if not os.path.exists(self.filename):
                with open(self.filename, 'w') as file:
                    json.dump({"messages": []}, file)
