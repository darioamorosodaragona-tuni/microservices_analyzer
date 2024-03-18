# microservices-analysis

### Setup
- Requirements:
	- Ruby
	- github-linguist: ```gem install github-linguist```
    - all packages in the requirements.txt file: ```pip install -r requirements.txt```

### Execution
put in the  ```repos``` folder the .csv file containing one git repo per link, be sure that the link are in https format, then run:
- ```python analyze_repo_multi_thread.py```
- the possible options are ```-d -w 10```
	- ```-w``` the number of threads to use, if not specified the number of threads will follow the threadpoolexecutor default value
    - ```-d``` debug mode: in this mode the number of threads is set to 1 and the output is printed to the console
