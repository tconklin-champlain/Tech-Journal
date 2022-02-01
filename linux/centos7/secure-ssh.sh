#secure-ssh.sh
#creates a new ssh user using USER parameter
#adds a public key from the local repo or curled from the remote repo
#removes roots ability to ssh in
echo 'Creating a user who can only log in vis RSA'
USER=$1
sudo useradd -m -d /home/$USER -s /bin/bash $USER
sudo mkdir /home/$USER/.ssh
sudo cp ~/Tech-Journal/linux/public-keys/id_rsa.pub /home/$USER/.ssh/authorized_keys
sudo chmod 700 /home/$USER/.ssh
sudo chmod 600 /home/$USER/.ssh/authorized_keys
sudo chown -R $USER:$USER /home/$USER/.ssh
exit 0
