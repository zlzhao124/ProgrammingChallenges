
import unittest
from csv_combiner import *
import os
import pandas as pd

class Tests(unittest.TestCase):
    #tests if a file is a csv
    def test_csv(self):
        print('Testing if a file is a CSV')
        path = "./testfiles"
        testfilelist = os.listdir(path)
        testfile = testfilelist[1]
        self.assertEqual(testfile[len(testfile)-4:],'.csv', "Not a csv file")

    #test the name method
    def test_name(self):
        path = "./testfiles/test1.csv"
        filename = name(path)
        self.assertEqual(filename,'test1.csv', "Name incorrect")

    #test the combine method
    def test_combine(self):
        testdf = pd.read_csv("./testfiles/test1.csv")
        testdf['filename'] = "test1.csv"

        combined = combine_csvs(testdf, ['./testfiles/test2.csv'])
        combined = combined.set_index(combined.columns[0])

        result = pd.read_csv("./testfiles/test3.csv")
        result = result.set_index(result.columns[0])

        equal = combined.equals(result)
        self.assertEqual(equal, True, "dataframes not equal!")

    # 3 main tests to see that the errors are accessed successfully
    def test_main1(self):
        argv = ['./csv-combiner.php', './testfiles/test1.csv', './testfiles/test2.csv']
        output = main_decoy(argv)
        self.assertEqual(output, "success!", "wrong output message!")

    def test_main2(self):
        argv = ['./csv-combiner.php']
        output = main_decoy(argv)
        self.assertEqual(output, "error, not enough arguments", "wrong output message!")

    def test_main3(self):
        argv = ['./csv-combiner.html', './testfiles/test1.csv', './testfiles/test2.csv']
        output = main_decoy(argv)
        self.assertEqual(output, "error, cannot parse", "wrong output message!")

        

if __name__ == "__main__":
    unittest.main()