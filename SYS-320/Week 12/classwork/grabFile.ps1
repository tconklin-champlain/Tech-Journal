# Create commandline parameters to copy a file and place into an evidence directory
param(

[Parameter(Mandatory = $true)]
[int]$reportNo,

[Parameter(Mandatory = $true)]
[string]$filePath

)

# Create a directory with a report number
$reportDir = "rpt$reportNo"

# Creating a new directory
mkdir $reportDir

# Copying file into new directory
Copy-Item $filePath $reportDir