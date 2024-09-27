# running this module will call this function when importing
from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

"""main function that runs other functions"""

__author__ = "730763981"

x: str = "123"
y: str = "abc"

get_coords(x, y)
# added after the fact to get rid of nonuse error
# not part of lesson
concat(x, y)
