# This scripts sorts the input from download.py into folders
from PIL import Image
import os
from typing import Final
import datetime
import shutil
# def get_date_taken(path):
#     exif = Image.open(path)._getexif()
#     if not exif:
#         raise Exception('Image {0} does not have EXIF data.'.format(path))
#     return exif[36867]

def getBasicDate(path):
    raw_data=f.split(".")[-2][-19:]
    year=raw_data[0:4]
    month=raw_data[5:7]
    day=raw_data[8:10]
    date=datetime.datetime(int(year),int(month),int(day))
    return date

def organize(originalPath):# This will return the correct new path
    
    getBasicDate(originalPath)
    date= getBasicDate(originalPath)
    phase1Begin:Final=datetime.datetime(2022,5,1)
    phase1End:Final=datetime.datetime(2022,8,31)
    phase2Begin:Final=datetime.datetime(2022,9,1)
    phase2End:Final=datetime.datetime(2022,12,31)
    phase3Begin:Final=datetime.datetime(2023,1,1)
    phase3End:Final=datetime.datetime(2023,12,31)
    newPath = os.path.dirname(originalPath)
    fileName=os.path.basename(originalPath).split('/')[-1]
    # Get it in the right phase
    if date>=phase1Begin and date<=phase1End:
        newPath=os.path.join(newPath, "Phase1")
    elif date>=phase2Begin and date<=phase2End:
        newPath=os.path.join(newPath, "Phase2")
    elif date>=phase3Begin and date<=phase3End:
        newPath=os.path.join(newPath, "Phase3")
    #Get it in the right subfolder
    if fileName.lower().endswith(".jpeg") or fileName.lower().endswith(".jpg") or fileName.lower().endswith(".png") or fileName.lower().endswith(".heic"):
        newPath=os.path.join(newPath, "Photos",fileName)
    else:
        newPath=os.path.join(newPath, "Videos",fileName)
    
    return newPath

    # f"C:\\Users\\There\\Downloads\\LLS Photos\\iCloud_Photos\\{filename}" - The New File
# 10:35

directory="C:\\Users\\There\\StudioPrograms\\Web\\LLS Photos\\Better_Photos"
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    shutil.move(f, organize(f))


