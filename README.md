<p align="center">
  <img src="https://drive.google.com/uc?id=10F8iwc-wW0PTSe3C3sia579Jl2ll5jfP" alt="logo" width="400">
</p>


Python module that calculates the probability density function, along with the median and standard deviation
for numerical datasets exhibiting Gaussian or Binomial distributions.


### Installation
Install libraries necessary for the project
```
pip install juan-stats
```

### Features Gaussian Distribution
- Read numerical datasets from a CSV file or  a Python list
```
gaussian_one = Gaussian()
gaussian_one.read_data_file("numbers.csv")

#another option is to read the data from a list
gaussian_one.data = [10,10,10,19,15,15,12,12,2,9,8,8,5] 
```

- Calculate the mean, standard deviation, and relative probability density at a specific point in a Gaussian distribution
```
print(gaussian_one.calculate_mean())
print(gaussian_one.calculate_stdev())
print(gaussian_one.pdf(49))
```

- Plot Histogram of the data or the Normalized histogram along with the probability density function 
```
gaussian_one.plot_histogram()
gaussian_one.plot_histogram_pdf()
```

### Features Binomial Distribution
- Calculate the mean, and standard deviation given some probability p and number of trials n
```
Binomial(0.4, 25)
#or
Binomial(p=0.4, n=25)
```

- Read numerical datasets from a CSV file or a Python list. The dataset should be composed of 0 and 1.
- Calculate the mean, standard deviation, and relative probability density at a specific point in a Binomial distribution
```
binomial_one.data = [0,1,0,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1] 
print(binomial_one.calculate_mean())
print(binomial_one.calculate_stdev())
print(binomial_one.pdf(5))
```

- Plot the probability density function of the binomial distribution
```
binomial_one.plot_bar_pdf()
```

#### Contributing
Submit a pull request and add other distributions you may like!
