from string_constants import BLUE_DISTINCTION_PLUS

class Award(object):
    def __init__(self, name=None, expires_in=None, quality=None):
        self.name = name
        self.expires_in = expires_in
        self.quality = quality

    def decrement_quality(self):
        if self.quality > 0 and self.name != BLUE_DISTINCTION_PLUS:
            self.quality -= 1

    def increment_quality(self):
        if self.quality < 50:
            self.quality += 1

    def remove_all_quality(self):
        self.quality = 0

    def age_one_day(self):
        if self.name != BLUE_DISTINCTION_PLUS:
            self.expires_in -= 1