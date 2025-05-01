from time_block import TimeBlock
from datetime import time
BEGINNER = 0
INTERMEDIATE = 1
ADVANCED = 2
CLASS_LIMIT = 7
BLOCK_ONE = TimeBlock(time(8, 0), time(9, 0))
BLOCK_TWO = TimeBlock(time(9, 15), time(10, 15))
BLOCK_THREE = TimeBlock(time(10, 45), time(11, 45))
LUNCH_TIME = TimeBlock(time(11, 45), time(12, 45))
BLOCK_FOUR = TimeBlock(time(12, 45), time(1, 45))
BLOCK_FIVE = TimeBlock(time(2, 0), time(3, 0))
BLOCK_SIX = TimeBlock(time(3, 30), time(4, 30))
LEVEL_DICT = {
    BEGINNER: "Beginner",
    INTERMEDIATE: "Intermediate",
    ADVANCED: "Advanced"
}

TIME_BLOCKS = [BLOCK_ONE, BLOCK_TWO, BLOCK_THREE, BLOCK_FOUR, BLOCK_FIVE, BLOCK_SIX]