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
#for image in conn.get_all_network_interfaces(network_interface_ids='34c6cbf5-5647-4210-8979-67e0b3b1f88a'):
 #       print image

#for interface1 in conn.get_all_network_interfaces():
#	print interface
#	print "malintha"
conn.run_instances('ami-00000015',min_count=1,max_count=1, instance_type = 'm1.medium',key_name='adikarikey',subnet_id='34c6cbf5-5647-4210-8979-67e0b3b1f88a')

