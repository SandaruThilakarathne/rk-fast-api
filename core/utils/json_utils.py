import json
import os
 
def read_json(file):
    # Opening JSON file
    cwd = os.getcwd()
    file_path = os.path.join(str(cwd), f"schedule_sets/{file}")
    print(file_path)
    f = open(file_path)
    
    # returns JSON object as
    # a dictionary
    data = json.load(f)

    return data["exerices"]