# IMPORTS BASICS
import numpy as np
# Importação das Ferramentas do Doc2Vec
import gensim
from gensim.utils import simple_preprocess
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

class DocToVector:
    def __init__(self) -> None:
        pass
    
    def __tagged_document(self, list_of_list_of_words):
        # Iterate over each list of words in the list of lists
        for i, list_of_words in enumerate(list_of_list_of_words):
            yield gensim.models.doc2vec.TaggedDocument(list_of_words, [i])
            
    def __create_X_vector_doc2vec(self, df, column_name, vector_size, epochs=40):
        # Create list of lists of words from df[column_name]
        doc_tokenized = [simple_preprocess(doc) for doc in df[column_name].values]
        # Create taggedDocument structure
        training_data = list(self.__tagged_document(doc_tokenized))
        # Create a Doc2Vec model
        model = Doc2Vec(vector_size=vector_size, min_count=2, epochs=epochs) # pass vector_size as a parameter
        # Build the model's vocabulary
        model.build_vocab(training_data)
        # Train the model with the documents
        model.train(training_data, total_examples=model.corpus_count, epochs=model.epochs)
        # Get vectors for the documents
        doc_vectors = [model.infer_vector(doc.words) for doc in training_data]
        return doc_vectors
    
    def create_XY_vector(self, df_news, vector_size, epochs):
        # Create document vectors for articles
        X_article = self.__create_X_vector_doc2vec(df_news, "article", vector_size, epochs)
        # Create document vectors for titles
        X_title = self.__create_X_vector_doc2vec(df_news, "title", vector_size, epochs)
        # Concatenate article and title vectors horizontally
        X = np.concatenate((X_article, X_title),axis=1)
        Y = df_news['manual_relevance_class'] # Classes de 0 para rejeitado e 1 para aceito
        
        return X, Y

    