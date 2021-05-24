# rgate-assignment
K8's cluster to implement RGate Functionality

## PreRequisites

Download one of the tools from the below

https://kubernetes.io/docs/tasks/tools/


## Creating aliases for running the code

Create the aliases for deployment,running and stopping rgate. RGate has a bug with aboslute paths. so please run them by changing the directory to the src folder of the cloned repo.

- ``` alias rgate-deploy="python3 deployer.py" ```
- ``` alias rgate-run="python3 executor.py" ```
- ``` alias rgate-run="python3 destroy.py" ```



## Bugs/To-do's

- Change the working directory of rgate from src. Use absolute path instead of relative paths
- Expose the default port to be configurable from port 80 to a command line argument
- Implment match-label to be templatized for a list instead of just the app-name
- Implement the Stats Endpoint and Integarte with the metrics API.
- Use Subcharts instead of using command line arguments


