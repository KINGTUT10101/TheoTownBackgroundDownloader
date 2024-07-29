import urllib.request
import re
import os

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
    pageContents = urllib.request.urlopen("https://forum.theotown.com/gallery/").read ().decode ("utf8")

    # Extract links from HTML data
    print ("Extracting image links...")
    urlList = extractImageLinks (pageContents)

    # Save images to disk
    print ("Saving images to disk...")
    for index, link in enumerate (urlList):
        print (str (index + 1) + "/" + str (len (urlList)) + ": " + link)
        # TODO: make sure folder path exists before doing this
        downloadImage (link, os.path.join ("C:", os.sep, "Users", os.getlogin (), "Pictures", "TheoTown Gallery", "popular_background" + str (index + 1) + ".png"))