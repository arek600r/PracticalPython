#!/bin/bash
if [[ $EUID -ne 0 || -z "$SUDO_USER" ]]; then
  echo "This script must be run with sudo. Please try again using 'sudo'." >&2
  exit 1
fi

NS=test

ip netns exec $NS sudo -u "$SUDO_USER" bash -c "echo Inside network namespace; ip addr; exec bash"
