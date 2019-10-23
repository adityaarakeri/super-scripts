# Bootstrap Mac Development Environment

This script will bootstrap a new Mac python development environment (or augment a current one) with a modern development toolset.
 
The script is meant to be used as a guide.  It works great for me, and can work for your environment as-is, provided you follow the same conventions.  If not, the script can be augmented very easily.

For a look at the conventions, see [My Dotfiles Repo](https://github.com/dirtyonekanobi/dotfiles)

## Dependencies

- Mac Only
- OSX Mojave or newer
- Internet connection
- git repo with dotfiles `[optional]`

## Packages

The script will install [Homebrew](https://brew.sh/) and [Brew Cask](https://github.com/Homebrew/homebrew-cask) to perform additional package installation.

The following packages will be installed by default:

| Brew Packages | Cask Packages | Fonts | Pip |
|--- | --- | --- | --- |
| zsh | iterm2 | fira-code | ansible |
| git | docker | fira-mono | virtualenv |
| python | visual studio code | hack-nerd | virtualenvwrapper |
| python3 | | source-code-pro | powerline-status |
| wget | | | |
| tree | | | |
| vim |  | | |
| nvim | | | |
| tmux | | | |
| terraform | | | |
| bash-completion | | | |
| docker-completion | | | |
| awscli | | | |

Feel free to add/remove packages to the arrays to install additional packages.

For a list of all Casks go [HERE](https://formulae.brew.sh/cask/)

For a list of all Homebrew Formulae go [HERE](https://formulae.brew.sh/formula/)

## Usage

If the `$DOTFILES_REPO` is populated with a git repo, the script will clone this repo to a temp directory and perform the following tasks:

- copy the `.tmux.conf` file to `~/.tmux.conf`
- create a `~/.vim` directory if none exists
- create a ~/.zshrc file

The script will also create a virtualenvs directory as defined in the `$VIRTUALENV_DIR` at the top of the script.
