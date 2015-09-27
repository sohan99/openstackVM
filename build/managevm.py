import os
import sys
import time
from novaclient import client
import novaclient.exceptions

Keystone_AuthUrl="http://controller:35357/v2.0"
Keystone_VersionNumber=2
Keystone_UserName="admin"
Keystone_Password="ADMIN_PASS"
Keystone_TennantName="admin"
ImageName="cirros-0.3.3-x86_64"
vm_id=["vm1","vm2"]

def create_vm(i):
	#global vm_id
	image=nova.images.find(name=ImageName)
	flavor=nova.flavors.find(name="m1.tiny")
	name = vm_id[i]
	print name
	vm=nova.servers.create(name=name,image=image,flavor=flavor)
	print "creating " + vm_id[i] ;
	print "waiting for status ..." 
	if vm.status == "BUILD" :
		time.sleep(20)
		print "ID : "+ vm.id
		print "Build Success !!"
	else:
		print name + " : Buid Failed .. "
	return;

def delete_vm():
	#global vm_id
	i=len(vm_id)-1
	name=vm_id[i]
	dvm = nova.servers.find(name=name)
	dvm.delete()
	del vm_id[i]
	return;



nova=client.Client(Keystone_VersionNumber,Keystone_UserName,Keystone_Password,Keystone_TennantName,Keystone_AuthUrl)
nova.servers.list()


