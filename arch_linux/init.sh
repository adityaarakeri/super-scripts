# ARCH LINUX 2019.06.01 Installation Guide
#
# WARNING: This script is a template, mild modifications may be
#	   required at launch or pre-execution based on,
#	   networking, file system, storage, and application needs.
#
#Follow Guide Shown:
#	https://wiki.archlinux.org/index.php/Installation_guide

#!/bin/bash


#Confirm and Adjust Network Settings:
	ip link
	ping -c 5 archlinux.org

#Time & Date:
	timedatectl set-ntp true

#Adjust and Partition Drives:
	fdisk -l

	parted /dev/sda

#	mklabel  msdos
#	mkpart	primary		ext4	0%	100%
#	set 	1 			boot 	on
#	print
#	quit


#Format Partitions:
	mkfs.ext4 /dev/sda1

#Mount Partitions:
	mount  /dev/sda1  /mnt


#Install Base Arch System:
	pacstrap /mnt base base-devel

#Generate Filesystem Table:
	enfstab -U /mnt >> /mnt/etc/fstab

#Move work to Mount:
	arch-chroot /mnt

	exit #exit?


#Set Region:
	ln  -sf  /usr/share/zoneinfo/America/New_York  /etc/localtime

#Set Hardware System Clock:
	hwclock --systohc

#Language Preference
	locale-gen #uncomment country language of preference

#Network configuration
#	Create the hostname file:

#	/etc/hostname
#	myhostname
#	Add matching entries to hosts(5):

		nano /etc/hostname
		#add name to file
		#save file


#	/etc/hosts
#	{
		127.0.0.1	localhost
		::1			localhost
		127.0.1.1	myhostname.localdomain	myhostname
#	}

#		{} copy & paste above into - 
		nano /etc/hosts


#Initramfs:
	mkinitcpio -p linux

I#nsure Internet Services begin at startup:
	systemctl enable dhcpcd.service


#Bootloader:
	pacman -S intel-ucode
	pacman -S grub
	grub-install --target=i386-pc /dev/sda
	grub-mkconfig -o /boot/grub/grub.cfg    

#Root Password:
	passwd


#Create Additional Users:
	useradd -m -g users -s /bin/bash archie
	passwd archie


#Add Temporary Permissions:
	pacman -S sudo



#Funzies installing a desktop environment:

	pacman -S net-tools pkgfile base-devel


# first, install Xorg
	pacman -S xorg  xorg-server  xorg-apps
	sudo pacman -S gnome

#	//sudo systemctl start gdm.service


#MINER SOFTWARE AND HARDWARE DRIVERS (VARIES BASED ON COMPONENTS)
	git clone https://aur.archlinux.org/ethminer.git
#	cd #INTOPACKAGE
#	makepkg -sri


#install correct drivers for graphics cards by following these steps:
#https://wiki.archlinux.org/index.php/Xorg#AMD

#example: 
#	pacman -S xf86-video-amdgpu


#git clone https://aur.archlinux.org/opencl-amd.git
#	cd #INTOPACKAGE
#	makepkg -sri


#all done:
#	start miner with:
#	https://github.com/ethereum-mining/ethminer/blob/master/docs/POOL_EXAMPLES_ETH.md

#	Example:
#	ethminer -G -P stratum2+tcp://BTC_WALLET.WORKERNAME@daggerhashimoto.br.nicehash.com:3353
