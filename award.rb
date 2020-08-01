Award = Struct.new(:name, :expires_in, :quality) do

  def decrement_quality
    if self.quality > 0 && self.name != 'Blue Distinction Plus'
      self.quality -= 1
    end
  end

  def increment_quality
    if self.quality < 50
      self.quality += 1
    end
  end

  def remove_all_quality
    self.quality = 0
  end

end
