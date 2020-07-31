class Award(object):
    def __init__(self, name=None, expires_in=None, quality=None):
        self.name = name
        self.expires_in = expires_in
        self.quality = quality

    def decrement_quality(self):
        if self.quality > 0 and self.name != "Blue Distinction Plus":
            self.quality -= 1


    def increment_quality(self):
        if self.quality < 50:
            self.quality += 1

    def remove_all_quality(self):
        self.quality = 0