To copy weights and set them for your validator, you can use the script below. You probably want to make a loop for it, to set weights frequently.
```
uid_to_copy=5
wallet_name=""
hotkey_name=""


import bittensor as bt
import torch
import bittensor

def set_weights(moving_averaged_scores,netuid,subtensor, metagraph, wallet, __spec_version__):
    # Calculate the average reward for each uid across non-zero values.
    # Replace any NaN values with 0.
    raw_weights = torch.nn.functional.normalize(moving_averaged_scores, p=1, dim=0)
    print("raw_weights", raw_weights)
    print("top10 values", raw_weights.sort()[0])
    print("top10 uids", raw_weights.sort()[1])

    # Process the raw weights to final_weights via subtensor limitations.
    (processed_weight_uids, processed_weights,) = bt.utils.weight_utils.process_weights_for_netuid(
        uids=metagraph.uids.to("cpu"),
        weights=raw_weights.to("cpu"),
        netuid=netuid,
        subtensor=subtensor,
        metagraph=metagraph,
    )
    print("processed_weights", processed_weights)
    print("processed_weight_uids", processed_weight_uids)

    # Set the weights on chain via our subtensor connection.
    subtensor.set_weights(
        wallet=wallet,
        netuid=netuid,
        uids=processed_weight_uids,
        weights=processed_weights,
        wait_for_finalization=True,
        version_key=__spec_version__,
    )
subtensor = bittensor.subtensor()

import bittensor as bt

metagraph = bt.metagraph(netuid=1,lite=False)
metagraph.weights


moving_averaged_scores = metagraph.weights[5]
netuid="1"
chain_weights = metagraph.weights[5] #torch.zeros(subtensor.subnetwork_n(netuid=1))


wallet = bittensor.wallet(name=wallet_name, hotkey=hotkey_name)

__version__ = "1.2.0"
version_split = __version__.split(".")
__spec_version__ = (1000 * int(version_split[0])) + (10 * int(version_split[1])) + (1 * int(version_split[2]))


set_weights(moving_averaged_scores,netuid,subtensor, metagraph, wallet, __spec_version__)

```
