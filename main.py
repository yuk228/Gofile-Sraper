import requests

class Gofile:
    def __init__(self):
        self.session = requests.Session()
        self.token = self.get_token()["token"]
        self.folder_id = self.get_token()["rootFolder"]

    def get_token(self):
        res = self.session.post("https://api.gofile.io/accounts")
        return res.json()["data"]
    
    def create_folder(self):
        headers = {
            "Authorization": "Bearer "+self.token,
            "Content-Type": "application/json"
        }
        payload = {
            "parentFolderId": self.folderid,
            "public": "true"
        }
        res = self.session.post("https://api.gofile.io/contents/createfolder", headers=headers, json=payload)
        return res.text
    
    def upload(self): 
        data = {
            "token": self.folder_id,
            "folderId": self.folder_id
                }
        with open("requirements.txt", 'rb') as file:
            files = {'file': file}
            res = self.session.post("https://upload.gofile.io/uploadfile", data=data, files=files)
        return res.text

if __name__ == "__main__":
    gofile = Gofile()
    print(gofile.create_folder())