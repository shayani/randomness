random = Random.new

test_size = 1_000_000

result_array = []

(1..test_size).each do |i|
  result_array << random.rand(2)
end

zeros = result_array.count(0)
zeros_percentage = (zeros.to_f / test_size.to_f * 100.0).round(3)

ones = result_array.count(1)
ones_percentage = (ones.to_f / test_size.to_f * 100.0).round(3)

puts "Generated #{test_size} random samples and got"
puts "#{zeros} (#{zeros_percentage}%) zeros and"
puts "#{ones} (#{ones_percentage}%) ones."
