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