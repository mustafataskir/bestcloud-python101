import boto3

class EC2:
    def __init__(self, region, access_key_id, secret_access_key):
        self.service = "ec2"
        self.region = region
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key
        
    def connect(self):
        self.resource = boto3.resource(service_name = self.service, region_name = self.region, aws_access_key_id = self.access_key_id, aws_secret_access_key = self.secret_access_key)
        self.client = boto3.client(service_name = self.service, region_name = self.region, aws_access_key_id = self.access_key_id, aws_secret_access_key = self.secret_access_key)

    def list_all_instances(self):
        item_list = []
        for item in self.resource.instances.all():
            item_list.append(item.id)
        return item_list
        
    
    def run(self, InstanceIds): 
        response = self.client.start_instances(InstanceIds=InstanceIds)
        return response
    
    def stop(self, InstanceIds):
        response = self.client.stop_instances(InstanceIds=InstanceIds)
        return response
    
