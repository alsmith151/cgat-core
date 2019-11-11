'''
Cloud.py - This contains all of the functions for cloud based execution
'''

import uuid




def get_container_image():
    '''Function to get latest stable cgatcore image'''
    return "cgatcore/cgatcore:v%s"

def CloudExecutor:
    '''Base class for Cloud exection'''
    def __init__(self, args):

        self.args = args

    def get_default_remote_provider(self):
        if self.args.default_remote_provider:
            return("--default-remote-provider %s --default-remote-prefix" % 
                   (self.args.default_remote_provider.__module__.split(".")[-1],
                    self.args.default_remote_prefix))
        return ""

    def run(self, job):
        pass

    def cancel(self):
        pass

    def shutdown(self):
        pass

def KubernetesExecutor(CloudExecutor):
    '''will run kubernates'''
    def __init__(self, pipeline, dag, namespace, args, argv):
    
        super().__init__(args)

        # Need to specify path to workflows - maybe specifying the github repo or its location in bucket?

        try:
            from kubernetes import config
        except ImporError:
            raise WorkflowError('''python-kubernates must be installed to run
                                   kubernetes''')

        # set config using helper class
        config.load_kube_config()

        import kubernetes.client

        self.kubeapi = kubernetes.client.CoreV1Api()
        self.batchapi = kubernetes.client.CoreV1Api()
        self.namespace = namespace
        self.args = args
        self.run_namespace = str(uuid.uuid4())
        self.register_secret()
        self.container_img = container_img or get_container_img()

        def register_secret(self):
            pass
    
# need to handle pipeline actions
# use python-kubernates API 
