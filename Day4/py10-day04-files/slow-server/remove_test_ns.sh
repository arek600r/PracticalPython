#!/bin/bash
# Use -f to kill all the processes in the namespace.

if [[ $EUID -ne 0 || -z "$SUDO_USER" ]]; then
  echo "This script must be run with sudo. Please try again using 'sudo'." >&2
  exit 1
fi

NS="test"
FORCE=false

while getopts ":fn:" opt; do
  case ${opt} in
    f )
      FORCE=true
      ;;
    \? )
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  esac
done

if ! ip netns list | grep -qw "$NS"; then
  echo "Namespace '$NS' does not exist."
  exit 0
fi

pids=$(ip netns pids "$NS")

if [ -z "$pids" ]; then
  ip netns delete "$NS"
  echo "Namespace '$NS' deleted successfully."
else
  if [ "$FORCE" = true ]; then
    echo "Killing processes in namespace '$NS':"
    echo "$pids"
    for pid in $pids; do
      echo Killing "$pid"...
      kill -TERM "$pid" 2>/dev/null
      # Wait for the process to terminate
      while kill -0 "$pid" 2>/dev/null; do
        sleep 0.1
      done
    done
    ip netns delete "$NS"
    echo "Namespace '$NS' and its processes have been deleted successfully."
  else
    echo "Error: Namespace '$NS' has running processes:"
    echo "$pids"
    exit 1
  fi
fi
