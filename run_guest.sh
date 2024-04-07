# TODO (run this automatically after the VM is up)
# clone the repo
git clone https://github.com/szulcmaciej/ui-bench.git
cd ui-bench
# install dependencies
uv venv venv
source venv/bin/activate
uv pip install -r requirements.txt
# get API keys (how?)
# run the program
python3 test_move_mouse.py