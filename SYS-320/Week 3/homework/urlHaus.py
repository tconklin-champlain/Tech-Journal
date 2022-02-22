# Import re, and sys
import csv, re
# Change the serachTerms to contents
def urlHausOpen(filename,searchTerms):
# Define lists /filename
    filename = "urlHausTestDataSet.csv"
    rows = []
# Change the while loop to 'with open()' and fix all indents
    with open(filename,'r') as f:
        # change filename to the open file variable f and change attribute to reader
        contents = csv.reader(f)
        for row in range(9):
            # Iterate contents
            next(contents)
        for eachLine in contents:
            for keyword in searchTerms:
                # fix the quotations needed in the function
                x = re.findall(r''+keyword+'', eachLine[2])
                for _ in x:
                    # Don't edit this line. It is here to show how it is possible
                    # to remove the "tt" so programs don't convert the malicious
                    # domains to links that an be accidentally clicked on.
                    the_url = eachLine[2].replace("http","hxxp")
                    the_src = eachLine[6]
                    print("""
URL: {}
Info: {} 
{}""".format(the_url, the_src,"*"*60))