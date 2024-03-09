import unittest
import pandas as pd
import datetime

class TestTickData(unittest.TestCase):
    def test_values(self):
       
        df = pd.read_excel('Data.xlsx')

        for index, row in df.iterrows():
            
            self.assertIsInstance(row['datetime'], datetime.datetime)

           
            for field in ['close', 'high', 'low', 'open']:
                self.assertIsInstance(row[field], float)

            self.assertIsInstance(row['volume'], int)
            self.assertIsInstance(row['instrument'], str)

if __name__ == '__main__':
    unittest.main()
