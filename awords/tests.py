from django.test import TestCase
from .models import Projects,Profile,Rates,Comments

class TestProjects(TestCase):
    def setUp(self):
        self.new_project=Projects(name='MOT',image='mot.jpg',description='movie recommendation engine',location='addis',link='www.mot.com',screen1='motty.png',screen2='motyy.png')
    def test_instace(self):
        self.assertTrue(isinstance(self.new_project,Projects))
    def test_initialization(self):
        self.assertEqual(self.new_project.name,"MOT")
        self.assertEqual(self.new_project.image,"mot.jpg")
        self.assertEqual(self.new_project.description,"movie recommendation engine")
        self.assertEqual(self.new_project.link,"www.mot.com")
        self.assertEqual(self.new_project.location="addis")
        self.assertEqual(self.new_project.screen1,"motty.png")
        self.assertEqual(self.new_project.screen2,"motyy.png")

class TestProfile(TestCase):
    def setUp(self):
        self.new_profile=Profile(profile='tay',bio='back at it')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))
    def test_initialization(self):
        self.assertEqual(self.new_profile.profile,'tay')
        self.assertEqual(self.new_profile.bio,'back at it')

class TestRating(TestCase):
    def setUp(self):
        self.new_rating=Rates(design=0,usability=0,content=0)
    def test_instance(self):
        self.assertTrue(isinstance(self.new_rating,Rates))
    def test_initialization(self):
        self.assertEqual(self.new_rating.design,0)
        self.assertEqual(self.new_rating.usability,0)
        self.assertEqual(self.new_rating.content,0)
class TestComments(TestCase):
    def setUp(self):
        self.new_comment=Comments(comment="nice one!",pro_id=0)
    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comments))
    def test_initialization(self):
        self.assertEqual(self.new_comment.comment,"nice one!")
        self.assertEqual(self.new_comment.pro_id,0)
