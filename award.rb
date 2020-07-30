Award = Struct.new(:name, :expires_in, :quality) do
  def greeting
    "Hello #{name}!"
  end
end

award = Award.new("Dave", 12, 50)
puts(award.name)     #=> "Dave"
puts(award.greeting) #=> "Hello Dave!"
