import urllib.request
import re
import os
import sys

# Get input parameters\
outputDir = None
try:
    outputDir = os.path.abspath (sys.argv[1])
except:
    raise Exception ("OUTPUT DIRECTORY IS NOT DEFINED IN INPUT PARAMETERS")

urlRegex = r'(?:href)\s*=\s*"(https:.+data.theotown.com.+get_file.php\?\S+)"\s+'

def extractImageLinks (stringToSearch):
    # Extract links
    urlList = re.findall (urlRegex, stringToSearch)

    #Fix formatting
    for index, value in enumerate (urlList):
        urlList[index] = value.replace ("\\", "")

    return urlList

def downloadImage (link, filename):
    urllib.request.urlretrieve (link, filename)

if __name__ == '__main__':
    # Get page html
    print ("Getting page contents...")
    try:
        pageContents = urllib.request.urlopen("https://forum.theotown.com/gallery/").read ().decode ("utf8")
    except:
        raise Exception ("GALLERY LINK MAY BE BROKEN. CONTACT DEVELOPER OF THIS SCRIPT FOR HELP")

    # Extract links from HTML data
    print ("Extracting image links...")
    urlList = extractImageLinks (pageContents)

    # Save images to disk
    print ("Saving images to disk...")
    try:
        for index, link in enumerate (urlList):
            print (str (index + 1) + "/" + str (len (urlList)) + ": " + link)
            # TODO: make sure folder path exists before doing this
            # downloadImage (link, os.path.join ("C:", os.sep, "Users", os.getlogin (), "Pictures", "TheoTown Gallery", "popular_background" + str (index + 1) + ".png"))
            downloadImage (link, outputDir)

    except:
        raise Exception ("ENSURE THAT THE DIRECTORY IS VALID AND NOT HIDDEN BY THE FILESYSTEM")