import csv
import config

def read_data_header(subset_name=config.data_subset):      
    subset = {}
    with open('data/LibriSpeech/SPEAKERS.TXT') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='|')
        for row in spamreader:
            if row[0].startswith(';'): 
                continue
            if row[2].strip() == subset_name:
                subset[row[0].strip()] = dict({'sex':row[1].strip()})
                subset[row[0].strip()]['chapters'] = []
    with open('data/LibriSpeech/CHAPTERS.TXT') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='|')
        for row in spamreader:
        	if row[0].startswith(';'):
        		continue
        	if row[3].strip() == subset_name:
        		subset[row[1].strip()]['chapters'].append(row[0].strip())
    return subset


def males_keys(dico):
    result = []
    for key, value in dico.items():
        if value['sex'] == 'M':
            result += [key]
    return result

def females_keys(dico):
    result = []
    for key, value in dico.items():
        if value['sex'] == 'F':
            result += [key]
    return result

# dico =  read_data_header('dev-clean')
# print females_keys(dico)