inputs = <<-EOL
((a((bc)(de)))f)
(((zbcd)(((e)fg))))
ab((c))
EOL

outputs = <<-EOL
((a((bc)(de)))f)
((zbcd)((e)fg))
ab(c)
EOL

def rm_parentheses(line)
  index = 0
  opens, closes, values, buffer = [], [], [], []

  # append string indices to the related array
  line.each_char do |char|
    char == '(' ? opens << index : char == ')' ? closes << index : values << index
    index += 1
  end

  # group sequental values together e.g. [1,2,4] => [[1,2], [4]]
  grouped_values = values.slice_when { |prev, cur| cur != prev + 1}

  grouped_values.each do |group|
    first, last = group.first, group.last
    opener = opens.reverse.detect { |opener| opener < first }

    # sometimes there is no openers
    if opener
      closer = closes.detect { |closer| closer > last }
      opens -= [opener]
      closes -= [closer]
      buffer << [opener, closer, group]
    else
      buffer << [group]
    end
  end
  buffer.flatten.sort.map { |i| line[i] }.join
end

puts rm_parentheses "((a((bc)(de)))f)" #"(((zbcd)(((e)fg))))"
