import json

class JSONOps():
    '''
    RESTful filehandling Operations
    '''
    def __init__(self,path):
        ''' check if the file exists else create an empty json '''
        self.path = path
        try:
            with open(self.path,"r") as rf:
                pass
        except:
            with open(self.path,"w+") as wf:
                wf.write("{ }")

    def get_from_json(self):
        with open(self.path,"r") as jsonfile:
            return jsonfile.read()

    def update_json_file(self,data):
        with open(self.path,"w") as jsonfile:
            print(json.dumps(data,indent=4))
            jsonfile.write(json.dumps(data))

    def append_json_file(self,data):
        json_dict = json.loads(self.get_from_json())
        json_dict.update(data)
        self.update_json_file(json_dict)