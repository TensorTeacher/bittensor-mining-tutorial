Recently, there have been ddos attacks on the bittensor network, and to protect your miners, you can modify the server running your miners to only accept requests from validator IP address ranges.

This code was provided by carro for blocking all non-validator IP addresses, you should run it using pm2 since you want it to be permanent:

```python3
import copy
import time
import torch
import argparse
import bittensor as bt
import subprocess

def resync_metagraph():
    bt.logging.info("resync_metagraph()")

    previous_metagraph = copy.deepcopy(metagraph)
    
    # sync metagraph
    metagraph.sync(subtensor=subtensor)

    # Check if the metagraph axon info has changed.
    metagraph_axon_info_updated = previous_metagraph.axons != metagraph.axons

    if metagraph_axon_info_updated:
        bt.logging.info("Metagraph updated, re-syncing hotkeys")

    bt.logging.info("Metagraph synced!")

def check_metagraph():
    bt.logging.info("check_metagraph()")
    indices = torch.topk(metagraph.stake, 60).indices

    uids_with_highest_stake = metagraph.uids[indices].tolist()

    axons = [metagraph.axons[uid] for uid in uids_with_highest_stake]

    ips = [axon.ip for axon in axons]

    uids_with_highest_stake, ips = zip(*[(uid, ip) for uid, ip in zip(uids_with_highest_stake, ips)])

    unique_ip_to_uid = {ip: uid for ip, uid in zip(ips, uids_with_highest_stake)}
    ips = list(unique_ip_to_uid.keys())

    bt.logging.info(f"Top 50 uids: {uids_with_highest_stake}")

    return ips

def whitelist_ips_in_ufw(ips):

    stop_cmd = "sudo ufw disable"
    reset_cmd = "echo y | sudo ufw reset"

    subprocess.run(stop_cmd, shell=True)
    subprocess.run(reset_cmd, shell=True)

    ssh_cmd = "sudo ufw allow ssh"
    subprocess.run(ssh_cmd, shell=True)
    for ip in ips:
        cmd = f"sudo ufw allow proto tcp from {ip}/16"
        subprocess.run(cmd, shell=True)
        bt.logging.info(f"Whitelisted IP {ip} for bittensor")


    start_cmd = "echo y | sudo ufw enable"
    subprocess.run(start_cmd, shell=True)


def parse_arguments():
    parser = argparse.ArgumentParser(description="Run firewall")
    parser.add_argument('--netuid', help='Machine to connect to', choices=[1, 11, 21], default=1)
    
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_arguments()
    subtensor = bt.subtensor(network="finney")
    metagraph = subtensor.metagraph(netuid=args.netuid)

    # ips = check_metagraph()

    # # take the first two places from ip e.g.  131.186.1.1 ->  131.186.0.0
    # ips = [ip.split(".")[0] + "." + ip.split(".")[1] + ".0.0" for ip in ips]
    
    while True:
        # Resync the metagraph
        resync_metagraph()
        
        # get the ips of the top 60 validator
        ips = check_metagraph()

        # take the first two places from ip e.g.  131.186.1.1 ->  131.186.0.0
        ips = [ip.split(".")[0] + "." + ip.split(".")[1] + ".0.0" for ip in ips]
        
        # Whitelist the IPs in UFW
        whitelist_ips_in_ufw(ips)
        

        # Wait for 100 blocks (1200 seconds or 20 minutes)
        bt.logging.info("Waiting for 100 blocks, sleeping")
        time.sleep(1200)

```

To use it, create a file called ufw.py by running this command:
```
cat > ufw.py
```
And then copy paste the code above into the file.

Then start the process by running:
```
pm2 start ufw.py --name ufw
```
