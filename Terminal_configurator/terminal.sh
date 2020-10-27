#!/bin/bash

# install zsh
sudo apt-get update
sudo apt upgrade
sudo apt install zsh

# After the installation is complete, change the default shell of the root user to zsh with the chsh command below
chsh -s /bin/zsh

# install oh_my_zsh
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# custom theme powerlevel9k
git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k
