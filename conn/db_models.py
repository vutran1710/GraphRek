from neomodel import (
    StructuredNode,
    StringProperty,
    IntegerProperty,
    # UniqueIdProperty,
    RelationshipTo,
    RelationshipFrom,
    ZeroOrMore,
)


class Post(StructuredNode):
    id = StringProperty(unique_index=True, required=True)
    score = IntegerProperty(required=True)
    has_label = RelationshipTo('Label', 'HAS_LABEL', cardinality=ZeroOrMore)


class Label(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    has_post = RelationshipFrom('Post', 'HAS_POST', cardinality=ZeroOrMore)
