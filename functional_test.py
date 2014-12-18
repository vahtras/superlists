from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)

    #Invitation to enter a to-do item


    #Enter "Buy peacock feathers" into a text box

    #On enter the page updates "1: Buy peacock feathers"

    #There is a textbox. Enter "Make a fly"

    #The page updates, both items are shown

    #Will the site remember the list : a unique URL is generated

    #Visiting the URL it is still there

    #Satisfied

if __name__ == "__main__":
    #unittest.main(warnings='ignore') #not recognized
    unittest.main()

