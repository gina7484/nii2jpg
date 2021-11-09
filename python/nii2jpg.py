import os, sys, getopt
from convert import convert

def main(argv):

    inputdir = ''
    outputdir = ''
    # "../../2D/training/"
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('nii2png.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    
    for opt, arg in opts:
        if opt == '-h':
            print('nii2jpg.py -i <inputdir> -o <outputdir>')
            sys.exit()
        elif opt in ("-i", "--input"):
            inputdir = arg
        elif opt in ("-o", "--output"):
            outputdir = arg

    print('Input file is ', inputdir)
    print('Output folder is ', outputdir)
 
    for filename in os.listdir(inputdir):
        if filename.endswith(".nii.gz"): 
            # filename = volume-17-resized.nii.gz
            case_number= int(filename.split("-")[1])
            convert(os.path.join(inputdir,filename),outputdir,case_number)
            continue
        else:
            continue
    


# call the function to start the program
if __name__ == "__main__":
   main(sys.argv[1:])