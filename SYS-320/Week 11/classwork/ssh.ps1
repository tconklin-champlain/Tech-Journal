# Login to remote ssh server
#New-SSHSession -ComputerName '192.168.1.12' -Credential (Get-Credential test)

<#

while ($True) {

#Add a prompt to run commands
$the_cmd = read_host -Prompt "Please Enter Command"

# Run command on remote ssh server
(Invoke-SSHCommand -index 0 'ps -ef').Output 

}

#>

Set-SCPItem -ComputerName '192.168.1.12' -Credential (Get-Credential test) `
-Destination '/home/test' -Path '.\test.jpg'

