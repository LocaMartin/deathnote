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
## git `tag` command

List existing tags
```
git tag
```
Create annotated tags
```
# With message prompt
git tag -a v1.0 -m "Version 1.0 release"

# Direct message
git tag -a v1.0 -m "Initial release"
```
Filter tags using wildcards
```
git tag -l "v1.*"
```
Create lightweight tags
```
git tag v1.0-lw
```
Tag older commits
```
git tag -a v1.2 <commit-hash>
```
Push tags to remote
```
# Push single tag
git push origin v1.0

# Push all tags
git push origin --tags
```
Delete tags
```
# Delete locally
git tag -d v1.0

# Delete remotely
git push origin --delete v1.0
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
