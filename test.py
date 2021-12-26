import sys
import os
import os.path
from github import Github
from dotenv import load_dotenv

load_dotenv()

path = os.getenv("FILEPATH")
path = os.path.join(path, "kickstart-python-project")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
token = os.getenv("TOKEN")

print("path: " + path)
print("username: " + username)
print("password: " + password)
print("token: " + token)

folderName = "test-project"
target_path = os.path.join(path, folderName)
os.makedirs(target_path, exist_ok=True)

g = Github(token)
for repo in g.get_user().get_repos():
    print(repo.name)

# print("Succesfully created repository {}".format(folderName))
