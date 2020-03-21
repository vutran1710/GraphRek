from logzero import logger  # noqa
import pytest  # noqa
from utils import CONFIG
from neomodel import db, install_all_labels, config
from conn.db_models import (
    Post,
    Label,
)

db.set_connection(CONFIG['NEO4J_URL'])
install_all_labels()


def test_02_create_posts():
    labels = [
        'food',
        'travel',
        'feeling',
        'music',
    ]

    label_obj = []
    for label in labels:
        entity = Label(name=label)
        entity.save()
        label_obj.append(entity)

    posts = [
        'abc',
        'def',
        'ghi',
        'ijk',
    ]

    for post_id in posts:
        post_obj = Post(id=post_id, score=10)
        post_obj.save()
        post_obj.has_label.connect(label_obj[0])
        label_obj[0].has_post(post_obj).save()
