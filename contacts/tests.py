from django.test import TestCase, LiveServerTestCase

from django.utils import timezone
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
from contacts.models import Person


class ContactsAppTestCase(LiveServerTestCase):
    fixtures = ['admin_user.json']
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_create_new_person_via_admin(self):
        self.browser.get(self.live_server_url + '/admin/')

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('viktoria')

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('123')
        password_field.send_keys(Keys.RETURN)

    
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)

        person_links = self.browser.find_elements_by_link_text('Persons')
        self.assertEquals(len(person_links), 1)
    def test_index_error_message(self):
        Person.objects.get().delete()
        
        self.browser.get(self.live_server_url+'/contacts/')
        
        err_field=self.browser.find_element_by_id('err_field')
        self.assertIn('Error:', err_field.text)
    def test_index_element_creation_if_person_in_db_from_fixtures(self):
        
        self.browser.get(self.live_server_url+'/contacts/')
        
        name_field=self.browser.find_element_by_id('name_field')
        self.assertIn('Oleg', name_field.text)
        
        surname_field=self.browser.find_element_by_id('surname_field')
        self.assertIn('Drebot', surname_field.text)
        
        date_field=self.browser.find_element_by_id('date_field')
        self.assertIn('1992-08-02', date_field.text)
        
        bio_field=self.browser.find_element_by_id('bio_field')
        self.assertIn('Bio:', bio_field.text)
        
        email_field=self.browser.find_element_by_id('email_field')
        self.assertIn('E-mail:', email_field.text)
        
        jabber_field=self.browser.find_element_by_id('jabber_field')
        self.assertIn('Jabber:', jabber_field.text)
        
        skype_field=self.browser.find_element_by_id('skype_field')
        self.assertIn('Skype:', skype_field.text)
        
        other_field=self.browser.find_element_by_id('other_field')
        self.assertIn('Other contacts:', other_field.text)
        
            
    def test_can_click_on_email_via_index(self):
        
        self.browser.get(self.live_server_url+'/contacts/')
        
        email_field=self.browser.find_element_by_id('email_field')
        self.assertIn('E-mail', email_field.text)
        
        email_links=self.browser.find_elements_by_link_text('drobovike@gmail.com')
        self.assertEquals(len(email_links), 1)

class PersonModelTest(TestCase):
    def test_creating_a_new_person_and_saving_it_to_the_database(self):
        per = Person()
        per.name = "Neko"
        per.surname="Miko"
        per.dateOfBirth = "1900-04-05"
        per.bio="Bio"
        per.jabber="jabber@j.com"
        per.email="e@mail.com"
        per.skype="skypeID"
        per.otherContact="Other"

        per.save()

        all_persons_in_database = Person.objects.all()
        self.assertEquals(len(all_persons_in_database), 2)
        test_person_in_database = all_persons_in_database[1]
        self.assertEquals(test_person_in_database, per)

        self.assertEquals(test_person_in_database.name, "Neko")
        self.assertEquals(test_person_in_database.surname, "Miko")
        self.assertEquals(test_person_in_database.dateOfBirth, datetime.date(1900, 4, 5))
        self.assertEquals(test_person_in_database.bio, "Bio")
        self.assertEquals(test_person_in_database.jabber, "jabber@j.com")
        self.assertEquals(test_person_in_database.email, "e@mail.com")
        self.assertEquals(test_person_in_database.skype, "skypeID")
        self.assertEquals(test_person_in_database.otherContact, "Other")
