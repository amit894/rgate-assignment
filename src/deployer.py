import os
import yaml
import json
import jinja2
from jinja2 import Template

ingress_master_dict="{'apiVersion': 'networking.k8s.io/v1', 'kind': 'Ingress', 'metadata': {'name': 'rgate', 'annotations': {'nginx.ingress.kubernetes.io/rewrite-target': '/$3'}}, 'spec': {'rules': [{'host': 'rgate', 'http': {'paths': 'None'}}]}}"
ingress_master_dict = ingress_master_dict.replace("'", "\"")
ingress_master_dict= json.loads(ingress_master_dict)

class Deployer:
    def __init__(self,config):
        self.config_file_path=config
        self.template_path="../resources/templates-jinja/"
        self.helm_path="../resources/helm/charts/"

    def deploy_rgate(self):
        file = open(self.config_file_path)
        input_list = yaml.load(file, Loader=yaml.FullLoader)
        routes=input_list["routes"]
        backend=input_list["backends"]
        file.close()

        self.create_ingress(routes)
        self.create_service(backend)

    def create_ingress(self,routes):
        temp_list=[]
        ingress_file = open(self.template_path+"ingress/ingress.yaml","r+")
        route_list=[]
        for route in routes:
            temp_dict={}
            temp_port={}
            temp_service={}
            temp_backend={}
            temp_dict["path"]=route["path_prefix"]
            temp_dict["pathType"]="Prefix"
            temp_port["number"]=8080
            temp_service["name"]=route["backend"]
            temp_service["port"]=temp_port
            temp_backend["service"]=temp_service
            temp_dict["backend"]=temp_backend
            route_list.append(temp_dict)
        ingress_master_dict["spec"]["rules"][0]["http"]["paths"]=route_list
        yaml.dump(ingress_master_dict,ingress_file)
        ingress_file.close()
        os.system("cp -f "+ self.template_path+"ingress/ingress.yaml " + self.helm_path+ "rgate/templates")


    def create_service(self,backends):
        for backend in backends:
            os.system("cd "+ self.helm_path+" && helm create "+backend["name"]+"-service")
            os.system("cp -f "+ self.template_path+"/service/deployment.yaml " +self.helm_path+backend["name"]+"-service/templates")
            os.system("cp -f " + self.template_path+"service/service.yaml " +self.helm_path+backend["name"]+"-service/templates")
            ingress_template=Template(open(self.template_path+"service/values.yaml").read())
            values_content=(ingress_template.render(serviceName=backend["name"]))
            f1=open(self.helm_path+backend["name"]+"-service/values.yaml","w")
            f1.write(values_content)
            f1.close()

D1=Deployer("../config.yaml")

D1.deploy_rgate()
