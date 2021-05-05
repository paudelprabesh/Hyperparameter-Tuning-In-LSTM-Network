## Dataset
The dataset consists of 50,000 user reviews from IMDB with no more than 30 reviews per movie and
has approximately equal number of positive and negative reviews.
The dataset is readily available with tenserflow.keras.dataset.
The mean length a review in the dataset is 234.75 words and the standard deviation is 172.91.
A review belongs to either a positive or negative class. Only the top 5000 frequently used words are retained
and the remaining words are labeled as <UNK> and do not contribute to the model.
