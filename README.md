# rgate-assignment
K8's cluster to implement RGate Functionality

## PreRequisites

* Download (kind/minikube) from the below to run kubernetes cluster on your local laptop : https://kubernetes.io/docs/tasks/tools/
   * Install the Nginx Controller for the Gateway Layer https://kubernetes.github.io/ingress-nginx/deploy/    
* Install python 3 on your machine : https://www.python.org/downloads/
* Install Helm on your machine : https://helm.sh/docs/intro/install/

 
## Creating aliases for running the code

Create the aliases for deployment,running and stopping rgate. RGate has a bug with aboslute paths. so please run them by changing the directory to the src folder of the cloned repo.

- ``` alias rgate-deploy="python3 deployer.py" ```
- ``` alias rgate-run="python3 executor.py" ```
- ``` alias rgate-delete="python3 destroy.py" ```


## Steps for running RGate

### Deploying RGate :

- `cd src`
-  `rgate-deploy`

### Running RGate :

- `cd src`
-  `rgate-deploy`

### Stopping RGate :

- `cd src`
-  `rgate-delete`


### Validating RGate :

Without making Changes to hosts file

- `curl -H “Host: rgate” http://192.168.64.2:80/api/payments/index.html` ( where 192.168.64.2 -> Minikube IP)


## Bugs/To-do's

- Change the working directory of rgate from src. Use absolute path instead of relative paths
- Expose the default port to be configurable from port 80 to a command line argument
- Implment match-label to be templatized for a list instead of just the app-name
- Implement the Stats Endpoint and Integarte with the metrics API.
- Use Subcharts instead of using command line arguments


