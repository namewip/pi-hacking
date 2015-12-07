require 'bigdecimal'

class Integer
	def fact
		f = 1
		for i in 1..self
			f *= i
		end
		f
  	end
end

prec = 3
BigDecimal::mode(BigDecimal::ROUND_MODE, BigDecimal::ROUND_HALF_UP)
@decprec = 2500 * prec

def calcit(maxiter)
	s = BigDecimal.new('0', @decprec)
	
	maxiter.times do |n|
		s += (-1) ** n * (6 * n).fact * (13591409 + n * BigDecimal.new(545140134, @decprec)) /
			n.fact ** 3 / (3 * n).fact / (100100025 * 8 * BigDecimal.new(327843840, @decprec)) ** n
	end

	return 53360 * BigDecimal.new(640320, @decprec) ** BigDecimal.new('0.5', @decprec) / s
end

puts(calcit(50 * prec).to_s("#{3750 * prec}F"))
