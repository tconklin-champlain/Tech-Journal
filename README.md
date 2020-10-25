# Tech-Journal
A journal where I can document everything I learn both in school from labs, and off of school on my own.
Finished the github tutorial, Now I can start!

*//Plan to later edit down most important parts of each lab//*
# Setting up a small enterprise network

## Virtual Firewall & Windows 10 Config
- Lab 1 https://docs.google.com/document/d/1-XcJ2gEjgBkTEluPB4NYKCjHchag2m1UZANIAqLSLMU/edit 
## ADDS & DNS
- Lab 2 https://docs.google.com/document/d/1p_SAaRlDF_noFukhFArUedUR1bblM1nifSaRPDSG1tY/edit#
## Linux Network
- Lab 3 https://docs.google.com/document/d/125Ow1J6dk_h_MnZB4vrpCgLh4LokoBaU-RCKISzvHsY/edit
## DHCP
- Lab 4 https://docs.google.com/document/d/1xNNudD7ch0pSXqaX4MQz4uvHGico4nzwpXnDekzWbws/edit
## ADDS
- Lab 5 https://docs.google.com/document/d/1x9crY4B8ykKc1JTd3JYN8G-cKPt9YJsb_GH1wrTxhoo/edit
## Assessment 1
- Lab 6 https://docs.google.com/document/d/1iXeTeAI8vCT_Exo_GohoDAAlySaRxXzh7Qu6LGyDnMg/edit
## Remote Administrator Tools
- Lab 7 https://docs.google.com/document/d/1IhIrHa8C-i0TBCYNr-SZd7hZsu24WGMEzNHTdxwwRGI/edit
## Apache Lab
- Lab 8 https://docs.google.com/document/d/1Yf4omb9Pmdcs3XWryZQOPSbHlOEanyYGunWBrC2tSd4/edit


## Secure SSH
https://wiki.centos.org/HowTos/Network/SecuringSSH
## DHCP
DHCP offer,
DHCP discover,
DHCP request,
DHCP acknowledge,
https://medium.com/@bromiley/full-packet-friday-dhcp-abbc6b7b3c77#:~:text=A%20DHCP%20Discover%20packet%20is,and%20find%20the%20DHCP%20server.
## File Permissions
useradd (name), 
passwd (name), 
usermod -aG (group) (name), 
-a append, 
-G group, 
groupadd (name), 
chgrp (group) (name), 
## Linux Domain Join
sudo yum install realmd samba samba-common oddjob oddjob-mkhomedir sssd, 
realm join --user=your-domain-admin-username@yourdomain.local yourdomain.local, realm list
## Apache Configuration
firewall-cmd --list-all, firewall-cmd --add-service=(http,https,httpd), firewall-cmd --reload
## Mapping a drive
https://activedirectorypro.com/map-network-drives-with-group-policy/
