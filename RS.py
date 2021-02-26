import pandas as pd
import numpy as np
import json


class RS:
    POS_THD = 5
    def __init__(self, N_condition, N_drug, range_of_compute = 10):
        self.N_drug = N_drug
        self.N_condition = N_condition
        self.rating = np.zeros((N_condition, N_drug))
        self.range_of_compute = range_of_compute
        self.condition2id = None
        self.drug2id = None
    
    def save_dict(self, condition2id_dict, drug2id_dict):
        self.condition2id = condition2id_dict
        self.drug2id = drug2id_dict

    def train(self, train_data):
        count = np.zeros((self.N_condition, self.N_drug))
        for k in range(len(train_data)):
            i,j,r,c = train_data[k]
            c = 1
            self.rating[i][j] += r * c
            count[i][j] += c
        for i in range(self.N_condition):
            condition_cnt = 0
            for j in range(self.N_drug):
                condition_cnt += count[i][j]

    def eval(self, test_data):
        total_score = 0
        model_score = 0
        for k in range(len(test_data)):
            i,j,r,c = test_data[k]
            c = 1
            total_score += c
            posc,negc = self.recommend(i)
            if r >= self.POS_THD:
                if j in posc:
                    model_score += c
            else:
                if j in negc:
                    model_score += c
        return model_score / total_score

    def recommend(self, condition):
        condition_id = condition
        array = self.rating[condition_id,:]
        order = np.argsort(-array)
        pos_choices = order[0:self.range_of_compute]
        neg_choices = order[-self.range_of_compute-1:-1]
        return [pos_choices, neg_choices]

def read_data_csv(dataset_fname):
    df = pd.DataFrame(pd.read_csv(dataset_fname))
    condition_name = df['condition'].to_numpy()
    drug_name = df['drugName'].to_numpy()
    rating = df['rating'].to_numpy()
    usefulCount = df['usefulCount'].to_numpy()


    return [condition_name, drug_name, rating, usefulCount]

def build_dataset(data_fname, c2id, d2id):
    c,d,r,u = read_data_csv(data_fname)
    dataset = []
    n = 0
    for i in range(len(c)):
        if c[i] not in c2id or d[i] not in d2id:
            n += 1
            continue
        dataset.append([c2id[c[i]], d2id[d[i]], r[i], u[i]])
    dataset = np.array(dataset)
    print(f"Discard {n} samples in dataset {data_fname}")
    return dataset

if __name__ == '__main__':
    train_fname = "Data/drugsComTrain_raw.csv"
    test_fname = "Data/drugsComTest_raw.csv"
    c2id = json.load(open("Data/c2id.json"))
    d2id = json.load(open("Data/d2id.json"))
    
    train_dataset = build_dataset(train_fname, c2id, d2id)
    test_dataset = build_dataset(test_fname, c2id, d2id)

    rs = RS(len(c2id), len(d2id))
    rs.train(train_dataset)
    performance = rs.eval(test_dataset)
    print(performance * 100)

