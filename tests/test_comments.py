import unittest
from app.models import Pitches, User,Comments
from app import db

class CommentsTest(unittest.TestCase):
    def setUp(self):
        self.user_mwikali = User(username='mwikali', password ='apple', email = 'winniemwikali07@gmail.com')
        self.new_pitch = Pitches(title= 'Finance', content = 'Make more money with us.',user_id = self.user_ruweydha.id)
        self.new_comment = Comments(comment = 'You need to put more effort', pitch_id = self.new_pitch.id, user_id = self.user_ruweydha.id)

    def tearDown(self):   
        User.query.delete() 
        Comments.query.delete()
        Pitches.query.delete() 

    def test_check_instance_variables(self) :
        self.assertEquals(self.new_comment.comment, 'You need to put more effort') 
        self.assertEquals(self.new_comment.pitch_id, self.new_pitch.id)  
        self.assertEquals(self.new_comment.user_id, self.user_mwikali.id)  

    def test_save_pitch(self):
        self.new_comment.save_comment() 
        self.assertTrue(len(Comments.query.all())>0)  

    def test_get_comment_by_id(self):
        self.new_comment.save_comment() 
        got_comment = Comments.get_comment(self.new_pitch.id) 
        self.assertTrue(len(got_comment)==1) 