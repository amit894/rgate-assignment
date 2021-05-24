import os

class Executor:
    def __init__(self):
        self.helm_path="../resources/helm/charts/"

    def run_rgate(self):
        charts=os.popen("ls "+self.helm_path).read()
        charts=charts.split()
        for chart in charts:
            os.system("helm install --set name="+chart+" "+chart+" "+self.helm_path+chart)

    def stop_rgate(self):
        charts=os.popen("ls "+self.helm_path).read()
        charts=charts.split()
        for chart in charts:
            os.system("helm uninstall "+chart)

E1=Executor()
E1.run_rgate()
