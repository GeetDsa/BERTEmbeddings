# BERTEmbeddings
To obtain bert embeddings from a given text.

The program has been derived from the tutorial, https://towardsdatascience.com/nlp-extract-contextualized-word-embeddings-from-bert-keras-tf-67ef29f60a7b.

This program puts everything in a single chunk, and allows to be executed on CPU/GPU instead of TPU.

It uses `modeling.py` and `tokenization.py` from the original implementation of bert.

Also, please change the path at `BERT_PRETRAINED_DIR=` in `bertEmbeddings.py` file to point to BERT model.


`sample_usage_bert_embeddings.py` shows the sample usage of the program.
