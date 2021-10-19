#secure-ssh.sh
#creates a new ssh user using $1 parameter
#adds a public key from the local repo or curled from the rmeote repo
#removes roots ability to ssh in
echo -e 'sudo useradd -m -d /home/sys265 -s /bin/bash sys265\nsudo mkdir /home/sys265/.ssh\nsudo cp SYS265/linux/public-keys/id_rsa.pub /home/sys265/.ssh/authorized_keys\nsudo chmod 700 /home/sys265/.ssh\nsudo chmod 600 /home/sys265/.ssh/authorized_keys\nsudo chown -R sys265:sys265 /home/sys265/.ssh'

