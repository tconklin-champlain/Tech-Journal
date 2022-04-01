# Get a list of running processes

# Get a list of members
#Get-Process | Get-Member

# Get a list of processes: name, id, path

# Save the output to a CSV File
#Get-Process | Select-Object ProcessName, Path, Id | Export-Csv -Path `
#C:\Users\knotm\Desktop\processes.csv

$outputName = "C:\Users\knotm\Desktop\runningServices.csv"

# System-Services and properties
#Get-Service | Get-Member
#Get-Service | select-object Status, Name, DisplayName| Export-Csv -Path `
#$outputName

#Get a list of running services
Get-Service | Where-Object { $_.Status -eq "Running" } |Export-Csv -Path `
$outputName

Check to see if file exists
if ( Test-path $outputName ) {
   write-host -BackgroundColor "Green" -ForegroundColor "White" "Services file was created!" 
} else {
    write-host -BackgroundColor "Red" -ForegroundColor "White" "Services file was not created!" 
}
