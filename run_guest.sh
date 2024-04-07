# TODO (run this automatically after the VM is up)

# clone the repo
git clone https://github.com/szulcmaciej/ui-bench.git # if there is no repo yet
cd ui-bench
git pull # if there is a repo, pull the latest changes

# install python dependencies
uv venv venv
source venv/bin/activate
uv pip install -r requirements.txt

# get API keys (how?)
# TODO

# run the program
python3 main.py