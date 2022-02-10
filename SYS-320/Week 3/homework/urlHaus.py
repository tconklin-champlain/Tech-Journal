# Import re, and sys
import csv, re, sys
# Change the serachTerms to contents
def urlHausOpen(filename,contents):
# Define lists /filename
    filename = "urlHausTestDataSet.csv"
    rows = []
# Change the while loop to 'with open()' and fix all indents
    with open(filename,'r') as f:
        # change filename to the open file variable f and change attribute to reader
        contents = csv.reader(f)
        for row in range(9):
            next(contents)
            for keyword in contents:
                    # fix the quotations needed in the function
                    x = re.findall(r''+keyword+'', contents[2])
                    for row in contents:
                        rows.append(row)
    rows = sorted(rows)
    return rows
    # Check to see if there are results
    if len(contents) == 0:
        print("No Results")
        sys.exit(1)
    # Don't edit this line. It is here to show how it is possible
    # to remove the "tt" so programs don't convert the malicious
    # domains to links that an be accidentally clicked on.
    the_url = eachLine[2].replace("http","hxxp")
    the_src = eachLine[4]
    print("""
    URL:
    Info: 
    {}""",format(the_url, the_src,"*"+60))