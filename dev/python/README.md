**pipx**

`.gitnore`
```
__pycache__/
*.pyc
*.egg-info/
dist/
```

```bash
git add .
git commit -m "Initial commit"
git push -u origin main
```
- structure

```bash
rip/
├── pyproject.toml
├── README.md
└── src/
    └── rip/
        ├── __init__.py
        └── main.py  # Your script code
```
`project.toml`
```bash
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "rip"
version = "1.0.0"
description = "Reverse IP Toolkit"
readme = "README.md"
requires-python = ">=3.7"
dependencies = [
    "requests>=2.20.0"
]

[project.scripts]
rip = "rip.main:main"
```
- version tagging
```bash
# Create annotated tag
git tag -a v1.0.0 -m "Initial release"

# Push tags to GitHub
git push origin --tags
```

- local & remote installation

```bash
# Local test
pipx install .

# Remote test (after pushing)
pipx install git+https://github.com/LocaMartin/rip.git

# Specific version
pipx install git+https://github.com/LocaMartin/rip.git@v1.0.0
```

```bash
# Update pyproject.toml version
git add .
git commit -m "Update to v1.0.1"
git tag -a v1.0.1 -m "Feature update"
git push --follow-tags
```
