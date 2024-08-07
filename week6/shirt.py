import sys
from os.path import splitext
from PIL import Image, ImageOps
def main():
    check_command_line_arg()
    try:
        imageFile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit('Input does not exist')
    shirtfile = Image.open('shirt.png')
    size = shirtfile.size
    muppet = ImageOps.fit(imageFile, size)
    muppet.paste(shirtfile, shirtfile)
    muppet.save(sys.argv[2])

def check_command_line_arg():
    if len(sys.argv) < 3:
        print('Too few command-line arguments')
    elif len(sys.argv) > 3:
        print('Too many command-line arguments')
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])
    if check_extension(file1[1]) == False:
        sys.exit('Invalid input')
    elif check_extension(file2[1]) == False:
        sys.exit('Invalid output')
    if file1[1].lower() != file2[1].lower():
        sys.exit('Input and output have different extensions')


def check_extension(file):
    if file in ['.jpg','.jpeg','.png']:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
