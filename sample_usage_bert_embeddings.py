import bertEmbeddings 
print("Note: change BERT_PRETRAINED_DIR= in bertEmbedding.py script")

bertEmbedding = bertEmbeddings.BertEmbeddings() 

embeddings=bertEmbedding.get_features(["Hey!! I am the sample usage for bert embeddings."])
for t,e in embeddings:
    print("token:",t)
    print("embedding:",e)
