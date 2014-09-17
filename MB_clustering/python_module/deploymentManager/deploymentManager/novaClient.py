from novaclient.client import Client
nova = Client(2, "malintha", "malintha", "automation", "http://192.168.4.24:5000/v2.0",service_type="compute")
print nova.servers.list()
floating_ip = nova.floating_ips.create(nova.floating_ip_pools.list()[0].name)
image = nova.images.find(name="DeploymentAutomationImageV2")
flavor = nova.flavors.find(name="m1.medium")
#print nova.networks.list()
server = nova.servers.create(name = "malintha",image = image.id,flavor = flavor.id,key_name = "adikarikey", network = "34c6cbf5-5647-4210-8979-67e0b3b1f88a")
