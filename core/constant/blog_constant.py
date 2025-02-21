from enum import Enum
from typing import List, Tuple


class BaseEnum(Enum):
    """Base Enum class with a reusable choices method."""

    @classmethod
    def get_choices(cls) -> List[Tuple[str, str]]:
        """ the first element will be enum name and second element will be the enum value """
        return tuple([(constant.value, constant.name.title().replace('_', ' ')) for constant in cls])

class BlogStatusConst(BaseEnum):
    """ This is used for the blog status"""
    DRAFT = "Draft"
    PUBLISHED = "Published"

    @classmethod
    def choices(cls):
        return [(tag.name, tag.value) for tag in cls]


class CategoryConst(BaseEnum):
    """This is used for blog categories"""
    TECHNOLOGY = "Technology"
    HEALTH = "Health"
    TRAVEL = "Travel"
    EDUCATION = "Education"

    @classmethod
    def choices(cls):
        return [(tag.name, tag.value) for tag in cls]
