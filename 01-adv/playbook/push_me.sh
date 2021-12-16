#!/bin/bash
#
# == Variables =================
docker_servers=( centos7=pycontribs/centos:7 ubuntu=pycontribs/ubuntu:latest fedora=pycontribs/fedora:latest )
#
#
# Prepairing containers...
#
for srv in ${docker_servers[@]}; do
    img=$(echo ${srv} | sed 's/^.*=//')
    name=$(echo ${srv} | sed 's/=.*$//')
    docker run --rm --name ${name} -d ${img} sleep 60000000
done

#docker run --rm --name centos7 -d pycontribs/centos:7 sleep 60000000
#docker run --rm --name ubuntu -d pycontribs/ubuntu:latest sleep 60000000
#docker run --rm --name fedora -d pycontribs/fedora:latest sleep 60000000

# Ansible routine
#
ansible-playbook ./site.yml -i ./inventory/prod.yml --vault-password-file ./key.txt

# Stopping containers..
#
for srv in ${docker_servers[@]}; do
    name=$(echo ${srv} | sed 's/=.*$//')
    docker stop ${name}
done
# That's all, exiting.