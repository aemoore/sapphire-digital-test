require 'award'

def update_quality(awards)
  awards.each do |award|

    if award.name != 'Blue First' && award.name != 'Blue Compare'
      award.decrement_quality
    else
      award.increment_quality
      if award.name == 'Blue Compare'
        if award.expires_in < 11
          award.increment_quality
        end
        if award.expires_in < 6
          award.increment_quality
        end
      end
    end

    if award.name != 'Blue Distinction Plus'
      award.expires_in -= 1
    end

    if award.expires_in < 0
      if award.name != 'Blue First'
        if award.name != 'Blue Compare'
          award.decrement_quality
        else
          award.remove_all_quality
        end
      else
        award.increment_quality
      end
    end
    
  end
end
