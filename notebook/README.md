eda.ipynb: EDA for Financial News and Stock Price Integration Dataset
AAPL,AMZN,GOOG,META,MSFT,NVDA,TSLA.ipynb for  Quantitative Analysis of Financial Datasets
cra.ipynb: Correlation analysis between news and stock movement


If import spacy creates an error of the following type:
ValueError: numpy.dtype size changed, may indicate binary incompatibility. Expected 96 from C header, got 88 from PyObject

The error you're encountering is related to a version mismatch between numpy and spacy, which can occur when different versions of libraries are not fully compatible with each other. Here's how you can resolve this issue:

Step 1: Update numpy
Start by ensuring that numpy is updated to the latest version:
pip install --upgrade numpy

Step 2: Reinstall spacy
Sometimes, reinstalling spacy after updating numpy can resolve the issue:
pip uninstall spacy
pip install spacy

Step 3: Check for Compatibility
If the problem persists, ensure that all related libraries (spacy, numpy, etc.) are compatible. You can do this by specifying versions known to work well together:
pip install numpy==1.24.2 spacy==3.5.0

Step 4: Rebuild the spacy Model
If you've already installed a model like en_core_web_sm, you may need to reinstall it:
python -m spacy download en_core_web_sm

Step 5: Restart the Kernel
After performing these updates, restart your Jupyter notebook kernel to ensure that the changes take effect.

## Sentimental analysis output

Here's what each of these statistics indicates:

Understanding Sentiment Scores
Sentiment scores typically range from -1 to 1, where:
-1 represents very negative sentiment.
0 represents neutral sentiment.
1 represents very positive sentiment.
Descriptive Statistics Breakdown
count: 1.407328e+06

This indicates that there are 1,407,328 sentiment scores in the dataset. In other words, sentiment analysis was performed on 1,407,328 headlines.
mean: 4.905657e-02

The mean sentiment score is approximately 0.049, which is slightly positive. This suggests that, on average, the headlines have a mildly positive sentiment.
std: 1.830652e-01

The standard deviation is approximately 0.183. This indicates that there is some variability in the sentiment scores, but most scores are relatively close to the mean.
min: -1.000000e+00

The minimum sentiment score is -1.0, which indicates that there are headlines with very negative sentiment in your dataset.
25% (1st quartile): 0.000000e+00

The 25th percentile is 0.0, meaning that 25% of the headlines have a sentiment score of 0 or lower. This suggests that at least a quarter of the headlines are neutral or have negative sentiment.
50% (median): 0.000000e+00

The median sentiment score is 0.0. This indicates that half of the headlines have a sentiment score of 0 or less, suggesting a significant portion of neutral or negative sentiment.
75% (3rd quartile): 0.000000e+00

The 75th percentile is also 0.0, meaning that 75% of the headlines have a sentiment score of 0 or lower. This further emphasizes the prevalence of neutral sentiment in your dataset.
max: 1.000000e+00

The maximum sentiment score is 1.0, indicating that there are headlines with very positive sentiment in your dataset.
Interpretation
Skewed Distribution: The fact that the mean is positive, but both the median and 75th percentile are 0.0, suggests that the distribution of sentiment scores is skewed. A small proportion of the headlines likely have a positive sentiment, which raises the mean, while a large proportion are neutral.
Dominance of Neutral Sentiment: The 25th, 50th, and 75th percentiles being 0.0 indicates that neutral sentiment is very common in your dataset.
Presence of Extremes: The minimum and maximum values of -1.0 and 1.0 show that there are headlines with extreme sentiments, both very negative and very positive.
This analysis suggests that while most headlines in the dataset are neutral, there are still a range of sentiments present, with a small number of headlines having strong positive or negative sentiments.

