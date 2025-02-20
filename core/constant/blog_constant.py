from enum import Enum


class BlogStatusConst(Enum):
    """ This is used for the blog status"""
    DRAFT = "Draft"
    PUBLISHED = "Published"

    @classmethod
    def choices(cls):
        return [(tag.name, tag.value) for tag in cls]


class CategoryConst(Enum):
    """This is used for blog categories"""
    TECHNOLOGY = "Technology"
    HEALTH = "Health"
    TRAVEL = "Travel"
    EDUCATION = "Education"

    @classmethod
    def choices(cls):
        return [(tag.name, tag.value) for tag in cls]
