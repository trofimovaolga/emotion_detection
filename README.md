# emotion_detection

Emotion detection web-service: multilabel text classification based on BERT model using FastAPI. The Uvicorn is used for implementing the server.

Used roberta-base-emotion model from https://huggingface.co/bhadresh-savani/roberta-base-emotion to classify texts into one of the six emotions: **anger, sadness, fear, surprise, joy, love**.

RoBERTa is robustly optimized BERT model.

roberta-base-emotion is finetuned on the emotion dataset using HuggingFace Trainer.

After running the code go to http://127.0.0.1:8000/docs - you’ll see interactive API docs.

<img src="https://user-images.githubusercontent.com/11677412/145719663-55b7bbff-56a0-4ffb-9d29-4c2cec02efa4.png" alt="alt text" width="512">


POST/emotion-detection endpoint predicts the emotion class and returns it as a response.

<img src="https://user-images.githubusercontent.com/11677412/145719673-2c94624a-abee-4558-a83a-ebc4ab550c9b.png" alt="alt text" width="512">

Click on the **Try it Out** button and enter the text you want the prediction for, click on **Execute** to see the result.

<img src="https://user-images.githubusercontent.com/11677412/145719689-eac5179e-29da-4853-a360-ceb92ba7ed62.png" alt="alt text" width="512">
