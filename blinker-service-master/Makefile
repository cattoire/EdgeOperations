DOCKER_NAME = arm_cpu
DOCKER_TAG = 1.0
DOCKER_HUB_ID = openhorizon

publish-service:
	hzn exchange service publish -P -f ./horizon/service.definition.json -v

publish-bpol:
	hzn exchange business addpolicy --json-file=./horizon/business.policy.json dla.light.policy -v
	hzn exchange business listpolicy dla.light.policy -v

republish-bpol:
		hzn exchange business removepolicy dla.light.policy -vf
		hzn exchange business addpolicy --json-file=./horizon/business.policy.json dla.light.policy -v

remove-bpol:
	  hzn exchange business removepolicy dla.light.policy -v

publish-spol:
	hzn exchange service addpolicy -f ./horizon/service.policy.json light-service_0.1_arm -v
	hzn exchange service listpolicy light.service_0.1_arm -v

remove-spol:
	hzn exchange service removepolicy light-service_0.1_arm -v
