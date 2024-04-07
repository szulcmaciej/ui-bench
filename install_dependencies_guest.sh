# as this needs to be run with root privileges, it should be already included in the VM image
apt-get update && apt-get install -y git curl python3-pip python3-tk python3-dev
#curl -LsSf https://astral.sh/uv/install.sh | sh
sed -i 's/#WaylandEnable=false/WaylandEnable=false/' /etc/gdm3/custom.conf
# in virt-manager VM options, set video to Bochs or VGA for guest mouse to stay on the screen