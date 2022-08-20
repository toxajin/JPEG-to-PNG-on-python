import os
import sys
from PIL import Image

path = sys.argv[1]
new_path = sys.argv[2]
if not os.path.exists(new_path):
    os.mkdir(new_path)
files = os.listdir(path)
for infile in files:
    f, e = os.path.splitext(infile)
    outfile = f + ".png"
    print(outfile)
    if infile != outfile:
        try:
            with Image.open(path+infile) as im:
                im.save(new_path+outfile)
                print('Wow! Did it!')
        except OSError:
            print("cannot convert", infile)