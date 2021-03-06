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
print("target_path: " + target_path)
os.makedirs(target_path, exist_ok=True)

projectName = folderName

g = Github(token)
user = g.get_user()

isCreated = True

try:
    user.create_repo(projectName)
except Exception as e:
    print("Exception Occured!")
    if e.status == 422:
        print("Repository of the name {} already exists.".format(projectName))
    isCreated = False

if isCreated:
    print("Succesfully created repository {}".format(projectName))