# Hello transformers

In 2017, researchers at Google published a paper that proposed a novel neural network
architecture for sequence modeling. Dubbed the Transformer, this architecture outperformed
recurrent neural networks (RNNs) - Attention is all you need

an effective transfer learning method called ULMFiT showed that training long
short-term memory (LSTM) networks on a very large and diverse corpus could produce stateof-the-art text classifiers with little labeled data.

These advances were the catalysts for two of today’s most well-known transformers: the
Generative Pretrained Transformer (GPT) and Bidirectional Encoder Representations from
Transformers (BERT)

## Encoder Decoder Framework

These architectures contain a feedback loop in the network connections that allows information
to propagate from one step to another, making them ideal for modeling sequential data like text.
As illustrated on the left side of Figure 1-2, an RNN receives some input (which could be a
word or character), feeds it through the network, and outputs a vector called the hidden state

Good blog for reference
http://karpathy.github.io/2015/05/21/rnn-effectiveness/

## Attention mechanism

This is where attention comes in: it lets
the decoder assign a different amount of weight, or “attention,” to each of the encoder states at
every decoding timestep. T

With the transformer, a new modeling paradigm was introduced: dispense with recurrence
altogether, and instead rely entirely on a special form of attention called self-attention. We’ll
cover self-attention in more detail in Chapter 3, but the basic idea is to allow attention to
operate on all the states in the same layer of the neural network.


## transfer learning

framework to adapt pretrained LSTM models for various tasks.
As illustrated in Figure 1-8, ULMFiT involves three main steps:
Pretraining
The initial training objective is quite simple: predict the next word based on the previous
words. This task is referred to as language modeling. The elegance of this approach lies in
8
9
the fact that no labeled data is required, and one can make use of abundantly available text
from sources such as Wikipedia.
Domain adaptation
Once the language model is pretrained on a large-scale corpus, the next step is to adapt it to
the in-domain corpus (e.g., from Wikipedia to the IMDb corpus of movie reviews, as in
Figure 1-8). This stage still uses language modeling, but now the model has to predict the
next word in the target corpus.
Fine-tuning
In this step, the language model is fine-tuned with a classification layer for the target task
(e.g., classifying the sentiment of movie reviews in Figure 1-8).

for transfer learning ulm fit was used.

page 25

