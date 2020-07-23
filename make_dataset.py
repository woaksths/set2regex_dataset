import os
import argparse


def file_write(dataset, file_name, set_size):
    if not os.path.exists('data/baseline'):
        os.makedirs('data/baseline')
    if not os.path.exists('data/set2regex'):
        os.makedirs('data/set2regex')
    
    with open('data/baseline/'+file_name,'w') as fw1, open('data/set2regex/'+file_name, 'w') as fw2:
        for pair in dataset:
            pos, neg, regex = pair.split('<sep>')
            pos = pos.strip().split('\t')
            neg = neg.strip().split('\t')
            regex = regex.strip()
            pos = pos[:set_size]
            neg = neg[:set_size]
            baseline_data = ' <sep> '.join(pos) +' <sep> ' + ' <sep> '.join(neg) +'\t' +regex
            our_model_data = '\t'.join(pos)+'\t'+ '\t'.join(neg) +'\t'+regex
            fw1.write(baseline_data +'\n')
            fw2.write(our_model_data +'\n')


parser = argparse.ArgumentParser(description='make dataset that have pairs of pos and '
                                             'neg samples with user defined set size')
parser.add_argument('--set_size', required=True, help='type set size')
parser.add_argument('--dataset_path', required=True, help='type the path of dataset')
args = parser.parse_args()
set_size = int(args.set_size)
dataset_path = args.dataset_path

with open(dataset_path, 'r') as rf:
    pair_dataset = rf.read().split('\n')
    star0_set = pair_dataset[0:20000]
    star1_set = pair_dataset[20000:40000]
    star2_set = pair_dataset[40000:60000]
    star3_set = pair_dataset[60000:]
    
    train_ratio = int(0.8 * 20000)
    valid_ratio = int(0.1 * 20000)
    test_ratio = int(0.1 * 20000) 

    train = star0_set[:train_ratio] + star1_set[:train_ratio] + star2_set[:train_ratio]+star3_set[:train_ratio]
    valid = star0_set[train_ratio:train_ratio+valid_ratio] +star1_set[train_ratio:train_ratio+valid_ratio]+star2_set[train_ratio:train_ratio+valid_ratio]+ star0_set[train_ratio:train_ratio+valid_ratio]
    test = star0_set[train_ratio+valid_ratio:]+star1_set[train_ratio+valid_ratio:]+star2_set[train_ratio+valid_ratio:]+star3_set[train_ratio+valid_ratio:]   
    
    print('train size{} valid size{} test size{}'.format(len(train), len(valid), len(test)))
    
    file_write(train, 'pos_neg_train.txt', set_size=set_size)
    file_write(valid, 'pos_neg_valid.txt', set_size=set_size)
    file_write(test, 'pos_neg_test.txt', set_size=set_size)

