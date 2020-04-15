from main import validFile

import unittest

class FileTest(unittest.TestCase):
    
    def testInvalidExtension(self):
        filename = "simple.txt.txt.txt"
        status = validFile(filename)
        self.assertEqual(status['valid'], False)
        self.assertEqual(status['message'], 'Wrong file extension')
    
    def testWrongFilePath(self):
        filename = "/twain.txt"
        status = validFile(filename)
        self.assertEqual(status['valid'], False)
        self.assertEqual(status['message'], 'Invalid file path')
    
    def testInvalidFilename(self):
        filename = ""
        status = validFile(filename)
        self.assertEqual(status['valid'], False)
        self.assertEqual(status['message'], 'Invalid file name')
    
    def testFileWithoutExtension(self):
        filename = "twain"
        status = validFile(filename)
        self.assertEqual(status['valid'], False)
        self.assertEqual(status['message'], 'Wrong file extension')
    
    def testFileWithRightName(self):
        filename = "twain.txt"
        status = validFile(filename)
        self.assertEqual(status['valid'], True)
        self.assertEqual(status['message'], 'Input specified correctly')

if __name__ == "__main__":
    unittest.main()

