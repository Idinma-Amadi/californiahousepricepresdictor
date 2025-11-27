For the cleaning process. I removed:
- missing values (using .dropna)
- categorical values (using .drop)

why?
- We are goin to use Linear regression model and Linear regression model doesn't work with missing values or categorical  values (non numeric values - strings)