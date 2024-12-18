# Tool Usage - Step-by-Step Instructions

## 1. Environment Setup

### Create Virtual Environment:

python3 -m venv takeda
source takeda/bin/activate

### Install Dependencies:

pip install -r requirements.txt

** File Link** 
   - [requirements.txt](requirements.txt)

###  IF THE FIRST TIME build database 
build the manufacturing database
python build_manufac_db.py

** File Link** 
   - [build_manufac_db.py](build_manufac_db.py)

Build a mock csv file manufacturing
python mock_manufacturing.py

** File Link** 
   - [mock_manufacturing.py](mock_manufacturing.py)

###  Clean, Analyze and Visualize the data
Using requirements that you can choose about defect and yeld, this also will store in a database 
python data_pipeline.py

** File Link** 
   - [data_pipeline.py](data_pipeline.py)

###  Make some queries to vizualize the table 



** File Link** 
   - [query_mdb.py](query_mdb.py)

### Run the data API
Generate Mock IoT Data
python api.py


** File Link** 
   - [api.py](api.py)

## Run the html to plot the data into a local host
python -m http.server

** File Link** 
   - [index.html](index.html)

## Add to azure blob (optional)
python to_azure.py

** File Link** 
   - [to_azure.py](to_azure.py)


