# Porto Alegre Traffic Accidents

[Porto Alegre](https://en.wikipedia.org/wiki/Porto_Alegre) is the capital and largest city of the Brazilian state of Rio Grande do Sul. Its population of 1,488,252 inhabitants (2020) makes it the twelfth most populous city in the country and the center of Brazil's fifth largest metropolitan area, with 4,405,760 inhabitants (2010). The city is the southernmost capital city of a Brazilian state.

The city hall hosts [Dados Abertos POA](http://datapoa.com.br/) a [CKAN](https://ckan.org/) repository with many information about the city. I used [Traffic Accidents Dataset](http://datapoa.com.br/dataset/acidentes-de-transito-acidentes) in this project to create a model to predict the probability of injured people given some information:

- latitude;
- longitude;
- involved trucks;
- involved motorcycle;
- involved cars,
- involved bus;
- involve other vehicle types;
- is a holiday;
- weekday;
- hour day; and
- accident type.

The final model was deployed in [HuggingFaces](https://huggingface.co/spaces/GregOliveira/poa_traffic_accidents) and it is available to use.

Our purpose with this project was strict to develop my machine learning and coding skills. If you want to use it with commercial goals, please contact me first at gregoryomelo@gmail.com.

---

## Methodology

First data loading was loaded by the repository and we applied some cleaning, processing, and transforming tasks. These steps can be seen in the notebook inside the `data folder`.

Initially, I planned to create three models:

1. Predict the probability of injured people.
2. Predict the probability of seriously injured people.
3. Predict the probability of dead people in the event or after it.

However, only the first model is ready to use now. The steps to train and evaluate this model can be seen in the notebook `model_feridos` inside the `model` folder.

The following methods were used:

- Logistic Regression;
- Gaussian Naive Bayes;
- K Neighbors;
- Random Forest;
- Gradient Boosting; and,
- XGBoost.

I used two scores to select and evaluate our models:

- F1 score: composition between the precision (how much our model correct classify every true label) and recall (how much our model correct indicates true labels); and,
- Brier score: average between the correct and the predicted probability.

However, we also analyzed other metrics to support my decision:

- Accuracy;
- ROC_AOC; and,
- Log loss (another way to quantify the quality of probability predictions).

I did not apply any tunning technique at this point.

---

## Results

The model trained showed a ROC AUC of 91.1% and an F1 score of 81.7%. The average probability error (Brier score) was 0.106. As said before, the final model was deployed in [HuggingFaces](https://huggingface.co/spaces/GregOliveira/poa_traffic_accidents) and it is available to use.

---

## Potential applications

There are some potential applications for this product, from my perspective I can highlight two of them:

- Model could help the emergency line decide where/when to send an ambulance. A great improvement here could be to apply speech recognition to fill data automatically or even analyze the voice to see how serious is the event;

- Model could indicate areas/periods where accidents with victims could happen and the city hall can take action to alert drivers and pedestrians

---
## Future works and improvements

There are some topics that we can explore in the future based on the results

- Tuning hyperparameters to improve evaluation scores;

- Apply other techniques to predict seriously injured people and casualties;

- Improvements on filling latitude and longitude features based on the address and web services such as GoogleMaps and OpenStreetMap; and,

- Create a data visualization using model results. This one is on my list and will be the next task.
---
## Acknowledgment

I would like to thank [Mario Filho](https://github.com/ledmaster). I discover how to create an app using HuggingFaces on his [youtube channel](https://www.youtube.com/watch?v=3y3l_rsbbB8&t=443s). After I saw it, I found a good thing to apply my knowledge.