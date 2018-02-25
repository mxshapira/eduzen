import pytest
from datetime import datetime
from blog.models import Post

from django.contrib.auth.models import User


@pytest.fixture()
def superuser():
    user = User.objects.create_superuser('myuser', 'myemail@test.com', 'pswd')
    return user


@pytest.fixture()
@pytest.mark.django_db
def post(mocker):
    user = User.objects.create_superuser('myuser', 'myemail@test.com', 'pswd')
    post = Post(
        title='My post1', slug='my-post1', text='Lorem ipsum1', author=user,
        published_date=datetime.now(), created_date=datetime.now())
    post.save()
    return post


@pytest.mark.django_db
def test_create_post(superuser):
    post = Post(
        title='My post1', slug='my-post1', text='Lorem ipsum1', author=superuser,
        published_date=datetime.now(), created_date=datetime.now())

    post.save()
    post_expected = Post.objects.get()
    assert post_expected


@pytest.mark.django_db
def test_modified_post(post):
    post = Post.objects.filter(id=post.id)[0]
    post.text = 'other text'

    assert post
