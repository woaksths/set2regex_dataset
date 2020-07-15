import rstr
from FAdo.reex import *
from FAdo.fa import *


def get_positive_samples(regex, set_num):
    positive_samples = set()
    early_stop_cnt = 0
    while len(positive_samples) < set_num:
        regex = regex.replace('*', '{0,4}')
        string = rstr.xeger(regex)
        if string.strip() == '':
            print('empty string can not be added into dataset')
            continue
        if early_stop_cnt == 30:
            break
        if string in positive_samples:
            early_stop_cnt += 1
            continue
        if len(string) < 100:
            positive_samples.add(string)
            early_stop_cnt = 0
    positive_samples = list(positive_samples)
    positive_samples.sort()
    return positive_samples


def get_negative_samples(target_regex, regex_set, set_size):
    neg_samples = set()
    while len(neg_samples) < set_size:
        random_regex = random.choice(regex_set)
        if target_regex == random_regex:
            continue
        target_dfa = str2regexp(target_regex).toDFA()
        random_dfa = str2regexp(random_regex).toDFA()
        negative_dfa = ~target_dfa & random_dfa
        neg_samples.add(negative_dfa.witness())
    neg_samples = list(neg_samples)
    neg_samples.sort()
    return neg_samples


def preprocess_target(regex):
    regex = list(regex)
    regex = ' '.join(regex)
    regex = regex.replace('( 0 | 1 | 2 | 3 ) *', '[0-3]*')
    regex = regex.replace('( 0 | 1 | 2 | 3 )', '[0-3]')
    return regex


def preprocess_source(source_list):
    for i in range(len(source_list)):
        if source_list[i] == '<pad>':
            continue
        source_list[i] = list(source_list[i])
        source_list[i] = ' '.join(source_list[i])
    return source_list


