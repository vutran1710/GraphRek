unique_id = """
CREATE CONSTRAINT unique_id
ON (p:Post) ASSERT p.id IS UNIQUE
"""

unique_label = """
CREATE CONSTRAINT unique_label
ON (l:Label) ASSERT l.name IS UNIQUE
"""
