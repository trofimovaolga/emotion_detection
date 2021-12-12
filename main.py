import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

classification_model = pipeline('text-classification',
								model='bhadresh-savani/roberta-base-emotion',
                				return_all_scores=True)

# Creating FastAPI instance
app = FastAPI(title='emotion-detection')

# Define the object for classification
class request_body(BaseModel):
	text: str

# Server definition
@app.get('/')
def get_root():
	return {'GoTo': '/docs'}

# Creating an Endpoint to receive the data to make prediction on
@app.post('/emotion-detection')
def predict(data: request_body):
	test_data = data.text
	result = classification_model(test_data)

	return {'emotions_probabilities': result[0]}

if __name__ == '__main__':
	uvicorn.run(app, host='127.0.0.1', port=8000)