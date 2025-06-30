from . import api_bp
from flask import jsonify
from flask_login import current_user, login_required
from my_app.models import Post, User
from my_app import db

@api_bp.route('/post/<int:post_id>/like', methods=['POST'])
@login_required
def like_post(post_id):
    post = Post.query.get_or_404(post_id)
    if current_user in post.liked_by_users:
        post.liked_by_users.remove(current_user)
        db.session.commit()
        return jsonify({'likes': post.likes_count, 'liked': False}), 200
    
    else: 
        post.liked_by_users.append(current_user)
        db.session.commit()
        return jsonify({'likes': post.likes_count, 'liked': True}), 200