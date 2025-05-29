# Go Project Setup & Version Management Guide

## Table of Contents
- [Initial Setup](#initial-setup)
- [Semantic Versioning](#semantic-versioning)
- [Tag Management](#tag-management)
- [GitHub Actions Workflow](#github-actions-workflow)
- [Best Practices](#best-practices)

## Initial Setup

### 1. Repository Setup
```bash
# Clone repository
git clone https://github.com/LocaMartin/turtle
cd turtle
```

### 2. Initialize Go Module
```bash
go mod init github.com/LocaMartin/turtle
go mod tidy
```

### 3. Initial Commit
```bash
git add .
git commit -m "Initial project setup"
git push origin main
```

## Semantic Versioning

### Version Format: `vMAJOR.MINOR.PATCH`

| Increment | Description                      | Example    |
|-----------|----------------------------------|------------|
| MAJOR     | Breaking API changes             | v2.0.0     |
| MINOR     | New backward-compatible features | v1.3.0     |
| PATCH     | Backward-compatible bug fixes    | v1.0.1     |

### Creating a New Release
```bash
# Commit changes
git add .
git commit -m "Add feature X"

# Create annotated tag
git tag -a v1.0.1 -m "Add feature X"

# Push with tags
git push origin main --tags
```

## Tag Management

### View Tags
```bash
# Local tags
git tag

# Remote tags
git ls-remote --tags origin
```

### Delete Tags
```bash
# Local delete
git tag -d v1.0.0

# Remote delete
git push origin --delete v1.0.0
```

## GitHub Actions Workflow

Create `.github/workflows/go.yml`:
```yaml
name: Go CI/CD

on:
  push:
    tags: [v*]
  pull_request:
    branches: [main]

jobs:
  build-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Go
        uses: actions/setup-go@v4
        with:
          go-version: 1.21
          
      - name: Build
        run: go build -v ./...
        
      - name: Test
        run: go test -v ./...
        
      - name: Lint
        run: |
          go install golang.org/x/lint/golint@latest
          golint ./...
```

### Workflow Use Cases
| Scenario                  | Automation Benefit               |
|---------------------------|-----------------------------------|
| Continuous Integration    | Run tests on every PR/push       |
| Cross-platform Builds     | Build for multiple OS targets    |
| Release Management        | Auto-create GitHub releases      |
| Code Quality              | Enforce linting/formatting       |

## Best Practices

1. **Always use annotated tags**  
   ```bash
   git tag -a v1.0.0 -m "Message"
   ```

2. **Push tags immediately** after creation  
   ```bash
   git push --tags
   ```

3. **Maintain semantic versioning** strictly  
   - Increment MAJOR for breaking changes
   - Increment MINOR for new features
   - Increment PATCH for bug fixes

4. **Keep dependencies updated**  
   ```bash
   go mod tidy
   ```

5. **Write meaningful commit messages**  
   Bad: "Fix stuff"  
   Good: "Fix file validation edge case"

6. **Use workflow triggers wisely**  
   ```yaml
   on:
     push:
       tags: [v*]  # Trigger on version tags
     pull_request:
       branches: [main]
   ```

> **Note:** For small projects or prototypes, you can simplify workflows, but maintaining version discipline from the start helps in long-term maintenance.