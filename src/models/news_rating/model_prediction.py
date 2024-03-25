# Imports Basics
import pandas as pd
import numpy as np
# Importação dos Modelos
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.svm import LinearSVC
# Importações do Sklearn
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
# Imports News Rating
from news_rating.doc_to_vector import DocToVector
from news_rating.confidence_calculation import ConfidenceCalculation

class ModelPrediction:
    def __init__(self) -> None:
        # definindo uma semente global
        np.random.seed(7)
        # Definição dos modelos
        self.models = []
        self.models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
        self.models.append(('KNC', KNeighborsClassifier()))
        self.models.append(('KNC-3', KNeighborsClassifier(3)))
        self.models.append(('CART', DecisionTreeClassifier()))
        self.models.append(('GNB', GaussianNB()))
        self.models.append(('SVM', SVC()))
        self.models.append(('LDA', LinearDiscriminantAnalysis()))
        self.models.append(('CART-dep-5',DecisionTreeClassifier(max_depth=5)))
        self.models.append(('GPC',GaussianProcessClassifier()))
        self.models.append(('RF', RandomForestClassifier(n_estimators=100)))
        self.models.append(('RF-n-estimators-10',RandomForestClassifier(max_depth=10, n_estimators=50, max_features=1)))
        self.models.append(('SVC', LinearSVC(random_state=0, tol=1e-5)))
        self.models.append(('ETC', ExtraTreesClassifier()))
        # Varibles Global
        self.dtv = DocToVector()
        self.confC = ConfidenceCalculation()
        
    def sort_model(self, models):
        models.sort()
        best_model = models[0]
        for aux in models:
            if aux[2] >= best_model[2]:
                if aux[3] != 0 and aux[3] < best_model[3]:
                    best_model = aux
        return best_model
        
    def cross_model(self, x, y, fold, name_model=None):

        if name_model == None:
            accuracy = []
            # Nome, Modelo dos modelos de IA
            for name, model in self.models: 
                scores = cross_val_score(model, x, y, cv=fold, scoring='balanced_accuracy') # Calculo do Score
                accuracy.append((name, model, scores.mean(), scores.std()))

        else:
            score = cross_val_score(name_model[1], x, y, cv=fold, scoring='balanced_accuracy')
            accuracy = (name_model[0], name_model[1], score.mean(), score.std())
            
        best_model = self.sort_model(accuracy)

        return best_model
    
    def train_model(self, pair_model, df_news, vector_size, epochs, fold):
        name, model = pair_model
        x, y = self.dtv.create_XY_vector(df_news, vector_size, epochs)
        scores = cross_val_score(model, x, y, cv=fold, scoring='balanced_accuracy')
        accuracy = (name, model, scores.mean(), scores.std())
        
        return accuracy
    
    def quality_assessment(self, df_news=None, operation=0, X_confidences=None):
        isFind = False 
        
        df_copy = df_news.copy() 

        while(not isFind): 
            # Obtém as previsões de relevância automática convertidas para inteiros
            predicts = list(df_copy['automatic_relevance_class'].astype(int)) 
            
            # Cria uma lista de índices das instâncias no DataFrame
            index_unlabel = list(range(0, len(df_copy['manual_relevance_class']))) 
            
            # Obtém os itens de menor confiança
            item, item_0, item_1 = self.confC.get_least_confidents(index_unlabel, X_confidences, predicts) 
            
            # Define o modo de operação
            doc_id, confidence, label = self.confC.set_mode(operation, predicts, X_confidences, index_unlabel, item, item_0, item_1) 
            
            # Verifica se a classe de relevância manual na instância selecionada é NaN
            if(pd.isna(df_copy['manual_relevance_class'][doc_id])): 
                # Se for NaN, a condição é encontrada e o loop é encerrado
                isFind = True 
            else:
                # Se não for NaN, remove a instância do DataFrame e sua confiança correspondente
                df_copy.drop(doc_id, inplace=True) 
                np.delete(X_confidences, doc_id, axis=0)
        
        # Retorna a instância selecionada, sua confiança e sua classe de relevância
        return doc_id, confidence, label
    
    def automatic_relevance_class(self, df_news, name_model, model, x):
        predicts = model.predict(x).astype(int)
        df_news['automatic_relevance_class'] = predicts
        df_news['relevance_model'] = name_model
        
        return df_news