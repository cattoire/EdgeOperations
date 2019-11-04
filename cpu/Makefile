DOCKER_NAME = arm_cpu
DOCKER_TAG = 1.0
DOCKER_HUB_ID = openhorizon

publish-service:
	hzn exchange service publish -P -f ./horizon/service.definition.json -v

publish-bpol:
	hzn exchange business addpolicy --json-file=./horizon/business.policy.json dla.cpu.policy -v
	hzn exchange business listpolicy dla.cpu.policy -v

remove-bpol:
	  hzn exchange business removepolicy dla.cpu.policy -v

publish-spol:
	hzn exchange service addpolicy -f ./horizon/service.policy.json dla.cpu.service_1.5.1_arm -v
	hzn exchange service listpolicy dla.cpu.service_1.5.1_arm -v

remove-spol:
	hzn exchange service removepolicy dla.cpu.service_1.5.1_arm -v

publish-nodepol:
	hzn exchange node addpolicy -f ~/services/node.policy.json booz.policy.test.node.vm
	hzn exchange node listpolicy booz.policy.test.node.vm

list-all-policies:
	hzn exchange node listpolicy
	hzn exchange service listpolicy dla.cpu.service_1.5.0_arm -v
	hzn exchange business listpolicy dla.cpu.policy -v
