# Bittensor Mining Tutorial

This tutorial will guide you through the process of setting up a miner on the Bittensor Network, a blockchain for decentralized AIs. The following steps will be covered:

- Step 1: Set up Subtensor
- Step 2: Create a Wallet
- Step 3: Set up the Miner
- Step 4: Register Your Miner

Please note that Steps 1, 2, and 4 have detailed documentation available on the official Bittensor website (https://bittensor.com/documentation/intro/index).

Here, we will focus on step 3, setting up the miner, and for that we will be using the Center endpoint script.

## Getting Started with the Endpoint Miner Script

### Step 1: Set up the center-endpoint

The center-endpoint acts as a server that forwards requests from your miners. It provides an easy way to manage, update, experiment, and scale your miners. Follow these steps to set it up:

1. Start the server and ensure that Python and pip are installed.
2. Clone the center-endpoint repository:
   ```
   git clone <center-endpoint-repo>
   cd center-endpoint
   ```
3. Install the required dependencies:
   ```
   pip3 install -r requirements.txt
   ```
4. You can either modify the `app.py` script or use the default script that utilizes OpenAI. To run the default script, execute the following command:
   ```
   python3 app.py --openai_key "YOUR_OPENAI_KEY"
   ```
   If you want the script to run in the background, you can use the following command:
   ```
   nohup python3 app.py --openai_key "YOUR_OPENAI_KEY" &
   ```
   You can view the output using `tail -n 100 nohup.out`.

### Step 2: Set up the miner

You can run multiple miners on a single server. As a general guideline, allocate around 0.5 GB of RAM per miner. For example, if your server has 8 GB of RAM, you can run approximately 16 miners without any issues. Follow these steps to set up a miner:

1. Install Bittensor by cloning the repository:
   ```
   git clone https://github.com/opentensor/bittensor
   cd bittensor
   python3 -m pip install -e .
   ```
2. Copy the script for the endpoint miner using the following command:
   ```
   cat > endpoint_miner.py
   ```
   Paste the endpoint miner script, press enter, and then press `Ctrl + D`.

3. Start the miner by running the following command:
   ```
   python3 endpoint_miner.py --name hotkey_name --axon.port your_axon_port --wallet.hotkey hotkey_name --wallet.name your_wallet_name --logging.debug --endpoint.url url_to_where_center_endpoint_is --endpoint.verify_token your_verification_token --subtensor.network finney --subtensor.chain_endpoint your_subtensor_endpoint:9944 --netuid 1
   ```

   It is recommended to use pm2 to manage miners instead of running them directly with Python. Once you have installed pm2, create a pm2 config file as shown below:

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
         "args": "--name hotkey_name --axon.port your_axon_port --wallet.hotkey hotkey_name --wallet.name your_wallet_name --logging.debug --endpoint.url url_to_where_center_endpoint_is --endpoint.verify_token your_verification_token --subtensor.network finney --subtensor.chain_endpoint your_subtensor_endpoint:9944 --netuid 1",
         "error_file": "nohup1.err",
         "out_file": "nohup1.out"
       }
     ]
   }
   ```

   You can include multiple miners in the same pm2-config.json file.

4. Start the miner(s) by running the following command:
   ```
   pm2 start pm2-config.json
   ```



