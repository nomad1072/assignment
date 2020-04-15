from main import searchURL, sanitizedResponse

import unittest

class APITest(unittest.TestCase):
    
    def testURLLanguage(self):
        '''
            Should return URL only with limit query parameter when set
        '''
        baseURL = "https://api.github.com/search/repositories"
        output = "{}?q={}+language:{}".format(baseURL, "covid19", "Python")
        api = searchURL(baseURL, "covid19", "Python")
        self.assertEqual(api, output)
    
    def testURLQuery(self):
        '''
            Should set only query when passed just the search query
        '''
        baseURL = "https://api.github.com/search/repositories"
        output = "{}?q={}".format(baseURL, "covid19")
        api = searchURL(baseURL, "covid19", None)
        self.assertEqual(api, output)
    
    def testResponseLength(self):
        '''
            Response should give same number of items as input
        '''
        test_data = [{'full_name': 'test', 'html_url': '1', 'description': '2', 'language': '3'}, {'full_name': '4', 'html_url': '5', 'description': '67', 'language': '7'}]
        response = sanitizedResponse(test_data)
        self.assertEqual(len(test_data), len(response))
    
    def testResponseParameters(self):
        '''
            Each repository item in the response should contain the json parameters
        '''
        test_data = [{'full_name': 'test', 'html_url': '1', 'description': '2', 'language': '3'}, {'full_name': '4', 'html_url': '5', 'description': '67', 'language': '7'}]
        response = sanitizedResponse(test_data)
        repository_item = response[0]
        self.assertIn('name', repository_item)
        self.assertIn('url', repository_item)
        self.assertIn('description', repository_item)
        self.assertIn('language', repository_item)


if __name__ == "__main__":
    unittest.main()
