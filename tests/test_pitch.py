import unittest
from app.models import Pitches, User
from app import db

class TestPitch(unittest.TestCase):
    def setUp(self):
        self.user_ruweydha = User(username='ruweydha', password ='potato', email = 'ruweydhaabdinoor@gmail.com')
        self.new_pitch = Pitches(title= 'Technology', content = 'Software development',user_id = self.user_ruweydha.id)

    def tearDown(self):
        Pitches.query.delete() 
        User.query.delete() 

    def test_check_instance_variables(self) :
        self.assertEquals(self.new_pitch.title, 'Technology') 
        self.assertEquals(self.new_pitch.content, 'Software development')  
        self.assertEquals(self.new_pitch.user_id, self.user_ruweydha.id)  

    def test_save_pitch(self):
        self.new_pitch.save_pitch()  
        self.assertTrue(len(Pitches.query.all())>0)  

    def test_get_pitch_by_id(self):
        self.new_pitch.save_pitch() 
        got_pitch = Pitches.get_pitch(self.user_ruweydha.id) 
        self.assertTrue(len(got_pitch)==1) 