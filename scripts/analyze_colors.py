# Best flags in terms of color density:
# /Users/helgammal/lightning_talks/flags/images/Flag_of_Savannah,_Georgia.gif
# /Users/helgammal/lightning_talks/flags/images/Flag_of_Madison,_Wisconsin.png
# /Users/helgammal/lightning_talks/flags/images/Flag_of_Portland,_Oregon.png
# /Users/helgammal/lightning_talks/flags/images/Flag_of_Denison,_Texas.png
# /Users/helgammal/lightning_talks/flags/images/PLFD_fahne.png
# /Users/helgammal/lightning_talks/flags/images/Municipal_Flag_of_Chicago.png
# /Users/helgammal/lightning_talks/flags/images/Flag_of_Westminster,_Colorado.gif
# /Users/helgammal/lightning_talks/flags/images/Flag_of_New_Orleans,_Louisiana.png
# /Users/helgammal/lightning_talks/flags/images/Flag_of_Albuquerque,_New_Mexico.png
# /Users/helgammal/lightning_talks/flags/images/Flag_of_Monterey,_California.png
# ***
# Worst flags in terms of color density:
# /Users/helgammal/lightning_talks/flags/images/Flag_of_Montgomery,_Alabama.png
# /Users/helgammal/lightning_talks/flags/images/Flag_of_Milwaukee,_Wisconsin.png
# /Users/helgammal/lightning_talks/flags/images/Flag_of_Houston,_Texas.png
# /Users/helgammal/lightning_talks/flags/images/Flag_of_Philadelphia,_Pennsylvania.png
# /Users/helgammal/lightning_talks/flags/images/City_of_Asheville_North_Carolina_Flag.jpg
# /Users/helgammal/lightning_talks/flags/images/Flag_of_Mobile,_Alabama.png
# /Users/helgammal/lightning_talks/flags/images/Flag_of_Toledo,_Ohio.png
# /Users/helgammal/lightning_talks/flags/images/Flag_of_Tucson,_Arizona.png
# /Users/helgammal/lightning_talks/flags/images/Bridgeport_flag.png
# /Users/helgammal/lightning_talks/flags/images/City_of_Moreno_Valley_CA_Flag.jpg
import os
import shutil
import sys
import cv2
import gif2numpy

color_dict = {}
best_color_flags = '/Users/helgammal/lightning_talks/flags/best_color_flags'
worst_color_flags = '/Users/helgammal/lightning_talks/flags/worst_color_flags'
def analyze_color(image_path):
    if not image_path.endswith('.gif'):
        im = cv2.imread(image_path)
    else:
        np_images, extensions, image_specs = gif2numpy.convert(image_path)
        im = np_images[0]
    distinct_colors = set(tuple(v) for m2d in im for v in m2d)
    color_dict[image_path] = len(distinct_colors)

images_path = sys.argv[1]
path_format = '/Users/helgammal/lightning_talks/flags/images/{0}'
with open(images_path,'r') as f:
    for name in f.readlines():
        curr_path = path_format.format(name).strip()
        analyze_color(curr_path)
color_dict = sorted(color_dict.items(), key=lambda x: x[1])
print (color_dict)
print ('Best flags in terms of color density:')
for flag in color_dict[0:10]:
    print(flag[0])
    shutil.copy(flag[0],best_color_flags)
print ('***')
print ('Worst flags in terms of color density:')
for flag in color_dict[-10:]:
    print(flag[0])
    shutil.copy(flag[0],worst_color_flags)