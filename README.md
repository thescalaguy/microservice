# Setting up a Python microservice  

This is the companion repository for [the series of blog posts on setting up a Python microservice](https://fasihkhatib.com/2024/03/21/Setting-up-a-Python-microservice/).  

## Running the code  

Running the code requires installing [Poetry](https://python-poetry.org/) and the required packages. You can install Poetry using pip as follows.   

```
pip install poetry
```   

Once installed, proceed to installing the packages.  

```
poetry install
```  

Next, bring up the Docker containers.  

```
docker compose up -d
```  

You can now run individual services using their start scripts. In two separate terminals, execute the following commands.

```shell
# Start the "first" microservice
./first.sh
```   

```shell
# Start the "second" microservice
./second.sh
```