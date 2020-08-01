def update_quality(awards):
    for award in awards:
        if award.name != 'Blue First' and award.name != 'Blue Compare':
            award.decrement_quality()
            if award.name == 'Blue Star':
                award.decrement_quality()
        else:
            award.increment_quality()
            if award.name == 'Blue Compare':
                if award.expires_in < 11:
                    award.increment_quality()
                if award.expires_in < 6:
                    award.increment_quality()
            else:
                if award.name == 'Blue Star':
                    #if award.expires_in > 11:
                        # award.increment_quality()
                    if award.expires_in > 6:
                        award.increment_quality()

        if award.name != 'Blue Distinction Plus':
            award.expires_in -= 1

        if award.expires_in < 0:
            if award.name != 'Blue First':
                if award.name != 'Blue Compare':
                    award.decrement_quality()
                    if award.name == 'Blue Star':
                        award.decrement_quality()
                else:
                    award.remove_all_quality()
            else:
                award.increment_quality()

