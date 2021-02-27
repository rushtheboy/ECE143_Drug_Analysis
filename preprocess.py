import pandas as pd
import numpy as np
import utils
import json

if __name__ == '__main__':
    uc1_fname = "Data/drugsComTrain_raw.csv"
    uc2_fname = "Data/drugsComTest_raw.csv"
    wb_fname = "Data/webmd.csv"
    uc1 = pd.read_csv(uc1_fname)
    uc2 = pd.read_csv(uc2_fname)
    wb = pd.read_csv(wb_fname)

    condition_set = set()
    #for condition_dataset in [uc1['condition'], uc2['condition'], wb['Condition']]:
    #for condition_dataset in [uc1['condition'], uc2['condition']]:
    for condition_dataset in [uc1['condition']]:
        for condition in condition_dataset:
            if utils.condition_filter(condition):continue
            condition_set.add(condition)
    c2id = {} 
    for condition in condition_set:
        c2id[condition] = len(c2id)
    json.dump(c2id, open('Data/c2id.json','w'))
    
    drug_set = set()
    #for drug_dataset in [uc1['drugName'], uc2['drugName']]:
    for drug_dataset in [uc1['drugName']]:
        for drug in drug_dataset:
            if utils.drug_filter(drug):continue
            drug_set.add(drug)
    '''
    for drug in wb['Drug']:
        drug = drug.split(' ',1)[0]
        if utils.drug_filter(drug):continue
        drug_set.add(drug)
    '''
    d2id = {} 
    for drug in drug_set:
        d2id[drug] = len(d2id)
    json.dump(d2id, open('Data/d2id.json','w'))
