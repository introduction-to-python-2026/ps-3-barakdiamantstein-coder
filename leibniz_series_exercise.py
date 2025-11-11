def approximate_pi(n_terms):
  sum = 0
  for i in range(n_terms):
      sum = sum + ((-1) ** i) / ((2 * i) + 1) 
      i = i + 1
  pi = sum * 4
  return(pi)
