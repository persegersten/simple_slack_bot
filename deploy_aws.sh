#!/bin/bash

docker build -t 715953572522.dkr.ecr.eu-north-1.amazonaws.com/simple_slack_bot:latest .

aws ecr get-login-password --region eu-north-1 | docker login --username AWS --password-stdin 715953572522.dkr.ecr.eu-north-1.amazonaws.com/hello-flask

docker push 715953572522.dkr.ecr.eu-north-1.amazonaws.com/simple_slack_bot:latest

# TODO OBS EJ UPPDATERAT
# För att uppdatera till den nya servicen
# 1. Välj ECS -> Clusters -> Hello-World-Cluster -> Services -> hello-world-service
# 2. Klicka på Update Service
# 3. Välj den önskade revisionen
# 4. Klicka på Update 
# 
# För att ta reda på det nya IP-numret
# 1. Välj ECS -> Clusters -> Hello-World-Cluster -> Services -> hello-world-service
# 2. Välj fliken Tasks
# 3. Klicka på den nya tasken som skapats, där finns ett Private IP. Kopiera det
#
# För att uppdatera ALB att gå till den nya IPn
# 1. Välj EC2 -> Target groups -> hello-world-ecs-target-group
# 2. Klicka på Register targets och lägg till den nya IP-adressenb (välj Include as pending below) 
# 3. Klicke på Deregister för att ta bort den gamls
#
# Konrollea att det fungerar
# 1. Öppna i en browser: http://hello-world-load-balancer-1683764243.eu-north-1.elb.amazonaws.com/


