# Makefile for usehello service container

VER = 1.0
BASE = BMBedge

default: set

set:
	export HZN_ORG_ID='local-cluster'
	export HZN_EXCHANGE_USER_AUTH='iamapikey:p4J5UA_LxQ0dCEqaRyIgfgePyEDir3O5m3tLauW8A-LD'
	export HZN_NODE_AUTH='BMBedge-000001:myedgeforever'

unregister-node:
	hzn unregister -fr
	hzn node list

register-node:
	hzn register --policy=BMBedge-node.policy.json
	hzn node list

display-agreement:
  hzn agreement list
