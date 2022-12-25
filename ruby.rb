random = Random.new

test_size = 1_000_000
zeros = 0
ones = 0

(1..test_size).each do |i|
  if random.rand(2) == 0
    zeros += 1
  else
    ones += 1
  end
end

zeros_percentage = (zeros.to_f / test_size.to_f * 100.0).round(3)
ones_percentage = (ones.to_f / test_size.to_f * 100.0).round(3)

puts "Generated #{test_size} random samples and got"
puts "#{zeros} (#{zeros_percentage}%) zeros and"
puts "#{ones} (#{ones_percentage}%) ones."
