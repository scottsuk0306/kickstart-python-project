import sys
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

path = os.getenv("FILEPATH")
# Should be discarded after testing
path = os.path.join(path, "kickstart-python-project")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
token = os.getenv("TOKEN")

def create():
    folderName = str(sys.argv[1])
    target_path = os.path.join(path, folderName)
    os.makedirs(target_path, exist_ok=True)
    g = Github(token)
    user = g.get_user()

    isCreated = True

    try:
        user.create_repo(folderName)
    except Exception as e:
        print("Exception Occured!")
        if e.status == 422:
            print("Repository of the name {} already exists.".format(projectName))
        isCreated = False
    
    if isCreated:
        print("Succesfully created repository {}".format(folderName))

if __name__ == "__main__":
    create()