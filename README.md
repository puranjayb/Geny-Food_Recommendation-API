
## API for Food Recommendation System

The food recommendation system API is a service that provides personalized food recommendations based on your preferences and dietary requirements. 


By inputting specific details such as your food preferences and restrictions, the API analyzes this information using advanced machine learning algorithms to generate customized food suggestions. It considers factors like popular food choices and relevant data to offer accurate recommendations. 

The API is efficient, continuously updated, and offers a user-friendly interface to explore and select from the suggested food items, allowing you to enhance your culinary experience and discover new dishes that align with your tastes.


## Installation

This API was developed on
```bash
Python 3.9.7
pip 23.1.2
```

To setup the api follow these steps for windows
```bash
  git clone https://github.com/puranjayb/Geny-Food_Recommendation-API.git
  cd Geny-Food_Recommendation-API
  pip install -r requirements.txt
```
    
## Deployment

To deploy this project run

```bash
  uvicorn food_recommendation_api:app --reload
```

