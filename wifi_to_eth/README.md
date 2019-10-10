Wifi Modem to Ethernet Port Forwarding:
========================================

This guide assumes you've already paired your Raspberry Pi 3B+ with your 
home wifi network and configured your username and root/admin password. 

Start:
---------------------

### Confirm Wi-Fi Signal:
```
  sudo ifup
```

### Confirm Dependencies:
```
  sudo apt-get install dnsmasq
```

### Network Address Translation (NAT) Share Settings:
```
  sudo iptables -F
  sudo iptables -t nat -F
  sudo iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
  sudo iptables -A FORWARD -i wlan0 -o eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT
  sudo iptables -A FORWARD -i eth0 -o wlan0 -j ACCEPT
```

### dnsmasq Setting Adjustments:
```
  sudo nano /proc/sys/net/ipv4/ip_forward
  sudo nano /etc/sysctl.conf 
```

### IP Routing:
```
  sudo ip route del 0/0 dev eth0 &> /dev/null
  a=`route | awk "/${wlan}/"'{print $5+1;exit}'`
```

### dnsmasq Setting (part 2):

If an error occurs when attempting the second line try:
```
  sudo ip route add 192.168.2.0/23 dev eth0
```
And then repeat line 2.

```
sudo ip route add 192.168.2.0/23 dev eth0
sudo route add -net default gw 192.168.2.1 netmask 0.0.0.0 dev eth0 metric $a
```

Additional steps:
```
  sudo nano /etc/dnsmasq.conf
```
  scroll to the bottom and add these lines:
```
  interface=eth0
  bind-interfaces
  server=8.8.8.8
  domain-needed
  bogus-priv
  dhcp-range=192.168.2.2,192.168.2.100,12h
```

To Confirm Functionality start what you've set up:
```
sudo systemctl start dnsmasq
```

## Additional Automation:

```
curl -o wifi-to-eth-route.sh https://raw.githubusercontent.com/arpitjindal97/raspbian-recipes/master/wifi-to-eth-route.sh

nano /home/pi/.config/lxsession/LXDE-pi/autostart
```
and add this to the bottom of the file:
```
  sudo bash /home/pi/wifi-to-eth-route.sh
```

### Anytime you would like to confirm or manually initiate wifi to ethernet route forwarding execute:
```
sudo bash /home/pi/wifi-to-eth-route.sh
```
