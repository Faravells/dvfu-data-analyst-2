import pandas as pd
import os
from openai import OpenAI
from dotenv import load_dotenv
import json
from time import sleep

load_dotenv()
df = pd.read_csv("input.csv")
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.environ.get('OPENROUTER_API_KEY'),
)

resDf = pd.DataFrame(columns=['reviewText', 'sentiment', 'theme'])
for i, reviewText in df.iterrows():
    reviewText = reviewText['reviewText']
    response = client.chat.completions.create(
        model="stepfun/step-3.5-flash:free",
        messages=[
            {
                "role": "user",
                "content": f"""
Проанализируй следующий отзыв и определи тональность (sentiment) - positive/negative/neutral и тему (theme):
Отзыв: "{reviewText}"
Верни только JSON объект без дополнительного текста в формате:
{{"sentiment": "значение", "theme": "значение"}}
"""
            }
        ]
    )
    response = json.loads(response.choices[0].message.content)
    resDf.loc[i] = reviewText, response['sentiment'], response['theme']
    sleep(5)

resDf.to_csv("output.csv", index=False)