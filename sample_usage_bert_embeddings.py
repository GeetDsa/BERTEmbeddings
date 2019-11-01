import bertEmbeddings 

bertEmbedding = bertEmbeddings.BertEmbeddings() 

embeddings=bertEmbedding.get_features(["killthemall"])
for t,e in embeddings:
    print("token:",t)
    print("embedding:",e)
