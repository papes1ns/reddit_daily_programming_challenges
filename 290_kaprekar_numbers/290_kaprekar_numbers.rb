# input: range of numbers, e.g. "101 9000"
# output: kaprekar numbers in the range of numbers from input

# In mathematics, a Kaprekar number for a given base is a non-negative integer,
# the representation of whose square in that base can be split into two parts
# that add up to the original number again. For instance, 45 is a Kaprekar
# number, because 45^2 = 2025 and 20+25 = 45.

def kaprekar_number?(n)
  n_squared = (n**2).to_s
  len = n_squared.length
  len.times do |i|
    part1 = n_squared[0..i].to_i
    part2 = n_squared[(i+1)...len].to_i
    break if part2.zero?
    return true if part1 + part2 == n
  end
  false
end

start = ARGV[0].to_i
finish = ARGV[1].to_i

start.upto(finish) do |n|
  puts n if kaprekar_number? n
end
