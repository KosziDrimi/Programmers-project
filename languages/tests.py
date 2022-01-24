from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve 

from .views import index, add, show
from .models import Programmer
from .forms import ProgrammerForm, LanguageForm


class TestIndexURL(SimpleTestCase):
    
    def test_index_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)
        

class TestURLs(SimpleTestCase):
        
    def test_add_url_resolves(self):
        url = reverse('add')
        self.assertEqual(resolve(url).func, add)
    
    def test_show_url_resolves(self):
        url = reverse('show')
        self.assertEqual(resolve(url).func, show)
        

class TestModel(TestCase):

    def test_model_str(self):
        programmer = Programmer.objects.create(name='John', surname='Wood', position='Manager')
        self.assertEqual(programmer.__str__(), '<John Wood - Manager>')
        self.assertTrue(isinstance(programmer, Programmer))


class TestViews(TestCase):

    def test_add_view(self):
        url = reverse('add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'languages/add_form.html')

    def test_show_view(self):
        url = reverse('show')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'languages/show_form.html')


class TestProgrammerForm(TestCase):

    def test_valid_programmer_form(self):
        pro = Programmer.objects.create(name='Anthony', surname='Pretty', email='anthony@pretty.com',
                                        position='programmer', c_plus_plus_level=0, c_level=0, rust_level=0,
                                        python_level=5, java_level=3)

        data = {'name': pro.name, 'surname': pro.surname, 'email': pro.email, 'position': pro.position,
                'c_plus_plus_level': pro.c_plus_plus_level, 'c_level': pro.c_level, 'rust_level': pro.rust_level,
                'python_level': pro.python_level, 'java_level': pro.java_level}

        form = ProgrammerForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_programmer_form_missing_field(self):
        pro = Programmer.objects.create(name='Anthony', surname='Pretty', email='anthony@pretty.com',
                                        c_plus_plus_level=0, c_level=0, rust_level=0,
                                        python_level=5, java_level=3)

        data = {'name': pro.name, 'surname': pro.surname, 'email': pro.email,
                'c_plus_plus_level': pro.c_plus_plus_level, 'c_level': pro.c_level, 'rust_level': pro.rust_level,
                'python_level': pro.python_level, 'java_level': pro.java_level}

        form = ProgrammerForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_programmer_form_level_over_10(self):
        pro = Programmer.objects.create(name='Anthony', surname='Pretty',
                                        email='anthony@pretty.com', position='programmer',
                                        c_plus_plus_level=0, c_level=11, rust_level=0,
                                        python_level=5, java_level=3)

        data = {'name': pro.name, 'surname': pro.surname, 'email': pro.email, 'position': pro.position,
                'c_plus_plus_level': pro.c_plus_plus_level, 'c_level': pro.c_level, 'rust_level': pro.rust_level,
                'python_level': pro.python_level, 'java_level': pro.java_level}

        form = ProgrammerForm(data=data)
        self.assertFalse(form.is_valid())


class TestLanguageForm(TestCase):

    def test_valid_language_form(self):
        data = {'c_plus_plus_level': 0, 'c_level': 2, 'rust_level': 0, 'python_level': 5, 'java_level': 3}

        form = LanguageForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_language_form(self):
        data = {'c_plus_plus_level': 11, 'c_level': 2, 'rust_level': 0, 'python_level': 5, 'java_level': 3}

        form = LanguageForm(data=data)
        self.assertFalse(form.is_valid())
