# Calculating the sample variance

If we do not know the exact value of the expectation for the distribution we should use the following estimator for the sample variance:

![](https://render.githubusercontent.com/render/math?math=S^2=\frac{1}{n-1}\sum_{i=1}^{n}[X-\overline{X}]^2\qquad\textrm{where}\qquad\overline{X}=\frac{1}{n}\sum_{i=1}^{n}X_i)

which we can easily rearrange to:

![](https://render.githubusercontent.com/render/math?math=S^2=\frac{n}{n-1}\left[\left(\frac{1}{n}\sum_{i=1}^{n}X_i^2\right)^2-\overline{X}^2\right])

__Your task in this exercise is to compute this quantity for the data in the NumPy array called radii.__  The data in this array are the radii of the bubbles that we looked at in the exercise on biased estimators.  To pass the test the variable S2 needs to be set equal to the sample variance computed of this data that is computed using the formula given above.  The correct value of this quantity will then be output in the black square if the code is written correctly.

N.B _I always compute variance using the second formula here rather than the first as the mean for the squares of the random variables and the mean for the random variable can then be computed in a single loop._  
