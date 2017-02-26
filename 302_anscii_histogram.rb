class Histogram

  def initialize(data, char)
    @points = []
    @char   = char
    data.split("\n").each_with_index do |line, index|
      datas = line.split.map(&:to_i)
      case index
      when 0
        @start_x, @end_x, @start_y, @end_y = datas
      when 1
        # not used
        # @total_records = datas[0]
      else
        @points << {
          :start     => datas[0],
          :end       => datas[1],
          :frequency => datas[2]
        }
      end
    end
    @points = @points.sort_by{ |point| point[:frequency] }.reverse
  end

  def print
    histogram = []
    row       = (@start_x..@end_x).step(10).to_a.map{ |e| [e, " "] }.flatten
    @end_y.downto(@start_y).each do |y|
      @points.each do |point|
        if point[:frequency] == y
          row[row.index(point[:start]) + 1] = @char
        end
      end
      histogram << y.to_s + row.map { |e| e != @char ? " " * e.to_s.length : @char }.join
    end
    histogram << " " * @end_y.to_s.length + row.map { |e| e == @char ? " " : e }.join
    puts histogram.join("\n")
  end

end

input = <<-EOF
140 190 1 8
5
140 150 1
150 160 0
160 170 7
170 180 6
180 190 2
EOF

Histogram.new(input, "*").print
