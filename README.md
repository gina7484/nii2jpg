# NIfTI Image Converter (nii2png) for Python and Matlab
Rejoice OpenCV users, a lightweight neuroimaging .nii to .png converter that actually works. 

Now supports both Python3 and Matlab 2017b!

## Environment
* Python 3.7 (or Matlab 2017b)

## Python Setup
1. clone this repository
2. download the requirements
'''
pip install -r requirements.txt
'''

## Python Usage 

1. Let's run the file and start converting images! Please ensure that your output folder ends with a slash to avoid errors.

```
$ python nii2png.py -i <inputfile> -o <outputfolder>
```

or

```
$ python nii2png.py --input <inputfile> --ouput <outputfolder>
```

Tip: You can drag and drop the file/folder into the terminal window instead of typing the path

2. Rotate the images if you wish

```
$ Would you like to rotate the orientation? (y/n) y
$ OK. By 90° 180° or 270°? 90
```

### Example

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


## Matlab Usage
Refer to the original library (https://github.com/alexlaurence/NIfTI-Image-Converter) for this section.

## Python Setup
Refer to the original library (https://github.com/alexlaurence/NIfTI-Image-Converter) for this section.
