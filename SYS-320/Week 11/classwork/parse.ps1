# Array of websites containing threat intel
$drop_urls = @('https://rules.emergingthreats.net/blockrules/emerging-botcc.rules','https://rules.emergingthreats.net/blockrules/compromised-ips.txt')

# Loop through the URLS for rules list
foreach ($u in $drop_urls){
    #Extract the filename
    $temp = $u.split("/")

    # The last element in the array plucked off is the filename
    $file_name = $temp[-1]

    IF (Test-Path $file_name){
        continue
    
    } else {

    
    # Download the rules list
    Invoke-WebRequest -Uri $u -OutFile $file_name

    } # close if statement

} # close the foreach loop

# Array containing filename
$input_paths =@('.\compromised-ips.txt','.\emerging-botcc.rules')

# Extract Ip addresses
$regex_drop = '\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
# Append the IP to temp list
Select-String -Path $input_paths -Pattern $regex_drop | `
ForEach-Object { $_.Matches } | `
ForEach-Object { $_.Value } | Sort-Object | Get-Unique
Out-File -FilePath "ips-bad.tmp"

# Get IP discovered, loop through and replace the begining of line with IPTables syntax
# After the IP address, add the remaining IPTables syntax and save results to filec
# iptables -A INPUT -s IP -j DROP
(Get-Content -Path ".\ips-bad.tmp") | ForEach-Object `
{ $_ -replace "^", "iptables -A INPUT -s " -replace "$", " -j DROP" } | `
Out-File -FilePath "iptables.bash"