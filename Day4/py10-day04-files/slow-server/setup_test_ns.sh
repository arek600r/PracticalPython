#!/bin/bash
if [[ $EUID -ne 0 || -z "$SUDO_USER" ]]; then
  echo "This script must be run with sudo. Please try again using 'sudo'." >&2
  exit 1
fi

NS=test

ip netns add $NS
ip netns exec $NS ip link set lo up

ip link add veth-host type veth peer name veth-ns
ip link set veth-ns netns $NS
ip addr add 192.168.33.1/24 dev veth-host
ip link set veth-host up

ip netns exec $NS ip addr add 192.168.33.2/24 dev veth-ns
ip netns exec $NS ip link set veth-ns up

ip netns exec $NS tc qdisc add dev veth-ns root tbf rate 256kbit burst 32kbit latency 100ms
tc qdisc add dev veth-host root tbf rate 256kbit burst 32kbit latency 100ms

echo "If this shows only loopback interface and it's up, everything worked:"
ip netns exec $NS ip addr

echo Network namespace name is: $NS
