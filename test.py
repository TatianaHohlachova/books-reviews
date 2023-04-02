import pytest
from main import app, db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

def test_review_add():
    with app.test_client() as client:
        response = client.post('/add-review', json={
            'book_name': 'ASDF',
            'rating': 3,
            'review': 'QWERTY'
        })
        assert response.status_code == 200

def test_get_book_id():
    with app.test_client() as client:
        response = client.post('/search', json={
            'query': 'ASDF',
        })
        assert response.status_code == 200
        assert int(response.json['book_id']) == 1

