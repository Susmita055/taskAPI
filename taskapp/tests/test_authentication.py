from django.http import response
from django.test import TestCase,client
from django.urls import reverse
import pdb

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
import json

class RegisterTests(TestCase):
    def setUp(self) -> None:
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.FirstName = 'testuser'
        self.LastName='gmail'
        self.Email = 'adhikari372@gmail.com'
        self.Password = 'admin'


        self.valid_payload = {
            'Title': 'nothi',
            'Description': "anything",
            'TaskStatus': True,
            'TaskID': 1
        }
        self.invalid_payload = {
            'Title': 'nothi',
            'Description': "anything",
            'TaskStatus': True,
            'TaskID': '232'
        }


    def test_register_page_url(self):
        response = self.client.get("/register/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='registration.html')

    def test_register_page_view_name(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='registration.html')

    def test_register_user(self):
        response = self.client.post(reverse('register'), data={
            'FirstName': self.FirstName,
            'LastName':self.LastName,
            'Email': self.Email,
            'Password': self.Password,
            
        })
        self.assertEqual(response.status_code, 200)

    def test_user_cannot_login_withoutRegister(self):
        response = self.client.post(reverse('login'), data={
            'username': 'admin',
            'password': 'admin',
            
        })
        self.assertEqual(response.status_code, 403)

 
        User = get_user_model()
        user = User.objects.create_user('task', 'task@gmail.com', 'task')



    def test_create_invalid_Task(self):
        response = self.client.post(
            reverse('task'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        


       

    
        








    




