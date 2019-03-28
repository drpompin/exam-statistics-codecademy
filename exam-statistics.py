#Your students just took their first test. It's time to see how everyone did. Let's write a program to compute the mean, variance, and standard deviation of the test scores.

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print grade

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores:
    sq_diff = (average - score) ** 2
    variance += sq_diff
  return variance / float(len(scores))


def grades_std_deviation(variance):
  return variance ** 0.5

variance = grades_variance(grades)



print 'grades:', print_grades(grades)
print 'sum of grades:', grades_sum(grades)
print 'average:', grades_average(grades)
print 'variance:', grades_variance(grades)
print 'std deviation:', grades_std_deviation(variance)

