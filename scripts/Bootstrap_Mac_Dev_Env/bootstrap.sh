#!/bin/bash

set -e -x

# Script to bootstrap new dev environment
# Mac only for now

# Change these values if needed:
TEMPDIR="/tmp/setup"
DOTFILES_REPO=""
VIRTUALENV_DIR="$HOME/.envs"

pretty_echo(){
    local fmt="$1"; shift

    # shellcheck disable=SC2059
    printf "\\n[BOOTSTRAP] $fmt\\n" "$@"
}

append_to_zshrc(){
    local text="$1" zshrc
    local skip_new_line="${2: -0}"

    if [ -w "$HOME/.zshrc.local" ]; then
      zshrc="$HOME/.zshrc.local"
    else
      zshrc="$HOME/.zshrc"
    fi

    if ! grep -Fqs "$text" "$zshrc"; then
    if [ "$skip_new_line" -eq 1 ]; then
      printf "%s\\n" "$text" >> "$zshrc"
    else
      printf "\\n%s\\n" "$text" >> "$zshrc"
    fi
  fi
}

osname=$(uname)

if [ "$osname" != "Darwin"]; then
  pretty_echo "Bootstrap only supports Mac for now. Exiting ..."
  exit 1
fi

if [ ! -d "Library/Developer/CommandLineTools"]; then
  pretty_echo "Command Line Tools must be installed first. Run 'xcode-select --install' first"
  exit 1
fi

# Enter a list of HOMEBREW Packages
BREW_PACKAGES=(
    zsh
    git
    python
    python3
    wget
    tree
    vim
    nvim
    tmux
    terraform
    bash-completion
    docker-completion
    docker-compose-completion
    awscli
) 

# ENTER A list of CASK Packages
CASK_PACKAGES=(
    iterm2
    docker
    visual-studio-code
)

CASK_FONTS=(
    font-fira-code
    font-fira-mono
    font-fira-mono-for-powerline
    font-hack-nerd-font
    font-source-code-pro
)

PIP_PACKAGES=(
    ansible
    virtualenv
    virtualenvwrapper
    powerline-status
)
# Make Install Dir
mkdir -p $TEMPDIR

# INSTALL HOMEBREW
if ! command -v brew >/dev/null; then
  pretty_echo "Installing Homebrew ..."
    curl -fsS \
      'https://raw.githubusercontent.com/Homebrew/install/master/install' | ruby

    export PATH="/usr/local/bin:$PATH"
fi

# UPDATE BREW & INSTALL BREW CASK
if brew list | grep -Fq brew-cask; then
  pretty_echo "Uninstalling old Homebrew-Cask ..."
  brew uninstall --force brew-cask
fi

pretty_echo "Updating Homebrew formulae ..."
brew update --force

pretty_echo "Installing Homebrew Cask & Fonts"
brew tap caskroom/cask
brew tap homebrew/cask-fonts

# INSTALL Brew Packages
pretty_echo "Installing Homebrew Packages"
brew install ${BREW_PACKAGES[@]}

# INSTALL CASK PACKAGES
pretty_echo "Installing CASK Packages"
brew cask install ${CASK_PACKAGES[@]}

# INSTALL CASK FONTS
brew cask install ${CASK_FONTS[@]}

# UPGRADE PIP
pretty_echo "Upgrading PIP"
pip3 install -U pip

# Install Powerline & Fonts
pretty_echo "Installing PIP Packages"
pip3 install --user ${PIP_PACKAGES[@]}

# Install Fonts
install_powerline_fonts(){
    local font_dir;
    font_dir="$TEMPDIR/powerlinefonts"
    pretty_echo "Installing Powerline Fonts"
    if [ ! -d "$font_dir" ]; then
      git clone https://github.com/powerline/fonts.git --depth=1 "$font_dir"
    fi
    pushd "$font_dir"
        sh ./install.sh
    popd
    rm -rf $font_dir
}

install_powerline_fonts

# Install OH-MY-ZSH
pretty_echo "Installing Oh-my-zsh"
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# GET DOTFILES
install_dotfiles(){
    local dotfiles_dir;
    dotfiles_dir="$TEMPDIR/dotfiles"
    git clone "$DOTFILES_REPO" "$dotfiles_dir"
    pushd "$dotfiles_dir"
        if [ -e "$dotfiles_dir/.tmux.conf" ]; then
            pretty_echo "Setting up tmux.conf"
            cp "$dotfiles_dir/.tmux.conf" $HOME/.tmux.conf
        fi

        if [ -e "$dotfiles_dir/.shell_aliases" ]; then
            pretty_echo "Setting up shell aliases"
            cp "$dotfiles_dir/.shell_aliases" $HOME/.shell_aliases
        fi

        pretty_echo "Setting up Vim"
        if [ ! -d $HOME/.vim ]; then
            mkdir -p $HOME/.vim
        fi
        cp -a "$dotfiles_dir/vim/." "$HOME/.vim"

        if [ -e "$dotfiles_dir/.zshrc" ]; then
            pretty_echo "Setting up ZSH"
            cp "$dotfiles_dir/.zshrc" $HOME/.zshrc
        fi
}

if [-z "$DOTFILES_REPO" ]; then
    pretty_echo "Setting up Dotfiles"
    install_dotfiles
fi

# Setup virtualenvs
create_venvs(){
    local venvs_dir;
    venvs_dir="$VIRTUALENV_DIR"
    if [ ! -d "$venvs_dir" ]; then
            pretty_echo "Adding Virtualenvs Directory"
            mkdir -p $venvs_dir
    fi
}

create_venvs

# shellcheck disable=SC2016
append_to_zshrc 'export WORKON_HOME=$VIRTUALENV_DIR 1'
append_to_zshrc 'source /usr/local/bin/virtualenvwrapper.sh'


# UPDATE SHELL
update_shell() {
  local shell_path;
  shell_path="$(command -v zsh)"

  pretty_echo "Changing your shell to zsh ..."
  if ! grep "$shell_path" /etc/shells > /dev/null 2>&1 ; then
    pretty_echo "Adding '$shell_path' to /etc/shells"
    sudo sh -c "echo $shell_path >> /etc/shells"
  fi
  sudo chsh -s "$shell_path" "$USER"
}

case "$SHELL" in
  */zsh)
    if [ "$(command -v zsh)" != '/usr/local/bin/zsh' ] ; then
      update_shell
    fi
    ;;
  *)
    update_shell
    ;;
esac


# shellcheck disable=SC2016
append_to_zshrc 'export PATH="/usr/local/bin:$PATH"' 1

