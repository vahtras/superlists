from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She ntoices the page title and heaer mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputboxx.get_attribute('placeholder'),
            'Enter a to-do item'
            )


        # She types "Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter the page updates, and the page lists
        #  "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacodk feathers' for row in rows)
            )

        # There is still a textbox inviting her to add another item. She
        # enters "Use peacock feathers to make a fly"
        self.fail('Finish the test')

    #The page updates, both items are shown

    #Will the site remember the list : a unique URL is generated

    #Visiting the URL it is still there

    #Satisfied

if __name__ == "__main__":
    #unittest.main(warnings='ignore') #not recognized
    unittest.main()

