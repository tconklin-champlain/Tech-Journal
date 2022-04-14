# List the files in the directory
# List all files and print the whole path
#Get-ChildItem -Recurse -Include *.docx,*.pdf,*.txt -Path '.\SYS-320\Week 12\classwork\Documents' |Select FullName

#Get-ChildItem -Recurse -Include *.docx,*.pdf,*.txt -Path '.\SYS-320\Week 12\classwork\Documents' |Export-Csv `
#-Path files.csv

# Import the CSV
$filelist = Import-Csv -Path '.\SYS-320\Week 12\classwork\files.csv' -Header FullName

# Loop through the results
foreach ($f in $filelist) {
    Get-ChildItem -Path $f.
}