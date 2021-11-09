#!/usr/bin/env python
#########################################
#       nii2png for Python 3.7          #
#         NIfTI Image Converter         #
#                v0.2.9                 #
#                                       #
#     Written by Alexander Laurence     #
# http://Celestial.Tokyo/~AlexLaurence/ #
#    alexander.adamlaurence@gmail.com   #
#              09 May 2019              #
#              MIT License              #
#########################################

import imageio, numpy, shutil, os, nibabel
import sys, getopt

def convert(inputfile,outputdir,case_number):
    # set fn as your 4d nifti file
    image_array = nibabel.load(inputfile).get_data()
    print("dimension:"+str(len(image_array.shape)))

    # ask if rotate
    '''
    ask_rotate = input('Would you like to rotate the orientation? (y/n) ')

    if ask_rotate.lower() == 'y':
        ask_rotate_num = int(input('OK. By 90° 180° or 270°? '))
        if ask_rotate_num == 90 or ask_rotate_num == 180 or ask_rotate_num == 270:
            print('Got it. Your images will be rotated by {} degrees.'.format(ask_rotate_num))
        else:
            print('You must enter a value that is either 90, 180, or 270. Quitting...')
            sys.exit()
    elif ask_rotate.lower() == 'n':
        print('OK, Your images will be converted it as it is.')
    else:
        print('You must choose either y or n. Quitting...')
        sys.exit()
    '''

    # if 4D image inputted
    if len(image_array.shape) == 4:
        # set 4d array dimension values
        nx, ny, nz, nw = image_array.shape

        # set destination folder
        if not os.path.exists(outputdir):
            os.makedirs(outputdir)
            print("Created ouput directory: " + outputdir)

        print('Reading NIfTI file...')

        total_volumes = image_array.shape[3]
        total_slices = image_array.shape[2]

        # iterate through volumes
        for current_volume in range(0, total_volumes):
            slice_counter = 0
            # iterate through slices
            for current_slice in range(0, total_slices):
                if (slice_counter % 1) == 0:
                    # rotate or no rotate
                    '''
                    if ask_rotate.lower() == 'y':
                        if ask_rotate_num == 90 or ask_rotate_num == 180 or ask_rotate_num == 270:
                            print('Rotating image...')
                            if ask_rotate_num == 90:
                                data = numpy.rot90(image_array[:, :, current_slice, current_volume])
                            elif ask_rotate_num == 180:
                                data = numpy.rot90(numpy.rot90(image_array[:, :, current_slice, current_volume]))
                            elif ask_rotate_num == 270:
                                data = numpy.rot90(numpy.rot90(numpy.rot90(image_array[:, :, current_slice, current_volume])))
                    elif ask_rotate.lower() == 'n':
                        data = image_array[:, :, current_slice, current_volume]
                    '''
                    data = image_array[:, :, current_slice, current_volume]
                            
                    #alternate slices and save as png
                    print('Saving image...')
                    #image_name = inputfile[:-4] + "_t" + "{:0>3}".format(str(current_volume+1)) + "_z" + "{:0>3}".format(str(current_slice+1))+ ".png"
                    image_name = "img_" + str(case_number)+ "_z" + "{:0>3}".format(str(current_slice))+ ".jpg"
                    imageio.imwrite(image_name, data)
                    print('Saved.')

                    #move images to folder
                    print('Moving files...')
                    src = image_name
                    shutil.move(src, outputdir)
                    slice_counter += 1
                    print('Moved.')

        print('Finished converting images')

    # else if 3D image inputted
    elif len(image_array.shape) == 3:
        # set 4d array dimension values
        nx, ny, nz = image_array.shape

        # set destination folder
        if not os.path.exists(outputdir):
            os.makedirs(outputdir)
            print("Created ouput directory: " + outputdir)

        print('Reading NIfTI file...')

        total_slices = image_array.shape[2]

        slice_counter = 0
        #########################################
        #       selectively choose Z index      #
        #########################################
        criteria=[100,300,700]
        windowsize=[30,100,260,480]
        exclude_data=[55,65]
        startIndex=0
        if total_slices<=criteria[0]:
            startIndex=total_slices-windowsize[0]
        elif total_slices<=criteria[1]:
            startIndex=total_slices-windowsize[1]
        elif total_slices<=criteria[2]:
            startIndex=total_slices-windowsize[2]
        else:
            startIndex=total_slices-windowsize[3]

        # iterate through slices
        for current_slice in range(startIndex, total_slices):
            # alternate slices
            if current_slice in exclude_data:
                continue
            if (slice_counter % 1) == 0:
                # rotate or no rotate
                '''
                if ask_rotate.lower() == 'y':
                    if ask_rotate_num == 90 or ask_rotate_num == 180 or ask_rotate_num == 270:
                        if ask_rotate_num == 90:
                            data = numpy.rot90(image_array[:, :, current_slice])
                        elif ask_rotate_num == 180:
                            data = numpy.rot90(numpy.rot90(image_array[:, :, current_slice]))
                        elif ask_rotate_num == 270:
                            data = numpy.rot90(numpy.rot90(numpy.rot90(image_array[:, :, current_slice])))
                elif ask_rotate.lower() == 'n':
                    data = image_array[:, :, current_slice]
                '''
                data = image_array[:, :, current_slice]

                #alternate slices and save as png
                if (slice_counter % 1) == 0:
                    print('Saving image...')
                    #image_name = inputfile[:-4] + "_z" + "{:0>3}".format(str(current_slice+1))+ ".png"
                    image_name = "img_" + str(case_number)+ "_z" + "{:0>3}".format(str(current_slice))+ ".jpg"
                    imageio.imwrite(image_name, data)
                    print('Saved.')

                    #move images to folder
                    print('Moving image...')
                    src = image_name
                    shutil.move(src, outputdir)
                    slice_counter += 1
                    print('Moved.')

        print('Finished converting images')
    else:
        print('Not a 3D or 4D Image. Please try again.')

