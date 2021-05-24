import os

class Destructor:
    def __init__(self):
        self.helm_path="../resources/helm/charts/"

    def stop_rgate(self):
        charts=os.popen("ls "+self.helm_path).read()
        charts=charts.split()
        for chart in charts:
            os.system("helm uninstall "+chart)

De1=Destructor()
De1.stop_rgate()
