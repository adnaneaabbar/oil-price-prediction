# Data Engineering Project using Git and Docker
What we are planning to work on is a project around time series prediction, mainly the prediction of oil prices.

## Git usage
We will be using Git and Github for version control, and collaborating with each other inside this repo

## Docker usage
We will have many containers responsible for different tasks and pipelines:
1. Data Preparation for Machine Learning task
2. Model Training (Different time steps for each training)
3. Inference to test the models on new data points

## Data Source
[Data](https://fred.stlouisfed.org/series/DCOILBRENTEU#0)

### Part 1 : Fetching data dynamically
Open a first terminal and run the following commands

```console
foo@bar:~$ cd data_fetching
foo@bar:~$ docker build -t data-fetch .
foo@bar:~$ docker run -it --name data-fetch data-fetch
# once inside the docker container
root@id:~$ URL="shorturl.at/arJNS"
root@id:~$ python data_fetching.py --url=${URL}
```

Open a second terminal and run the following command

```console
foo@bar:~$ docker cp data-fetch:/app/raw_data.csv ../data/raw_data.csv
```

Now we have fetched our CSV file and it's stored in the directory data at the root of our repo

```console
root@id:~$ exit
```