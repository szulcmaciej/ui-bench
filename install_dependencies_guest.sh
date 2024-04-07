# as this needs to be run with root privileges, it should be already included in the VM image
apt-get update && apt-get install -y git curl
curl -LsSf https://astral.sh/uv/install.sh | sh