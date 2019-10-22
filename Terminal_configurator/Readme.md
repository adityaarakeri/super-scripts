## UBUNTU
### 1.install zsh
```
sudo apt-get update
sudo apt upgrade
sudo apt install zsh
```
### 2.After the installation is complete, change the default shell of the root user to zsh with the chsh command below.
```
chsh -s /bin/zsh
```
### 3.install oh_my_zsh
```
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```
### 4.custom theme powerlevel9k
```
git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k
```
### 5.edit .zshrc
### 6.download nerd font from https://www.nerdfonts.com/ and install it
### 7.change terminal font from ubuntu settings

