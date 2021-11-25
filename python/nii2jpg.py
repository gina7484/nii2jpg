import os, sys, getopt
from convert import convert
from pandas import *
import argparse

def convertDir(args):

    # parse arguments
    inputdir = args.inputdir
    outputdir = args.outputdir
    csvpath= args.csvpath
    
    # nii2jpg.py -i ../../CT-ORG/CT_ORG_Data_Training_labels_kidneys/ -o ../../2D/training/label-kidney/ -idx ./kidney_idx_training.CSV
    # nii2jpg.py -i ../../CT-ORG/CT_ORG_Data_Testing_labels_kidneys/ -o ../../2D/testing/label-kidney/ -idx ./kidney_idx_testing.CSV

    print('Input file is ', inputdir)
    print('Output folder is ', outputdir)
    print('csvpath is ', csvpath)
    
    index_data = read_csv(csvpath)
    
    # converting column data to list
    data_id_list = index_data['id'].tolist()
    start_idx_list = index_data['first'].tolist()
    last_idx_list = index_data['last'].tolist()
    
    for idx in range(0,len(data_id_list)):
        print("length of data:"+str(len(data_id_list)))

        case_number=data_id_list[idx] # int
        filename='labels-'+str(case_number)+'-kidneys.nii.gz'
        
        start_idx=start_idx_list[idx]
        last_idx=last_idx_list[idx]

        print("converting: "+filename)
        convert(os.path.join(inputdir,filename),outputdir,case_number,start_idx, last_idx)
        continue


def get_args():
    parser = argparse.ArgumentParser(description='Convert nifti file to 2D image according to z info in csv file')
    parser.add_argument('--inputdir', '-i', type=str, help='indut directory with nifti files (has to end with /)')
    parser.add_argument('--outputdir', '-o', type=str, help='output directory to save 2D images (has to end with /)')
    parser.add_argument('--csvpath', '-x', type=str, help='csv file with z index info')

    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    convertDir(args)


