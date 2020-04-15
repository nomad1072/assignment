from typing import List

import argparse
import os
import string

def validFile(filename: str) -> bool:
    '''
        Given a filename, validate if its a valid file
    '''
    if not filename:
        return { 'valid': False, 'message': 'Invalid file name' }
    
    name = filename.split(".")
    if len(name) != 2 or name[1] != 'txt':
        return { 'valid': False, 'message': 'Wrong file extension' }
    
    if not os.path.exists(filename):
        return { 'valid': False, 'message': 'Invalid file path' }
    
    return { 'valid': True, 'message': 'Input specified correctly' }

def longestParagraph(paragraphs: List[str]) -> int:
    '''
        Given a list of paragraphs in a text, function should return the
        index of the longest paragraph w.r.to word count
    '''
    removeLines = [paragraph.replace("\n", " ") for paragraph in paragraphs]
    prunedParagraphs = [paragraph.translate(str.maketrans('', '', string.punctuation)) for paragraph in removeLines]
    wordCount = [len(paragraph.split(" ")) for paragraph in prunedParagraphs]
    maxCount = wordCount.index(max(wordCount))
    return prunedParagraphs[maxCount]

def longestWord(filename: str) -> str:
    validStatus = validFile(filename)
    if validStatus['valid']:

        fileHandle = open(filename, 'r')
        fileData = fileHandle.read()
        paragraphs = fileData.split("\n\n")
        paragraph = longestParagraph(paragraphs)
        return max(paragraph.split(" "), key=len)
    
    else:
        print(validStatus['message'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--filename', default='twain.txt', help='Name of the file to parse')
    args = parser.parse_args()
    
    word = longestWord(args.filename)
    print('Maximum word: ', word)
