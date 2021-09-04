# 💻 Tech-Journal
>*This is the journal that I use for both in-school labs and all out-of-school research. I'm going to organize any subjects I study into sections and highlight the critical parts. I will put any outside coding I do into separate folders on this git-repository.*    
#  🔧 Setting Up A Small Enterprise Network
# 📕 SYS-255
##  [Pfsense Virtual Firewall & Windows 10 Configuration](https://docs.google.com/document/d/1-XcJ2gEjgBkTEluPB4NYKCjHchag2m1UZANIAqLSLMU/edit "Lab 1")
### Quick Setup:
| Pfsense | Default Credentials
|----------|---------|
| Username: | *admin* |
| Password: | *pfsense* |
1. Assign interfaces 
1. Setup interface IP address
1. Navigate to firewall ip to finish setup
##  [Domain Name Server](https://docs.google.com/document/d/1p_SAaRlDF_noFukhFArUedUR1bblM1nifSaRPDSG1tY/edit# "Lab 2")
### Setting up DNS feature in ADDS:
1. Select Active Directory Domain Services
1. Add Features 
1. Pick Active Directory Domain 
1. Continue through deployment
1. Sign in as Domain Admin
### Adding a DNS record:
1. Open DNS Manager
1. Expand Foward Lookup Zones
1. Add a New Host on your domain
 <br> OR
1. Expand Reverse Lookup Zones
1. Add a New Zone
 
### Creating Named Domain User:
1. Select ADDS
1. Choose Active Directory Users & Computers
1. Under Users Select 'New User'
<br> AND OR
1. Add them to Domain Admins group to become a admin. 

### Joining a PC to a domain:
1. Control Panel -> System & Security
1. System -> System Properties
1. Change Domain
> 💡 *Best to create two accounts, one with admin privileges and one without.*


 
##  [Linux Network Configuration](https://docs.google.com/document/d/125Ow1J6dk_h_MnZB4vrpCgLh4LokoBaU-RCKISzvHsY/edit "Lab 3")
### File Permissions:
|Command | Description |
| ----------- | ----------- |
| nmtui | Network Manager Text User Interface |
| useradd | Adds New User |
| passwd | Adds Password for User |
| usermod -aG | Modify and Append User's Group |
| groupadd | Add New Group |
| chgrp | Change Group |
##  [Dynamic Host Configuration Protocol](https://docs.google.com/document/d/1xNNudD7ch0pSXqaX4MQz4uvHGico4nzwpXnDekzWbws/edit "Lab 4")
#### DORA:
1. DHCP Discover
1. DHCP Offer
1. DHCP Request
1. DHCP Acknowledge
<br>[Citation](https://medium.com/@bromiley/full-packet-friday-dhcp-abbc6b7b3c77#:~:text=A%20DHCP%20Discover%20packet%20is,and%20find%20the%20DHCP%20server.)
> 💣 *Time It is very important that all your Windows systems are on the same timezone and have accurate time with respect to one another.  Windows authentication is sensitive to differences in time.* 
##  [Active Directory Domain Services](https://docs.google.com/document/d/1x9crY4B8ykKc1JTd3JYN8G-cKPt9YJsb_GH1wrTxhoo/edit "Lab 5")
### Organizational Unit Creation:
1. Server Manager -> Local Server
1. Active Directory Users & Computers
1. Select Domain -> New OU

### Group Policy Enforcment:
1. Active Directory Users & Computers
1. Groups -> Group Policy Managment
1. Select Folder -> Create a GPO
##  [Practical Assessment 1](https://docs.google.com/document/d/1iXeTeAI8vCT_Exo_GohoDAAlySaRxXzh7Qu6LGyDnMg/edit "Lab 6")

___
##  [Remote Administrator Tools](https://docs.google.com/document/d/1IhIrHa8C-i0TBCYNr-SZd7hZsu24WGMEzNHTdxwwRGI/edit "Lab 7")
### Enable Remote Administration On Windows Server:
1. On Windows Server type <code>sconfig</code>
1. Enable *Configure Remote Managment*
> 💡 *Remote Administration in an enterprise environment would likely not be done on the domain controller, but rather a Domain Joined workstation or server with Remote Server Administration Tools installed.*

##  [Apache Lab](https://docs.google.com/document/d/1Yf4omb9Pmdcs3XWryZQOPSbHlOEanyYGunWBrC2tSd4/edit "Lab 8")
### Disable root SSH Access:
1. Disable remote root ssh access within the PermitRootLogin no flag in <code>/etc/ssh/sshd_config</code> file.
![ssh_disable](https://cdn.discordapp.com/attachments/578082700825591811/883824110235443240/ssh_access.png)
1. Type <code>service sshd restart</code> to finalize settings.
>💣 *CentOS and other Redhat based Linux servers ship with SSH turned on.  This combined with a known "root" user who is able to attempt login remotely presents a security flaw that must be addressed by the systems administrator before the system is accessible over the internet.  The typical solution involves explicitly preventing root from logging in via the sshd_config file.*
### Properly Securing SSH:
[Setting Up *sshd_config* File](https://wiki.centos.org/HowTos/Network/SecuringSSH "Citation")

### Linux Domain Join:
1. Install realmd <pre><code>sudo yum install realmd samba samba-common oddjob oddjob-mkhomedir sssd </pre></code>
1. Join The Domain <pre><code>realm join --user=your-domain-admin-username@yourdomain.local yourdomain.local, realm list</pre></code>
>💡 *Note, if your time is not consistent across Windows and Linux, then you will likely have problems.  Timezone can sometimes be a problem.*

### Apache Installation / Firewall Configuration:
1. [Installing Apache](http://httpd.apache.org/docs/2.4/install.html "Apache")
1. Firewall Config Commands<pre><code>firewall-cmd --list-all<br>firewall-cmd --add-service=(http,https,httpd)<br>firewall-cmd --reload</pre></code>
# 📗 SYS-265

## [Routing and Windows](https://docs.google.com/document/d/1JdoUgWs7obDHrJfRAtmzxTBbNifgAnoJHji9P9-tCOo/edit "Lab00")
###  
