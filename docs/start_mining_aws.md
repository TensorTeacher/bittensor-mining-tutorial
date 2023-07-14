# Bittensor Mining Tutorial

This tutorial will guide you through the process of setting up a miner on the Bittensor Network, a blockchain for decentralized AIs.
There might be slight differences depending on platform. This tutorial was confirmed working for AWS servers with the ubuntu image.
The following steps will be covered:

- Step 1: Set up Subtensor
- Step 2: Create a Wallet
- Step 3: Set up the Miner
- Step 4: Register Your Miner

Please note that Steps 1, 2, and 4 have detailed documentation available on the official Bittensor website (https://bittensor.com/documentation/intro/index).

Here, we will focus on step 3, setting up the miner, and for that we will be using the Center endpoint script.

## Getting Started with the Endpoint Miner Script

### Step 1: Set up the center-endpoint

The center-endpoint acts as a server that forwards requests from your miners. It provides an easy way to manage, update, experiment, and scale your miners. Follow these steps to set it up:

1. Start the server, and update and instal python and pip:
   ```
   sudo apt update && sudo apt upgrade -y
   sudo apt install python3-pip -y
   ```
2. Clone the center-endpoint repository:
   ```
   git clone https://github.com/TensorTeacher/endpoint-center
   ```
3. Install the required dependencies:
   ```
   cd endpoint-center
   pip3 install -r requirements.txt
   ```
4. You can either modify the `endpoint_center.py` script or use the default script that utilizes OpenAI. To run the default script, execute the following command:
   ```
   python3 endpoint_center.py --openai_api_key "YOUR_OPENAI_KEY" --auth_token "any_auth_token_you_want"
   ```
   If you want the script to run in the background, you can use the following command:
   ```
   nohup python3 endpoint_center.py --openai_api_key "YOUR_OPENAI_KEY" --auth_token "any_auth_token_you_want" &
   ```
   You can view the output using `tail -n 100 nohup.out`.

### Step 2: Set up the miner

You can run multiple miners on a single server. As a general guideline, allocate around 0.5 GB of RAM per miner. For example, if your server has 8 GB of RAM, you can run approximately 16 miners without any issues. Follow these steps to set up a miner:

1. Start the server, and update and instal python and pip:
   ```
   sudo apt update && sudo apt upgrade -y
   sudo apt install python3-pip -y
   ```
2. Install Bittensor by cloning the repository:
   ```
   git clone https://github.com/opentensor/bittensor
   cd bittensor
   python3 -m pip install -e .
   ```
3. Add the package to path:
   ```
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```
5. Create keys if you don't already have them:
   ```
   btcli new_coldkey
   btcli new_hotkey
   ```
7. You then need to add the endpoint miner script found at: https://github.com/TensorTeacher/endpoint-center/blob/main/endpoint_miner.py
   
   In the terminal to create a file with the endpoint miner script, enter:
   ```
   cat > endpoint_miner.py
   ```
   Then aste the endpoint miner script, press enter, and then press `Ctrl + D`.

8.  Install pm2:
   ```
   sudo apt-get install nodejs -y -y
   sudo apt-get install npm
   sudo npm install pm2 -g
   ```
10. It is recommended to use pm2 to manage miners instead of running them directly with Python. Once you have installed pm2, create a pm2 config file as shown below:

   ```
   cat > pm2-config.json
   ```

   Paste the following example config file, modifying it to match your requirements:

   ```json
   {
     "apps": [
       {
         "name": "miner_1",
         "script": "endpoint_miner.py",
         "interpreter": "python3",
         "args": "--name hotkey_name --axon.port your_axon_port --wallet.hotkey hotkey_name --wallet.name your_wallet_name --logging.debug --endpoint.url url_to_where_center_endpoint_is --endpoint.verify_token your_verification_token --subtensor.network finney --subtensor.chain_endpoint your_subtensor_endpoint:9944 --netuid netuid_you_want_to_mine_on",
         "error_file": "nohup1.err",
         "out_file": "nohup1.out"
       }
     ]
   }
   ```

   You can include multiple miners in the same pm2-config.json file.

11. Start the miner(s) by running the following command:
   ```
   pm2 start pm2-config.json
   ```
12. Recyle register
You then need to burn tao to get your miner registered. The cost varies depending on time and on what network. 
   ```
   btcli recycle_register -subtensor.network finney --netuid netuid_you_want_to_mine_on --wallet.name your_wallet_name --wallet.hotkey hotkey_name
   ```
