from aws import EC2
from flask import Flask, request, jsonify
import configparser
import os
import logging

app = Flask(__name__)
basedir = os.path.dirname(os.path.abspath(__file__))
configpath = os.path.join(basedir, "config.cfg")
config = configparser.ConfigParser()
config.read(configpath)
logging.basicConfig(filename=config['LOGGING']['log_path'], level=config['LOGGING']['log_level'], encoding=config['LOGGING']['encoding'])

@app.route("/ec2/list", methods = ["GET"])
def list_instances():
    try:
        args = request.args
        access_key_id = args["aws_access_key_id"]
        secret_access_key = args["aws_secret_access_key"]
        region = args["region_name"]
        ec2 = EC2(region, access_key_id, secret_access_key)
        ec2.connect()
        instances = ec2.list_all_instances()
        return jsonify(data = instances,status_code=200)
    except Exception as err:
        logging.error(err)
        return jsonify(Response = "Bir hata oldu", Error=str(err))

@app.route("/ec2/start", methods = ["GET"])
def start():
    try:
        args = request.args
        access_key_id = args["aws_access_key_id"]
        secret_access_key = args["aws_secret_access_key"]
        region = args["region_name"]
        instanceid = args["InstanceId"] 
        ec2 = EC2(region, access_key_id, secret_access_key)
        ec2.connect()
        response = ec2.run([instanceid])
        return jsonify(data = response, status_code=200)
    except Exception as err:
        logging.error(err)
        return jsonify(Response = "Bir hata oldu", Error=str(err))

@app.route("/ec2/stop", methods = ["GET"])
def stop():
    try:
        args = request.args
        access_key_id = args["aws_access_key_id"]
        secret_access_key = args["aws_secret_access_key"]
        region = args["region_name"]
        instanceid = args["InstanceId"] 
        ec2 = EC2(region, access_key_id, secret_access_key)
        ec2.connect()
        response = ec2.stop([instanceid])
        return jsonify(data = response, status_code=200)
    except Exception as err:
        logging.error(err)
        return jsonify(Response = "Bir hata oldu", Error=str(err))

if __name__ == "__main__":
    
    host = config['APISETTINGS']['host']
    port = config['APISETTINGS']['port']
    app.run(host=host, port=int(port), debug=False)
     
#List bağlantısı    
#http://<ip>:<port>/ec2/list?region_name=<***>&aws_access_key_id=<***>&aws_secret_access_key=<***>

#Start bağlantısı
#http://<ip>:<port>/ec2/start?region_name=<***>&aws_access_key_id=<***>&aws_secret_access_key=<***>&InstanceId=<***>

#Stop bağlantısı
#http://<ip>:<port>/ec2/stop?region_name=<***>&aws_access_key_id=<***>&aws_secret_access_key=<***>&InstanceId=<***>