from . import api_bp
from flask import jsonify, request
from flask_login import current_user, login_required
from pydantic import BaseModel, ValidationError, StringConstraints
from typing import Annotated
from my_app.models import Post, Comment
from my_app import db

class CommentSchema(BaseModel):
    text: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


@api_bp.route('/post/<int:post_id>/comment', methods=['POST'])
@login_required
def add_comment(post_id):
    post = Post.query.get_or_404(post_id)
    json_data = request.get_json()

    if not json_data:
        return jsonify({'error': 'No data'}), 400
    
    try:
        comment_data = CommentSchema(**json_data)
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400
    
    new_comment = Comment(
        text=comment_data.text,
        author=current_user,
        post=post   
    )
    db.session.add(new_comment)
    db.session.commit()

    return jsonify({
        'id': new_comment.id,
        'text': new_comment.text,
        'date_created': new_comment.date_created.strftime('%Y-%m-%d %H:%M'),
        'author': {
            'id': new_comment.author.id,
            'username': new_comment.author.username
        }
    })


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