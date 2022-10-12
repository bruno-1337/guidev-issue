from github import Github 
import json


f = open('authkey.json',)
data = json.load(f)
authk = data['authkey']

g= Github(authk)

coutinho = g.get_user("arthurspk");

# def get_coutinhorepos():
#      repositorios = []
#      for repo in coutinho.get_repos():
#          repositorios.append(repo.name)
#      return repositorios

def get_validrepos():
    validrepodic = {}
    reposwithissues = {}
    #go thru all repos in coutinho github
    for repo in coutinho.get_repos():
        commits = get_commits(repo)
        issue = get_issues(repo)
        #check if repo has more than one issue
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

fulllist = get_validrepos()

for repo in fulllist.items():
    print(repo)

print (len(fulllist))
