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