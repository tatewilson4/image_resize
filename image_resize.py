import os
import argparse
from PIL import Image


DEFAULT_SIZE = (320, 180)

#resize method
def resize_image(input_dir, infile, output_dir='resized', size=DEFAULT_SIZE):
    #take off file extension and add _resized
    outfile = os.path.splitext(infile)[0] + '_resized'
    extension = os.path.splitext(infile)[1]

    try:
        img = Image.open(input_dir + '/' + infile)
        img = img.resize((size[0], size[1]), Image.LANCZOS)

        #setup new variable for the new file we will be resizing
        new_file = output_dir + '/' + outfile + extension
        img.save(new_file)
    except IOError:
        print('unable to resize image {}'.format(infile))


#added variables that check if we're running the script directly
if __name__ == '__main__':
    dir = os.getcwd()

    #check for command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_dir', help='Full Input Path')
    parser.add_argument('-o', '--output_dir', help='Full Output Path')

    #add options to customize image size
    parser.add_argument('-w', '--width', help='Resized Width')
    parser.add_argument('-t', '--height', help='Resized Height')

    args = parser.parse_args()

    #check if there was an input path specfied, if not put in resized dir
    if args.input_dir:
        input_dir = args.input_dir
    else:
        input_dir = dir + '/images'

    #check if there was an output path specfied, if not put in resized dir
    if args.output_dir:
        output_dir = args.output_dir
    else:
        output_dir = dir + '/resized'

    #check if height and width arguments are added, if not use default size
    if args.width and args.height:
        size = (int(args.width), int(args.height))
    else:
        size = DEFAULT_SIZE

    #check if resized directory exists
    #if it does not exist, create one
    if not os.path.exists(os.path.join(dir, output_dir)):
        os.mkdir(output_dir)

    try:
        for file in os.listdir(input_dir):
            #create resize method
            resize_image(input_dir, file, output_dir, size=size)
    except OSError:
            print('file not found')
