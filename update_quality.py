from string_constants import BLUE_COMPARE, BLUE_FIRST, BLUE_STAR

def __handle_expired_award(award):
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

        award.age_one_day()
        __handle_expired_award(award)

    