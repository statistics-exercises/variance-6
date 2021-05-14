# Calculating the sample variance

If we do not know the exact value of the expectation for the distribution we should use the following estimator for the sample variance:

![](https://render.githubusercontent.com/render/math?math=S^2=\frac{1}{n-1}\sum_{i=1}^{n}[X-\overline{X}]^2\qquad\textrm{where}\qquad\overline{X}=\frac{1}{n}\sum_{i=1}^{n}X_i)

which we can easily rearrange to:

![](https://render.githubusercontent.com/render/math?math=S^2=\frac{n}{n-1}\left[\left(\frac{1}{n}\sum_{i=1}^{n}X_i^2\right)^2-\overline{X}^2\right])

__Your task in this exercise is to write a function called `variance` that calculates an estimate of this quantity.__  This function should take in a single number `n`.  Within the function you should then generate `n` uniform 
random variables that all lie between 0 and 1.  From these `n` random variables you should then calculate an estimate for the variance of the underlying distribution using the second of the two expressions above.  
