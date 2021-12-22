# NIfTI Image Converter (nii2jpg) for Python and Matlab
Rejoice OpenCV users, a lightweight neuroimaging .nii to .jpg converter that actually works. 

Now supports both Python3 and Matlab 2017b!

## Environment
* Python 3.7 (or Matlab 2017b)

## Python Setup
1. clone this repository
2. download the requirements
```
pip install -r requirements.txt
```

## Python Usage 

We have 2 versions.
The first version is as same as the original library (https://github.com/alexlaurence/NIfTI-Image-Converter). It converts a sinle NIfTI image into series of 2D jpg images.
The second version is modified from the original library, which converts each file in a given folder into series of 2D jpg images. It selectively produces 2D images within the z index range indicated in the csv file.

### First verion (master branch)
1. Let's run the file and start converting images! **Please ensure that your output folder ends with a slash to avoid errors.**

```
$ cd (move to the python/foler)
$ python nii2jpg.py -i <inputfile> -o <outputfolder>
```

or

```
$ python nii2jpg.py --input <inputfile> --ouput <outputfolder>
```


2. Rotate the images if you wish

```
$ Would you like to rotate the orientation? (y/n) y
$ OK. By 90° 180° or 270°? 90
```

This will be sliced into several 2D jpg images which are named as below. The number after 'z' means the z index corresponding to the produced jpg image.
```
img_z72.jpg
```
#### Example

with change directory command

```
$ cd ~/images/
$ python nii2jpg.py -i brain.nii.gz -o png/
```

with full paths

```
$ python /users/ernie/images/nii2jpg.py -i /users/ernie/images/brain.nii.gz -o /users/ernie/images/png/
```

with long options


```
$ python /users/ernie/images/nii2jpg.py --input /users/ernie/images/brain.nii.gz --output /users/ernie/images/png/
```

### Second verion (targetConvert branch)
1. Move to the 'targetConvert' branch.
```
$ git checkout targetConvert
```
2. Let's run the file and start converting images! **Please ensure that your output folder ends with a slash to avoid errors.**

```
$ cd (move to the python/foler)
$ python nii2jpg.py -i <inputfolder> -o <outputfolder> -x <csvfile>
```

or

```
$ python nii2jpg.py --input <inputfolder> --ouput <outputfolder> -x <csvfile>
```

Note: We assume that the files in the inputfolder is names in the following format. (The number 1 is the id for the input file)
```
volume_1_resized.nii.gz
```
(You can change this part (https://github.com/gina7484/nii2jpg/blob/629f76cd03deda9123dbd67de675fbfcc7ade887/python/nii2jpg.py#L31) according to the file name format in your own input folder.)

This will be sliced into several 2D jpg images which are named as below. The first number means the id of the input file and the number after 'z' means the z index corresponding to the produced jpg image.
```
img_1_z72.jpg
```
(You can change this part https://github.com/gina7484/nii2jpg/blob/c4364096a4164dc5b9b6fdf25f037bee58eb8cf3/python/convert.py#L80 according to the desired filename format in your own output folder.)

#### Example

with change directory command

```
$ cd ./python/
$ python nii2jpg.py -i ../../CT-ORG/CT_ORG_Data_Testing/ -o ../../2D/testing/image-kidney/ -x ./kidney_idx_testing.CSV
```
The format of csv file is as below. The id should be identical to the number included in the file name. (i.e. If the id in the csv is 21, the corresponding file should be named as volume_21_resized.nii.gz)
```
id,first,last
21,272,457
22,303,474
23,225,309
...
```

## Matlab Usage
Refer to the original library (https://github.com/alexlaurence/NIfTI-Image-Converter) for this section.

## Python Setup
Refer to the original library (https://github.com/alexlaurence/NIfTI-Image-Converter) for this section.
