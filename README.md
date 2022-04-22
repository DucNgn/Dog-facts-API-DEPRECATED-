This project is deprecated and has been migrated to a new repo: [Dog-Facts-API-v2](https://github.com/DukeNgn/Dog-Facts-API-v2) with support for CORS, built with Python and FastAPI. This repository will be archived soon. The heroku api service will be kept alive for a while before terminated.

# Dog Facts API (DEPRECATED)


An API that will return random facts about dog.

## Inspirations 
+ The project is a port of [kinduff/dog-api](https://github.com/kinduff/dog-api) using Python with Flask.
+ There is still no other dog facts api while there are many APIs supporting cat facts. It is unfair !!!
+ I'm a dog person. Cats are jerks.

## Usage:

+ `https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/all` to get all the facts at once.
+ Change `all` to parameter `?number=` to specify the number of facts you want to receive.
+ Change `all` to parameter `?index=` to specify the index of the fact you are targeting.

> Note: The project is being hosted by Heroku with free dyno; thus, there will be potential delay the first time you make a request (app went to sleep after dyno does not receive traffic in 1 hour). Please be patient, and the call will be faster next time.

## Rebuild the project:
+ Clone the repo.
+ Run `python3 -m venv .env` to create a virtual environment.
+ Run `source .env/bin/activate` to activate the virtual environment.
+ Run `pip install requirements.txt`.
+ Run `python3 app.py`.
+ App starts at port 5000 by default, but can be configured with a `.env` file. 

## Example:
+ `https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1` returns:
```JSON
[
    {
        "fact": "Many foot disorders in dogs are caused by long toenails."
    }
]
```

+ `https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=2` returns:
```JSON
[
    {
        "fact": "Endal was the first dog to ride on the London Eye (the characteristic ferris wheel in London, England), and was also the first known dog to successfully use a ATM machine."
    },
    {
        "fact": "At the age of 4 weeks, most dogs have developed the majority of their vocalizations."
    }
]
```
