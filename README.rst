docker build -t demo-app .

docker run --env PORT=8080 demo-app 




uvicorn main:app  --port 8080 --workers 1 --timeout-keep-alive 0 --reload