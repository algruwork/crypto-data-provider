Create 

`sudo docker build . --tag okx`

Run with docker

`sudo docker run -p 8000:8000 --env MAIN_URL=/ okx`

Run localy with poetry 

`poetry run uvicorn crypto_data_provider.main:app --reload`