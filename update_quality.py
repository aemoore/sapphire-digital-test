BLUE_FIRST = 'Blue First'
BLUE_COMPARE = 'Blue Compare'
BLUE_STAR = 'Blue Star'
BLUE_DISTINCTION_PLUS = 'Blue Distinction Plus'

def update_quality(awards):
    for award in awards:
        if award.name != BLUE_FIRST and award.name != BLUE_COMPARE:
            award.decrement_quality()
            if award.name == BLUE_STAR:
                award.decrement_quality()
        else:
            award.increment_quality()
            if award.name == BLUE_COMPARE:
                if award.expires_in < 11:
                    award.increment_quality()
                if award.expires_in < 6:
                    award.increment_quality()
            else:
                if award.name == BLUE_STAR:
                    if award.expires_in > 11:
                        award.increment_quality()
                    if award.expires_in > 6:
                        award.increment_quality()

        if award.name != BLUE_DISTINCTION_PLUS:
            award.expires_in -= 1

        if award.expires_in < 0:
            if award.name != BLUE_FIRST:
                if award.name != BLUE_COMPARE:
                    award.decrement_quality()
                    if award.name == BLUE_STAR:
                        award.decrement_quality()
                else:
                    award.remove_all_quality()
            else:
                award.increment_quality()

