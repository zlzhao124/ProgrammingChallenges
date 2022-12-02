import sys
import os
import pandas as pd

def combine_csvs(combined, csvlist):
    #iterates through a csvlist, makes dataframes for each csv in the list, 
    #and puts them into our combined dataframe 1 by 1
    for i in range(len(csvlist)):
        try:
            temp = pd.read_csv(csvlist[i])
            nameindex = csvlist[i].rfind('/')
            filename = csvlist[i][nameindex+1:]
            temp['filename'] = filename
            combined = pd.concat([combined,temp])
        except IOError as e:
            print(e)        
    return combined

# a decoy of main that has the exact same code, only instead of sys.argv, we input a test array argv,
# and this method returns our output string instead of printing error strings out. 
# Also no comments in this one. See main() for those.
#THIS METHOD IS USED FOR TESTING PURPOSES
def main_decoy(argv):
    num_arguments = len(argv)
    if (num_arguments <= 1):
        return "error, not enough arguments"
        
    elif (argv[0][len(argv[0])-4:] != '.php'): 
        return "error, cannot parse"

    else:
        csvlist = []
        for i in range(1,num_arguments):
            if (os.path.isfile(argv[i]) == True):
                if (argv[i][len(argv[i])-4:] == '.csv'):
                    csvlist.append(argv[i])
        try: 
            combined = pd.read_csv(csvlist[0])
            nameindex = csvlist[0].rfind('/')
            filename = csvlist[0][nameindex+1:]
            combined['filename'] = filename

            if (len(csvlist) > 1):
                combined = combine_csvs(combined, csvlist[1:])

            combined = combined.set_index(combined.columns[0])
            new_csv = combined.to_csv()
            #print(new_csv)
            return "success!"

        except IOError as e:
            print(e)
            return "error, cannot read first CSV"


def main():
    #gets the number of arguments in the command line
    num_arguments = len(sys.argv)

    #if <= 1, then no csvs to begin with!
    if (num_arguments <= 1):
        print("error, not enough arguments")
        return
    #if the first thing isn't a php, stop right there
    elif (sys.argv[0][len(sys.argv[0])-4:] != '.php'): 
        print("error, cannot parse")
        return

    else:
        csvlist = []
        #puts all valid csv files into csvlist, ignores other files
        for i in range(1,num_arguments):
            if (os.path.isfile(sys.argv[i]) == True):
                if (sys.argv[i][len(sys.argv[i])-4:] == '.csv'):
                    csvlist.append(sys.argv[i])
        try: 
            #the program will try and read the first csv in the list and make a dataframe
            combined = pd.read_csv(csvlist[0])
            nameindex = csvlist[0].rfind('/')
            filename = csvlist[0][nameindex+1:]
            combined['filename'] = filename

            #if there is more than one valid csv, call the combine method
            if (len(csvlist) > 1):
                combined = combine_csvs(combined, csvlist[1:])

            #once everything is combined, delete the row indices and make a new csv from our merged dataframe
            combined = combined.set_index(combined.columns[0])
            new_csv = combined.to_csv()
            print(new_csv)

        except IOError as e:
            print(e)
            print("error, cannot read first CSV")
            return

if __name__ == "__main__":
    main()
