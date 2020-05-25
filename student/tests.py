from django.test import TestCase, Client
from .models import Student


# Create your tests here.

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name='Alroy',
            sex=1,
            email='sqrtln@163.com',
            profession='softwaredeveloper',
            qq='347625023',
            phone='18395551111',
        )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='ligen',
            sex=1,
            email='347625023@qq.com',
            profession='AI_developer',
            qq='123456',
            phone='32165478921',
        )
        self.assertEqual(student.sex_show, '男', '性別字段內容跟展示不一致')

    def test_filter(self):
        Student.objects.create(
            name='tongji',
            sex=1,
            email='sjpgmoe@gmail.com',
            profession='programmer',
            qq='9876543',
            phone='12345678910',
        )
        name = 'abraxas'
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(), 1, '應該只存在一個名稱爲{}的記錄'.format(name))

    def test_get_index(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200, 'status code must be 200!')

    def test_post_student(self):
        client = Client()
        data = dict(
            name='test_for_post',
            sex=1,
            email='333@dd.com',
            profession='programmer',
            qq='4646746',
            phone='13234676123',
        )
        response = client.post('/', data)
        self.assertEqual(response.status_code, 302, 'status code must be 302!')

        response = client.get('/')
        self.assertTrue(b'test_for_post' in response.content, 'response content must contain `test_for_post`')
