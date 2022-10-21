from github import Github 
import json
import time

#lê o arquivo authkey.json para pegar a key da github api, o arquivo deve estar no mesmo local que o script
f = open('authkey.json',)
data = json.load(f)
authk = data['authkey']

g= Github(authk)

#define qual o user do github que o programa deve inspecionar
coutinho = g.get_user("arthurspk");


def get_validrepos():
    validrepodic = {}
    reposwithissues = {}
    #go thru all repos in coutinho github
    for repo in coutinho.get_repos():
        time.sleep(2)
        commits = get_commits(repo)
        issue = get_issues(repo)
        #check if repo has more than one issue
        if not ((repo.name).startswith("guiade")):
            print(repo.name + ' não é um guia, skipping')
            continue
        if issue > 0:
            print (str(repo.name) + ' has ' + str(issue) + ' issues, skipping')
            continue
        #check if repo has less than 9 commits
        if commits > 8:
            print (str(repo.name) + ' has ' + str(commits) + ' commits, skipping')
            continue
        
        
        repo.create_issue(title="Guia sem conteudo", body="Guia sem conteudo | Issue criado pelo verificador de população de guia para guiadevbrasil em https://github.com/bruno-1337/guidev-issue")
        print('criei um issue em: '+ str(repo.name))
        validrepodic[repo.name] = commits
 
    return validrepodic

def get_issues(crepo):
    issues = 0
    for issue in crepo.get_issues(state='open'):
        issues+=1
    return issues

def get_commits(crepo):
    commit = 0
    #count all commits in crepo
    for commits in crepo.get_commits():
        commit+=1
    return commit

get_validrepos()
