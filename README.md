
## Hyperparameter tuning in LSTM Network

In this study, we choose four different search strategies to tune hyperparameters in an LSTM network.
The dataset that we used in this experiment is the IMDB movie review dataset which contains 50,000 reviews and is listed on the official tf.keras website.
Our methods are Random Search(RS), Bayesian Optimization(BO), Genetic Algorithm(GA) and Grid Search(GS). With these methods, we tune the following hyperparameters:
learning rate, number of hidden units, input length and number of epochs.

We attempt to answer the following research questions:

     RQ1: How do the hyperparameter tuning techniques compare with each other?
     RQ2: Which set of above-mentioned hyperparameters yields the best results for LSTM?

We obtain three best models from GA and one each from RS and BO. Using these five models, we apply GS to get the final best set of hyperparameters.
Our study shows that GA gives the best result in finding the best model with AUC of 0.946.
Our comparative study between RS, BO, and GA (with Grid Search) shows that GA gives the optimal hyperparameters with high validation accuracy on the test dataset.
However, Random Search and Bayesian Optimization give sub-optimal results with faster training time.

