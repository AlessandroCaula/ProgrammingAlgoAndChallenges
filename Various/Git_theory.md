<img src="../assets/Git-Logo-2Color.svg">

\
Source: https://www.youtube.com/watch?v=S7XpTAnSDL4&t=2s

# Tracking Files & making commits.

### Create a new Repository

Inside the folder that we want to set as the repository, type:

```bash
git init
```

To rename the primary branch (which by default was `'master'`) to `'main'` (commonly used nowadays) or other names type the command:

```bash
# Instead of 'main' you can put other names for the primary branch
git config --global init.defaultBranch main
```

Main is the default branch name of your repo created by git. Every time you run the `git init` this branch will be automatically created for you. 