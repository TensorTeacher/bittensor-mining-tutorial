Subnet 11 and subnet 21 will have a lot lower emission than net 1, while also having more miners.

This means cost efficiency becomes very important, since if you pay too much for compute, the generated tao will not cover the expenses.

## Earnings
Subent 11 will have 2048 miners, and initally get 512 Tao per day in emission. Half of this goes to miners.

Thus, the average miner will earn about 0.14 Tao per day. Thus the compute cost needs to be very low to be profitable, and you need a large number of miners for it to be worth your time.

## Setup Recommendation

### 1. Use an API
The easiest way to mine, will be to use an API, for use gpt-3.5-turbo by OpenAI. However, this might get expensive, and hard to make profitable.

If you do use an API, I suggest you try to limit the amount of tokens you input, and also set the max length of generation.

###2. Use a Small Open Source Model from Huggingface
There are some good models around 7B parameters in size, and you can hopefully fit them on cost efficient GPUs such as 3090 or 4090 GPUs.

You might have to limit the amount of tokens though not to run out of vram. If you need more vram you can always use an A6000.

Further, I highly recomend you use one GPU for many miners, for example using the endpoint-center repo: https://github.com/TensorTeacher/endpoint-center/tree/main

## Other tips

### Blacklist if Your Incentive Allows it

If you want to cut costs, and your miners have good enough incentive not to get deregistered, you can blacklist validators with low stakes.

Here are two ways to do it:
#### Option 1. 
Change the blacklisting value in the bittensor/_blacklist/init.py file.

If you are in the bittensor repo, you can use: nano bittensor/_blacklist/init.py
And then go down to "default = 0.0" and change the value from 0 to the desired value.

You need to restart the miners that are already running for the change to take effect.

#### Option 2.
Pass the flag "--neuron.blacklist.default_stake" to you miner, followed by the stake you want to set as minimum.

