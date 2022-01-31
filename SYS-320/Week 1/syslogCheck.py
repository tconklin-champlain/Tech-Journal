# Create and interface to search through syslog files
import re

def _syslog(filename,listOfKeywords):
    
    # Open a file
    with open(filename) as f:

        # read in the file and save it to a variable
        contents = f.readlines()
    # Lists to store the results
    results = []
    # Loop through the list returned. Each element is a line fromt thee smallSyslog file
    for line in contents:

        # Loops through the keywords
        for eachKeyword in listOfKeywords:

            # If the 'line' contains the keyword then it will print
            #if eachKeyword in line:
            # Searches and returns results using a regular expression search
            x = re.findall(r''+eachKeyword+'', line)
            # print(x)
            
            for found in x:
                
                # Append the returned keywords to the results list
                results.append(found)
                
                
    # Check to see if there are results
    if len(results) == 0:
        print("No Results")
        sys.exit(1)
    
    # Sort the list    
    results = sorted(results)
    
    return results