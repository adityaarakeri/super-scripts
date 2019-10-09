# ✅ Automate Git Reposiory Creation

Let’s say you want to create a new repository on GitHub. Without automation, it
involves multiple steps and can take a few minutes. This script makes it easier.

Using this script, a single command creates a repository of the name you want, declares it private
or public, adds a description, clones the repository locally in the current directory,
updates `README.md` and pushes all changes.

## Usage

Simply execute the script file by supplying repository name, description and type (public or private).
You can also make it global by including it in `.bashrc` as a
function.

```sh
$ repo.sh your-repo-name repo-description private
```

![Preview](https://ahmadbilal.dev/wp-content/uploads/2019/04/run-2.png)
