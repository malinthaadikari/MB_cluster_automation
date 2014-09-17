import boto.ec2
import time
import libxml2

region = boto.ec2.regioninfo.RegionInfo(name="nova" , endpoint="192.168.4.24")
conn = boto.connect_ec2(aws_access_key_id="694801110ef64468ba80074147fa3e89",
                                aws_secret_access_key="a5e9756a6f4242069787605156695315",
                                is_secure=False,
                                region=region,
                                port=8773,
                                path="/services/Cloud")
i=0
instanceList=[]

#this dictionary contains the IP addresses of the populated instances
ipmap = {}

#get the configurations details of the deployment
doc = libxml2.parseFile('configuration.xml')

# nova.servers.create(name ="malintha",password="malintha",image="b754996c-45dc-43d4-b2cb-47b6c10beca3",flavor=fl.id ,key_name = "adikarikey",nics = [{'net-id': '34c6cbf5-5647-4210-8979-67e0b3b1f88a','v4-fixed-ip': ''}])

#creating instaces one by one
for node in doc.xpathEval("//node"):
        myInstance=conn.run_instances('ami-00000013',min_count=1,max_count=1, instance_type = 'm1.small',key_name='adikarikey', network_interfaces = [{'net-id': '34c6cbf5-5647-4210-8979-67e0b3b1f88a','v4-fixed-ip': ''}])
        instanceList.append(myInstance)
        while (instanceList[i].instances[0]).update() != "running":
              print (instanceList[i].instances[0]).update()
              time.sleep(2)
        print (instanceList[i].instances[0]).ip_address

        #we shutdown the instance just after create it to avoid running the puppet deamon
        ipmap[node.prop('id')] =  (instanceList[i].instances[0]).ip_address
        instanceID=(instanceList[i].instances[0]).id
        conn.stop_instances(instance_ids=[instanceID])
        i=i+1

#we turn on all the machines after creating all instances
time.sleep(5)
j=0;
print "came"

while(j<len(doc.xpathEval("//node"))):
        currentNode= doc.xpathEval("//node")[j]
        configFilepath = '/tmp/'+currentNode.prop('id')
        xmlstring = currentNode.serialize('UTF-8', 1).replace('\n', '')
        t = xmlstring.format(**ipmap)
        print t
        f = open(configFilepath,'w+')
        f.write('configurations,'+xmlstring)
        f.close()
        instance = conn.get_all_instances(instance_ids=[(instanceList[j].instances[0]).id])
        instance[0].instances[0].start()
        j=j+1
                         

