# File to traverse a given directory and it's sub directories and retrieve all the files.

from logging import root
import os, argparse

#parser
parser = argparse.ArgumentParser(

    description ="Traverses a directory and builds a forensic body file",
    epilog="Developed by Trisha Conklin, 20220222"
)

# Add argument to pass to the fs.py program
parser.add_argument("-d", "--directory", required="True", help="directory that you want to traverse.")

#Parse the argumetns
args = parser.parse_args()

rootdir = args.directory

# Get info from commandline
#print(sys.argv)

# Directory to traverse
#rootdir = sys.argv[1]

#print(rootdir)

# We will traverse a directory

# Check if arg is directory
if not os.path.isdir(rootdir):
    print("Invalid directory => {}".format(rootdir))
    exit()
# List to save files
fList = []

# Crawl through provided directory
for root, subfolders, filenames in os.walk(rootdir):

    for f in filenames:

        # print(root + "/" +f)
        fileList = root + "/" + f
        #print(fileList)
        fList.append(fileList)

#print(fList)

def statFile(toStat):

    # i is going to be the variable used for each metadata element
    i =  os.stat(toStat,follow_symlinks=False)

    # url
    url = i[0]

    # status
    status = i[1]

    # bytes reurned
    bytes_ret = i[2]

    print("0|{}|{}|{}|".format(toStat, status, url, bytes_ret))

for eachFile in fList:

    statFile(eachFile)