#!/bin/bash

sudo apt-get install dnsmasq
sudo iptables -F
sudo iptables -t nat -F
sudo iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
sudo iptables -A FORWARD -i wlan0 -o eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -i eth0 -o wlan0 -j ACCEPT
sudo nano /proc/sys/net/ipv4/ip_forward
sudo nano /etc/sysctl.conf 
sudo ip route del 0/0 dev eth0 &> /dev/null
a=`route | awk "/${wlan}/"'{print $5+1;exit}'`
sudo ip route add 192.168.2.0/23 dev eth0
sudo route add -net default gw 192.168.2.1 netmask 0.0.0.0 dev eth0 metric $a
sudo nano /etc/dnsmasq.conf
sudo systemctl start dnsmasq
curl -o wifi-to-eth-route.sh https://raw.githubusercontent.com/arpitjindal97/raspbian-recipes/master/wifi-to-eth-route.sh
nano /home/pi/.config/lxsession/LXDE-pi/autostart
sudo bash /home/pi/wifi-to-eth-route.sh
