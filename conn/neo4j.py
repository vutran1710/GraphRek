""" Neo4j Client
"""
from typing import List
from time import time
from random import randrange
from logzero import logger
from models import PostMeta
from decorator import singleton

from migrate import (
    unique_id,
    unique_label,
)


@singleton
class NeoClient:
    """ Neo4J DB Client
    """
    db = None

    def __init__(self, driver):
        self.db = driver
        try:
            with self.db.session() as session:
                session.run(unique_id)
                session.run(unique_label)
        except Exception as err:
            logger.warning('Constraint already exist!')

    def create_labels(self, labels: List[str]):
        """ creating Labels
        """
        count = 0
        with self.db.session() as session:
            for lab in labels:
                try:
                    session.run("CREATE (l:Label {name:$name})", name=lab)
                    count += 1
                except Exception as err:
                    logger.warning('Error: %s', err)

            return count

    def create_posts(self, posts: List[PostMeta], label: str):
        """ creating Posts
        """
        findq = """
        MATCH (p:Post {id:$post_id}), (l:Label {name:$label})
        MERGE (p)-[:LIKES]->(l)
        RETURN 1
        """

        query = """
        MATCH (lab:Label {name:$label})
        CREATE (:Post {id:$post_id, score:$post_score, created_at:$created_at})-[:LIKES]->(lab)
        RETURN 1
        """

        counter = 0
        with self.db.session() as session:
            for post in posts:
                result = session.run(findq, label=label, post_id=post.id)

                if result.single():
                    counter += 1
                else:
                    logger.warning("No post like that")
                    session.run(
                        query,
                        post_id=post.id,
                        post_score=post.score,
                        created_at=int(time()) -
                        randrange(1, 12) * 60 * 60 * 1000,
                        label=label,
                    )
                    counter += 1

            return counter

    def query_posts_by_labels(self, labels):
        pass
