#!/usr/bin/env python3

import os
import sys
import json
import requests
from bs4 import BeautifulSoup
import tqdm
import re
from time import sleep
from git import Repo

username = "rotarymars"
lastunixtime = 0

with open(".lastunixtime", "r") as f:
    lastunixtime = int(f.read())

response = requests.get(f"https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions?user={username}&from_second={lastunixtime}")
results = response.json()
# results = json.loads(response)
# print(results)

repo = Repo(".")

for submission in tqdm.tqdm(results):
    sleep(1)
    if submission["result"] != "AC":
        continue
    contest_id = submission["contest_id"]
    problem_id = submission["problem_id"]
    submission_id = submission["id"]
    submission_language = submission["language"]
    submission_content = requests.get(f"https://atcoder.jp/contests/{contest_id}/submissions/{submission_id}").text
    # print(submission_content)
    soup = BeautifulSoup(submission_content, "html.parser")
    # print(soup.prettify())
    code = soup.find("pre", id="submission-code").text
    # print(code)
    os.makedirs(f"./{contest_id}", exist_ok=True)
    os.makedirs(f"./{contest_id}/{problem_id}", exist_ok=True)
    py_pattern = r"Python.*"
    cpp_pattern = r"C++.*"
    bf_pattern = r"Brainf.*"
    rb_pattern = r"Ruby.*"
    c_pattern = r"C.*"
    dc_pattern = r"dc.*"
    bash_pattern = r"Bash.*"
    extension = ""
    if re.match(py_pattern, submission_language):
        extension = "py"
    elif re.match(cpp_pattern, submission_language):
        extension = "cpp"
    elif re.match(bf_pattern, submission_language):
        extension = "bf"
    elif re.match(rb_pattern, submission_language):
        extension = "rb"
    elif re.match(c_pattern, submission_language):
        extension = "c"
    elif re.match(dc_pattern, submission_language):
        extension = "dc"
    elif re.match(bash_pattern, submission_language):
        extension = "bash"
    else:
        print("unknown language for submission {} at contest {}: {}".format(submission_id, contest_id, submission_language))
        continue
    with open(f"{contest_id}/{problem_id}/{problem_id}.{extension}", "w") as f:
        f.write(code)
    with open(".lastunixtime", "w") as f:
        f.write(str(submission["epoch_second"]))

    repo.git.add(f"{contest_id}/{problem_id}/{problem_id}.{extension}")
    repo.git.add(f".lastunixtime")
    repo.index.commit(f"Add {contest_id}/{problem_id}/{problem_id}.{extension}")
