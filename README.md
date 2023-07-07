# AlarmClock
##### "Будильник" который делает запросы на бэк и проигрывает mp3 файлы, если надо. Кроме этого, идёт проверка на список этих mp3 файлов
---
### Примеры запросов и ответов:

### GET /api/v1/alarm/status/:school_id
#### school_id и TOKEN берётся из .env
Headers:
  Authorizate: Bearer {TOKEN}

Ответ положительный:
```json
{"alarm":true,"mp3":"https://sampleurl.com/music.mp3", "hash":"570d78bd695e43034204b99d6a6817bf"}
```

Ответ отрицательный:
```json
{"alarm":false}
```

После того, как бэк ответил положительно, скрипт проверяет наличие предоставленного файла (по хэшу MD5 в ответе)
и проигрывает его

---
### GET /api/v1/alarm/list/:school_id
#### school_id и TOKEN берётся из .env
Headers:
  Authorizate: Bearer {TOKEN}

Ответ:
```json
[
  {
    "url":"https://sampleurl.com/music.mp3",
    "hash":"570d78bd695e43034204b99d6a6817bf"
  },
  {
    "url":"https://sampleurl.com/music2.mp3",
    "hash":"3ab8cc73337a9bdc54df40cb88cf1ce3"
  },
  {
    "url":"https://sampleurl.com/musi3c.mp3",
    "hash":"badc18fd92f383e04d67000b683c0bfb"
  },
]
```
После получения ответа скрипт сверяет список аудиофайлов, который у него сейчас скачан, и 
список аудиофайлов, который предоставил BackEnd. При расхождении он скачивает / удаляет файлы.

---



Если файл отсутствует - он его скачивает, после чего проигрывает. 

