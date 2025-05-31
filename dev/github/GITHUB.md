# GitHub

# `git` commands

if you added a new repo to your repo you want to treat as a directory remove cache `.git`
```bash
# this command remove cache from a repo
git rm --cached <repo name>
```
```
git add .
```
```
git commit -m "message"
```
```
git push -u origin main
```

# Github API command `gh`

```
gh api /users/LocaMartin
```
```
gh api /users/LocaMartin/repos
```
```
gh auth login
```
```
gh api /repos/LocaMartin/<repository-name>
```
```
gh repo view LocaMartin/<repository-name>
```