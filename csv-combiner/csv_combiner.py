import sys
import os
import pandas as pd

#apologies in advance if this isn't my best work. I had a lot of 
#schoolwork to catch up on, including 2 projects and 1 presentation.
    
def name(path):
    namelist = path.rfind('/')
    filename = path[namelist+1:]
    return filename

def combine_csvs(combined, csvlist):
    for i in range(len(csvlist)):
        try:
            temp = pd.read_csv(csvlist[i])
            temp['filename'] = name(csvlist[i])
            combined = pd.concat([combined,temp])
        except IOError as e:
            print(e)        

    return combined

#a decoy of main that has the exact same properties, only instead of sys.argv, we input a test array argv,
#and this method returns our output string instead of printing is
#THIS METHOD IS USED FOR TESTING PURPOSES
def main_decoy(argv):
    num_arguments = len(argv)
    if num_arguments <= 1:
        return "error, not enough arguments"
        
        
    elif(argv[0][len(argv[0])-4:] != '.php'): 
        return "error, cannot parse"

    else:
        csvlist = []
        for i in range(1,num_arguments):
            if os.path.isfile(argv[i]):
                if (argv[i][len(argv[i])-4:] == '.csv'):
                    csvlist.append(argv[i])
        try: 
            combined = pd.read_csv(csvlist[0])
            combined['filename'] = name(csvlist[0])

            if len(csvlist) > 1:
                combined = combine_csvs(combined, csvlist[1:])

            combined = combined.set_index(combined.columns[0])
            new_csv = combined.to_csv()
            #print(new_csv)
            return "success!"

        except IOError as e:
            print(e)
            return "error, cannot read first CSV"


def main():
    num_arguments = len(sys.argv)
    if num_arguments <= 1:
        print("error, not enough arguments")
        return
        
    elif(sys.argv[0][len(sys.argv[0])-4:] != '.php'): 
        print("error, cannot parse")
        return

    else:
        csvlist = []
        for i in range(1,num_arguments):
            if os.path.isfile(sys.argv[i]):
                if (sys.argv[i][len(sys.argv[i])-4:] == '.csv'):
                    csvlist.append(sys.argv[i])
        try: 
            combined = pd.read_csv(csvlist[0])
            combined['filename'] = name(csvlist[0])

            if len(csvlist) > 1:
                combined = combine_csvs(combined, csvlist[1:])

            combined = combined.set_index(combined.columns[0])
            new_csv = combined.to_csv()
            print(new_csv)

        except IOError as e:
            print(e)
            print("error, cannot read first CSV")
            return

if __name__ == "__main__":
    main()
