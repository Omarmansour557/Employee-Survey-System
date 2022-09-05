from urllib import response
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.

class SignupPageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
    
    def test_signup_view_name(self):
        response = self.client.get(reverse('signup'))
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')
    
    def test_signup_form(self):
        response = self.client.post(reverse('signup'),
        data={
            "username":"testEmployee",
            "name":"Test Employee",
            "department":"Test Department",
            "job_title":"Test Job",
            "password1":"testingg",
            "password2":"testingg",
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "testEmployee")
        self.assertEqual(get_user_model().objects.all()[0].employee.name, "Test Employee")
        self.assertEqual(get_user_model().objects.all()[0].employee.department, "Test Department")
        self.assertEqual(get_user_model().objects.all()[0].employee.job_title, "Test Job")
        