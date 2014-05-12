def findPayment(loan, r, m):
	"""loan, r为浮点数，m为整数
	返回贷款loan,利率为r,时间为m, 每月的支付数量"""
	return loan * ((r * (r + 1) ** m) / ((1 + r) ** m - 1))

class Mortgage(object):
	def __init__(self, loan, annRate, months):
		self.loan = loan
		self.rate = annRate /12.0
		self.months = months
		self.paid = [0.0]
		self.owed = [loan]
		self.payment = findPayment(loan, self.rate, months)
		self.legend = None

	def makePayment(self):
		self.paid.append(self.payment)
		reduction = self.payment - self.owed[-1] * self.rate
		self.owed.append(self.owed[-1] - reduction)

	def getTotalPaid(self):
		return sum(self.paid)

	def __str__(self):
		return self.legend

class Fixed(Mortgage):
	"""docstring for Fixed"""
	def __init__(self, loan, r, months):
		Mortgage.__init__(self, loan, r, months)
		self.legend = 'Fixed, rate:' + str(r * 100) + '%'

class FixedWithPts(Mortgage):
	"""docstring for FixedWithPts"""
	def __init__(self, loan, r, months, pts):
		Mortgage.__init__(self, loan, r, months)
		self.pts = pts
		self.paid =  [loan * (pts / 100)]
		self.legend = 'Fixed, rate:' + str(r * 100) + '%, ' + str(pts) + ' points'

class TwoRate(Mortgage):
	"""docstring for TwoRate"""
	def __init__(self, loan, r, months, teaserRate, teaserMonths):
		Mortgage.__init__(self, loan, teaserRate, months)
		self.teaserRate = teaserRate
		self.teaserMonths = teaserMonths
		self.nextRate = r / 12
		self.legend = str(teaserRate * 100) + '% for ' + str(self.teaserMonths)  + ' months, \n then ' + str(r * 100) + '%'

	def makePayment(self):
		if (len(self.paid)) == self.teaserMonths + 1:
			self.rate = self.nextRate
			self.payment = findPayment(self.owed[-1], self.rate, self.months - self.teaserMonths)
		Mortgage.makePayment(self)


def compareMortgage(amt, years, fixedRate, pts, ptsRate, varRate1, varRate2, varMonths):
	totMonth = 12 *years
	fixed1 = Fixed(amt, fixedRate, totMonth)
	fixed2 = FixedWithPts(amt, ptsRate, totMonth, pts)
	twoRate = TwoRate(amt, varRate2, totMonth, varRate1, varMonths)

	morts = [fixed1, fixed2, twoRate]

	for m in range(totMonth):
		for mort in morts:
			mort.makePayment()

	for m in morts:
		print m
		print ' Total payment = $' + str(int(m.getTotalPaid()))

compareMortgage(
	amt = 200000,
	years = 30,
	fixedRate = 0.07,
	pts = 3.25,
	ptsRate = 0.05,
	varRate1=0.045,
	varRate2 = 0.095,
	varMonths = 48)
