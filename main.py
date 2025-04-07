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

def write_time(time: int) -> None:
    with open(".lastunixtime", "w") as f:
        f.write(str(1+time))


with open(".lastunixtime", "r") as f:
    lastunixtime = int(f.read())

response = requests.get(f"https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions?user={username}&from_second={lastunixtime}")
results = response.json()
# results = json.loads(response)
# print(results)

repo = Repo(".")

for submission in tqdm.tqdm(results):
    sleep(0.1)
    if submission["result"] != "AC":
        write_time(submission["epoch_second"])
        continue
    contest_id = submission["contest_id"]
    problem_id = submission["problem_id"]
    submission_id = submission["id"]
    submission_language = submission["language"]
    submission_content = requests.get(f"https://atcoder.jp/contests/{contest_id}/submissions/{submission_id}").text
    # print(submission_content)
    try:
        soup = BeautifulSoup(submission_content, "html.parser")
    except:
        write_time(submission["epoch_second"])
        continue
    # print(soup.prettify())
    code = soup.find("pre", id="submission-code").text
    # print(code)
    os.makedirs(f"./{contest_id}", exist_ok=True)
    os.makedirs(f"./{contest_id}/{problem_id}", exist_ok=True)
    py_pattern = r"Python.*|PyPy3.*"
    cpp_pattern = r"C++.*"
    bf_pattern = r"Brainf.*"
    rb_pattern = r"Ruby.*"
    c_pattern = r"C.*"
    dc_pattern = r"dc.*"
    bash_pattern = r"Bash.*"
    txt_pattern = r"Text.*"
    sed_pattern = r"Sed.*"
    go_pattern = r"Go.*"
    cs_pattern = r"C#.*"
    kt_pattern = r"Kotlin.*"
    java_pattern = r"Java.*"
    nim_pattern = r"Nim.*"
    zig_pattern = r"Zig.*"
    js_pattern = r"JavaScript.*"
    d_pattern = r"D.*"
    swift_pattern = r"Swift.*"
    dart_pattern = r"Dart.*"
    php_pattern = r"PHP.*"
    cr_pattern = r"Crystal.*"
    fs_pattern = r"F#.*|Forth"
    jl_pattern = r"Julia.*"
    hs_pattern = r"Haskell.*"
    for_pattern = r"Fortran.*"
    lua_pattern = r"Lua.*"
    lisp_pattern = r"Common Lisp.*"
    cbl_pattern = r"COBOL.*"
    zsh_pattern = r"Zsh.*"
    sage_pattern = r"SageMath.*"
    bc_pattern = r"bc.*"
    pl_pattern = r"Perl.*|Prolog.*"
    awk_pattern = r"AWK.*"
    nako3_pattern = r"なでしこ.*"
    asm_pattern = r"Assembly.*"
    p_pattern = r"Pascal.*"
    ps1_pattern = r"PowerShell.*"
    scm_pattern = r"Scheme.*"
    scala_pattern = r"Scala.*"
    vb_pattern = r"Visual Basic.*"
    clj_pattern = r"Clojure.*"
    erl_pattern = r"Erlang.*"
    ts_pattern = r"TypeScript.*"
    rs_pattern = r"Rust.*"
    k_pattern = r"Koka.*"
    ml_pattern = r"OCaml.*"
    p6_pattern = r"Raku.*"
    vim_pattern = r"Vim.*"
    el_pattern = r"Emacs Lisp.*"
    rdr_pattern = r"プロデル.*"
    ecl_pattern = r"ECLiPSe.*"
    nbl_pattern = r"Nibbles.*"
    adb_pattern = r"Ada.*"
    jq_pattern = r"jq.*"
    cy_pattern = r"Cyber.*"
    carp_pattern = r"Carp.*"
    ll_pattern = r"LLVM IR.*"
    factor_pattern = r"Factor.*"
    ws_pattern = r"Whitespace.*"
    fish_pattern = r"><>.*"
    re_pattern = r"ReasonML.*"
    m_pattern = r"Octave.*|Mercury.*"
    jar_pattern = r"Haxe.*"
    ex_pattern = r"Elixir.*"
    sd_pattern = r"Seed7.*"
    uc_pattern = r"Unison.*"
    R_pattern = r"R.*"
    v_pattern = r"V.*"
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
    elif re.match(txt_pattern, submission_language):
        extension = "txt"
    elif re.match(sed_pattern, submission_language):
        extension = "sed"
    elif re.match(go_pattern, submission_language):
        extension = "go"
    elif re.match(cs_pattern, submission_language):
        extension = "cs"
    elif re.match(kt_pattern, submission_language):
        extension = "kt"
    elif re.match(js_pattern, submission_language):
        extension = "js"
    elif re.match(java_pattern, submission_language):
        extension = "java"
    elif re.match(nim_pattern, submission_language):
        extension = "nim"
    elif re.match(zig_pattern, submission_language):
        extension = "zig"
    elif re.match(d_pattern, submission_language):
        extension = "d"
    elif re.match(swift_pattern, submission_language):
        extension = "swift"
    elif re.match(dart_pattern, submission_language):
        extension = "dart"
    elif re.match(php_pattern, submission_language):
        extension = "php"
    elif re.match(cr_pattern, submission_language):
        extension = "cr"
    elif re.match(fs_pattern, submission_language):
        extension = "fs"
    elif re.match(jl_pattern, submission_language):
        extension = "jl"
    elif re.match(hs_pattern, submission_language):
        extension = "hs"
    elif re.match(for_pattern, submission_language):
        extension = "for"
    elif re.match(lua_pattern, submission_language):
        extension = "lua"
    elif re.match(lisp_pattern, submission_language):
        extension = "lisp"
    elif re.match(cbl_pattern, submission_language):
        extension = "cbl"
    elif re.match(zsh_pattern, submission_language):
        extension = "zsh"
    elif re.match(sage_pattern, submission_language):
        extension = "sage"
    elif re.match(bc_pattern, submission_language):
        extension = "bc"
    elif re.match(pl_pattern, submission_language):
        extension = "pl"
    elif re.match(awk_pattern, submission_language):
        extension = "awk"
    elif re.match(nako3_pattern, submission_language):
        extension = "nako3"
    elif re.match(asm_pattern, submission_language):
        extension = "asm"
    elif re.match(p_pattern, submission_language):
        extension = "p"
    elif re.match(ps1_pattern, submission_language):
        extension = "ps1"
    elif re.match(scm_pattern, submission_language):
        extension = "scm"
    elif re.match(scala_pattern, submission_language):
        extension = "scala"
    elif re.match(vb_pattern, submission_language):
        extension = "vb"
    elif re.match(clj_pattern, submission_language):
        extension = "clj"
    elif re.match(erl_pattern, submission_language):
        extension = "erl"
    elif re.match(ts_pattern, submission_language):
        extension = "ts"
    elif re.match(rs_pattern, submission_language):
        extension = "rs"
    elif re.match(k_pattern, submission_language):
        extension = "k"
    elif re.match(ml_pattern, submission_language):
        extension = "ml"
    elif re.match(p6_pattern, submission_language):
        extension = "p6"
    elif re.match(vim_pattern, submission_language):
        extension = "vim"
    elif re.match(el_pattern, submission_language):
        extension = "el"
    elif re.match(rdr_pattern, submission_language):
        extension = "rdr"
    elif re.match(ecl_pattern, submission_language):
        extension = "ecl"
    elif re.match(nbl_pattern, submission_language):
        extension = "nbl"
    elif re.match(adb_pattern, submission_language):
        extension = "adb"
    elif re.match(jq_pattern, submission_language):
        extension = "jq"
    elif re.match(cy_pattern, submission_language):
        extension = "cy"
    elif re.match(carp_pattern, submission_language):
        extension = "carp"
    elif re.match(ll_pattern, submission_language):
        extension = "ll"
    elif re.match(factor_pattern, submission_language):
        extension = "factor"
    elif re.match(ws_pattern, submission_language):
        extension = "ws"
    elif re.match(fish_pattern, submission_language):
        extension = "fish"
    elif re.match(re_pattern, submission_language):
        extension = "re"
    elif re.match(m_pattern, submission_language):
        extension = "m"
    elif re.match(jar_pattern, submission_language):
        extension = "jar"
    elif re.match(ex_pattern, submission_language):
        extension = "ex"
    elif re.match(sd_pattern, submission_language):
        extension = "sd"
    elif re.match(uc_pattern, submission_language):
        extension = "uc"
    elif re.match(R_pattern, submission_language):
        extension = "R"
    elif re.match(v_pattern, submission_language):
        extension = "v"
    else:
        print("unknown language for submission {} at contest {}: {}".format(submission_id, contest_id, submission_language))
        continue
    with open(f"{contest_id}/{problem_id}/{problem_id}.{extension}", "w") as f:
        f.write(code)
    write_time(submission["epoch_second"])
    repo.git.add(f"{contest_id}/{problem_id}/{problem_id}.{extension}")
    repo.git.add(f".lastunixtime")
    repo.index.commit(f"Add {contest_id}/{problem_id}/{problem_id}.{extension}")

repo.git.add(".")
repo.index.commit("Commit all changes")
repo.git.clear_cache()
del repo
