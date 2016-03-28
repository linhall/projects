import unittest

def match(candidate, job):
	c = candidate['min_salary']
	j = job['max_salary']
	c_pct = c * .10
	c_adj = c - c_pct

	if (int(c) <= j) or (int(c_adj) <= j):
		print c,j
		return True
	else:
		return False 


# print match(12000, 19000)
# print match(120000, 19000)
# print match()

# Test.describe("Basic tests")
candidate1 = { 'min_salary': 120000 }
candidate2 = { 'min_salary': 190000 }
job1 = { 'max_salary': 130000 }
job2 = { 'max_salary': 80000 }
job3 = { 'max_salary': 171000 }

print match(candidate1, job1)
print match(candidate1, job3)
print match(candidate2, job3)

print match(candidate1, job2)
print match(candidate2, job1)
print match(candidate2, job2)

# Test.it('should throw when a candidate has no min_salary')
# Test.expect_error("Should throw error", lambda a: match({}, job2))

# Test.it('should throw when a job has no max_salary')
# Test.expect_error("Should throw error", lambda a: match(candidate1, {}))