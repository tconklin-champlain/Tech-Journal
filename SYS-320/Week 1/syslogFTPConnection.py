import syslogCheck
import importlib
importlib.reload(syslogCheck)

# FTP Connection failures
def ftp_connection(filename, searchTerms):
    
    # Call syslogCheck and return the results
    is_found = syslogCheck._syslog(filename, searchTerms)
    
    # Found list
    found = []
    
    # Loop through results
    for eachFound in is_found:
        
        #Split the results
        sp_results = eachFound.split(" ")
        
        # Append the split value to the found list
        found.append(sp_results[3])
        
    returnedValues = set(found)
    
    for eachValue in returnedValues:
        
        print(eachValue)