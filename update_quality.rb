require 'award'
require 'strings'

def update_quality(awards)
  awards.each do |award|

    if award.name != BLUE_FIRST && award.name != BLUE_COMPARE
      award.decrement_quality
      if award.name == BLUE_STAR
        award.decrement_quality
      end
    else
      award.increment_quality
      if award.name == BLUE_COMPARE
        if award.expires_in < 11
          award.increment_quality
        end
        if award.expires_in < 6
          award.increment_quality
        end
      end
    end

    if award.name != BLUE_DISTINCTION_PLUS
      award.expires_in -= 1
    end

    if award.expires_in < 0
      if award.name != BLUE_FIRST
        if award.name != BLUE_COMPARE
          award.decrement_quality
          if award.name == BLUE_STAR
            award.decrement_quality
          end
        else
          award.remove_all_quality
        end
      else
        award.increment_quality
      end
    end
    
  end
end
