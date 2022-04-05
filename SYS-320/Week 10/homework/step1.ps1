#Create random number to add to file
$sbRand = get-random -Minimum 1000 -Maximum 9876

# Output name variable
$outputName =  "D:\Documents\School\Programming\Tech-Journal\SYS-320\Week 10\homework\EnNoB-$sbRand.exe"
$outputName2 = "C:\Users\knotm\Desktop\Readme.READ"

# Copy powershell.exe to home directory
Copy-Item "C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe" -Destination $outputName

# Check if file exists
if ( Test-path $outputName ) {
    write-host -BackgroundColor "Green" -ForegroundColor "White" "Powershell file was created!" 
 } else {
     write-host -BackgroundColor "Red" -ForegroundColor "White" "Powershell file was not created!" 
 }

 # Creates a Message
 Write-Host "If you want your files restored, please contact me at dunston@champlain.edu.`
I look forward to doing business with you." > $outputName2


# Check if READ file exists
if ( Test-path $outputName2 ) {
    write-host -BackgroundColor "Green" -ForegroundColor "White" "READ file was created!" 
 } else {
     write-host -BackgroundColor "Red" -ForegroundColor "White" "READ file was not created!" 
 }

 # I liked that this assignment showed that malware is someetimes easier to understand then one thinks
 # No additional questions.