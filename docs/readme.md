#Getting Started with Bittensor Mining

##Inital remarks
Mining on net 1 is very different from how it was to mine on net 3.

The goal is to give the best and most unique replies to prompts sent by the validators in a chat format. You can check out the code that validators use for scoring here: https://github.com/opentensor/validators

There is a big penalty for generating replies that are similar to replies generated by other miners. Therefore it can be a good idea to use unusual models, high temperature (randomness when generating) and prompt injection to get more unique responses.


##Models to Use
One popular model to use, is gpt-3.5-turbo (chatgpt), by OpenAI. However, since it is widely used, you need to make your generations different somehow, for example through prompt injection or high temperature.

You can also browse Huggingface for open source models, for exampel by searching on "chat": https://huggingface.co/models?sort=trending&search=chat

Or you can simply Google "best open source chat models".

##Prompt injection
Prompt injection means in text giving specific instructions to the model on what type of response to generate.

For example, if you get the prompt "What is the capital of Egypt?", you could have a prompt you add to your questions, for example "Answer using academic language.", so the full prompt would be "What is the capital of Egypt? Answer using academic language."

This way, the responses would be more academic than responses by other miners using, which might give you a better uniqueness score.



##GPU Recommendations
Most miners use either Vast.ai for rundpod.io for GPUs.

What GPUs are most suitable depends on the model you want to run, as well as your price sensetivity.

4090 GPUs are both extremely fast and cost effective, so if your model fits in the 24GB vram it is highly recommended

A6000 Ada and L40 GPUs are roughly as fast as 4090s, but have twice the vram, meaning they can fit bigger models. However, they are about twice as expensive.

Normal A6000s are a cheaper option if you need 48 GB ram, but the GPUs are slower.

If you need even more ram H100 is the best option, although expensive, they are the fastest in most cases, and has 80 GB vram.