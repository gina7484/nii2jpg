# NIfTI Image Converter (nii2png) for Python and Matlab
Rejoice OpenCV users, a lightweight neuroimaging .nii to .png converter that actually works. 

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
$ python nii2png.py -i <inputfile> -o <outputfolder>
```

or

```
$ python nii2png.py --input <inputfile> --ouput <outputfolder>
```


2. Rotate the images if you wish

```
$ Would you like to rotate the orientation? (y/n) y
$ OK. By 90° 180° or 270°? 90
```

#### Example

with change directory command

```
$ cd ~/images/
$ python nii2png.py -i brain.nii.gz -o png/
```

with full paths

```
$ python /users/ernie/images/nii2png.py -i /users/ernie/images/brain.nii.gz -o /users/ernie/images/png/
```

with long options


```
$ python /users/ernie/images/nii2png.py --input /users/ernie/images/brain.nii.gz --output /users/ernie/images/png/
```

### Second verion (targetConvert branch)
1. Let's run the file and start converting images! **Please ensure that your output folder ends with a slash to avoid errors.**

```
$ cd (move to the python/foler)
$ python nii2png.py -i <inputfolder> -o <outputfolder> -x <csvfile>
```

or

```
$ python nii2png.py --input <inputfolder> --ouput <outputfolder> -x <csvfile>
```


#### Example

with change directory command

```
$ cd ./python/
$ python nii2jpg.py -i ../../CT-ORG/CT_ORG_Data_Testing/ -o ../../2D/testing/image-kidney/ -x ./kidney_idx_testing.CSV
```
The format of csv file is as below.
```
id,first,last,total
21,272,457,825
22,303,474,844
23,225,309,390
...
```

## Matlab Usage
Refer to the original library (https://github.com/alexlaurence/NIfTI-Image-Converter) for this section.

## Python Setup
Refer to the original library (https://github.com/alexlaurence/NIfTI-Image-Converter) for this section.
