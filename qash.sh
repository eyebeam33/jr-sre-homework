#!/bin/sh -ve
# requires 'jq' utility

image=$1

docker pull $image
docker run $image

mkdir -p $image 

docker save $image | tar xf - -C $image

config=$(jq -r '.[].Config' "${image}/manifest.json")

CMD=$(jq -r '.config.Cmd[]' ${image}/${config})

printf "A1:\tCMD=%s\n" $CMD > q1.txt

mkdir -p ${image}/sysimage
container=$(docker ps -lq)
docker export $container|tar xf - -C ${image}/sysimage etc/resolv.conf

( echo "A2: contents of /etc/resolv.conf"

cat ${image}/sysimage/etc/resolv.conf ) > q2.txt

# cleanup
rm -rf $image
docker rm $container
