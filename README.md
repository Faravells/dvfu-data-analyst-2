# Задание 2 — API-пайплайн: данные → LLM → результат
Цель: написать рабочий скрипт, который автоматически отправляет данные в LLM через API и получает структурированный ответ.

### Что нужно сделать
Написать скрипт на любом языке (Python, PHP, JavaScript и др.), который выполняет пайплайн:
- Читает входные данные из CSV-файла или внешнего API.
- Формирует запрос и отправляет его в LLM через API (OpenAI, Anthropic, Qwen, Xiaomi MiMo и др.).
- Получает от LLM структурированный ответ в формате JSON.
- Сохраняет результат в файл (CSV, JSON или TXT).

### Задача
Классификация отзывов: скрипт читает отзывы → LLM определяет тональность (positive/negative/neutral) и тему → результат в CSV.
- входной файл сделан из датасета Massive Rotten Tomatoes Movies & Reviews (https://www.kaggle.com/datasets/andrezaza/clapper-massive-rotten-tomatoes-movies-and-reviews), убрав все колонки, кроме reviewText, удалив пустые строки и взяв первые 10 строк. 

### Инструкция запуска
- Открываем командную строку
- cd {папка, в которую поместим работу}
- git clone https://github.com/Faravells/dvfu-data-analyst-2
- cd dvfu-data-analyst-2
- pip install -r requirements.txt
- Заходим на https://openrouter.ai/settings/keys и получаем свой API ключ
- Создаем в папке файл .env и добавляем в него "OPENROUTER_API_KEY=ваш_API_ключ"
- python main.py
- После запуска и отработки скрипта, выходные данные будут в файле output.csv

### Пример входных данных (первые 5 строк input.csv)
reviewText  
"Timed to be just long enough for most youngsters' brief attention spans -- and it's packed with plenty of interesting activity, both on land and under the water."  
"It doesn't matter if a movie costs 300 million or only 300 dollars; good is good and bad is bad, and Bloodmask: The Possession of Nicole Lameroux is just plain bad."  
"The choreography is so precise and lifelike at points one might wonder whether the movie was rotoscoped, but no live-action reference footage was used. The quality is due to the skill of the animators and Kodama's love for professional wrestling."  
The film's out-of-touch attempts at humor may find them hunting for the reason the franchise was so popular in the first place.

### Пример выходных данных (первые 5 строк output.csv)
reviewText,sentiment,theme  
"Timed to be just long enough for most youngsters' brief attention spans -- and it's packed with plenty of interesting activity, both on land and under the water.",positive,entertainment  
"It doesn't matter if a movie costs 300 million or only 300 dollars; good is good and bad is bad, and Bloodmask: The Possession of Nicole Lameroux is just plain bad.",negative,Movie quality  
"The choreography is so precise and lifelike at points one might wonder whether the movie was rotoscoped, but no live-action reference footage was used. The quality is due to the skill of the animators and Kodama's love for professional wrestling.",positive,animation/choreography  
The film's out-of-touch attempts at humor may find them hunting for the reason the franchise was so popular in the first place.,negative,cinema/franchise
