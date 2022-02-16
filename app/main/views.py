from flask import redirect, render_template, url_for, abort,request
from flask_login import current_user, login_required
from . import main
from ..models import Comments, User, Pitches, Category
from .forms import UpdateProfile, PitchesForm, CommentsForm
from .. import db, photos
import markdown2

@main.route('/')
def index():
    pitches = Pitches.query.all()
    return render_template('index.html', pitches = pitches, pitcher = pitches)

@main.route('/user/<uname>') 
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    pitches = Pitches.get_pitch(user.id)

    if user is None:
        abort(404)

    return render_template('profile/profile.html', user = user, pitches = pitches)    

@main.route('/user/<uname>/update', methods = ['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    
    if user is None:
        abort(404)

    form = UpdateProfile() 
    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()  

        return redirect(url_for('.profile', uname = user.username)) 
    return render_template('profile/update_profile.html', form = form)

@main.route('/user/<uname>/update/pic', methods=['POST']) 
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first() 
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

    return redirect(url_for('main.profile',uname=uname))  

@main.route('/user/pitch/new/<int:id>', methods =['GET', 'POST'])
@login_required
def new_pitch(id):
    form = PitchesForm()
    user = User.query.filter_by(id = id).first()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        category = form.category.data
        pitch_category = Category.query.filter_by(id = category).first()
        new_pitch = Pitches(title = title, content = content, pitcher = current_user, categories = pitch_category)
        new_pitch.save_pitch()
        return redirect(url_for('.profile', uname = user.username ))

    return render_template('new_pitch.html', pitch_form = form, user = user.username)

@main.route('/user/comment/new/<int:id>', methods =["GET", "POST"])
@login_required
def comment(id):
    form = CommentsForm()
    comments = Comments.query.filter_by(pitch_id = id).all()
    pitch = Pitches.query.filter_by(id = id).first()

    if form.validate_on_submit():
        comment_submitted = form.comment.data
        new_comment = Comments(comment= comment_submitted, commenter = current_user, comments = pitch )
        new_comment.save_comment()

    return render_template('new_comments.html', comment_form = form, comments = comments, pitch = pitch)  

@main.route('/category/<int:id>')  
def category(id) :
    pitches = Pitches.query.filter_by(category_id = id).all()

    return render_template('category.html', categories = pitches)
