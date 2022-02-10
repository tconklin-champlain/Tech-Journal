import logCheck
import importlib
importlib.reload(logCheck)

# SSH authentication failures
def apache_events(filename, service, term):
    
    # Call syslogCheck and return the results
    is_found = logCheck._logs(filename, service, term)
    
    # Found list
    found = []
    
    # Loop through results
    for eachFound in is_found:
        
        #Split the results
        sp_results = eachFound.split(" ")
        
        # Append the split value to the found list
        found.append(sp_results[8])
        
    hosts = set(found)
    
    for eachHost in hosts:
        
        print(eachHost)
        
# SSH authentication passes
def ssh_pass(filename, searchTerms):
    
    # Call syslogCheck and return the results
    is_found = logCheck._logs(filename, searchTerms)
    
    # Found list
    found = []
    
    # Loop through results
    for eachFound in is_found:
        
        #Split the results
        sp_results = eachFound.split(" ")
        
        # Append the split value to the found list
        found.append(sp_results[0] + " " + sp_results[1] + " " + sp_results[3])
    hosts = set(found)
    
    for eachHost in hosts:
        
        print(eachHost)
# YAML dissection
def yaml_pass(filename, service, term):
    
    # Call syslogCheck and return the results
    is_found = logCheck._logs(filename, service, term)
    
    # Found list
    found = []
    
    # Loop through results
    for eachFound in is_found:
        
        #Split the results
        sp_results = eachFound.split(" ")
        
        #QQ.exe - tcpconn6.tencent.com:80 close, 0 bytes sent, 0 bytes received, lifetime <1 sec
        # Append the split value to the found list
        found.append(sp_results[0] + " " + sp_results[2] + " " + sp_results[4] + " bytes sent " + sp_results[7] + " bytes recieved " )
    hosts = set(found)
    
    for eachHost in hosts:
        
        print(eachHost)