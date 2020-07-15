from utils import get_dataset, file_write
from generate_string import get_positive_samples, get_negative_samples, preprocess_target, preprocess_source
import random


def main():
    regex_set = get_dataset('data/regex/star0.txt')+get_dataset('data/regex/star1.txt')\
            + get_dataset('data/regex/star2.txt')+get_dataset('data/regex/star3.txt')
    dataset = []
    num_samples = 50

    for regex in regex_set:
        positive_samples = get_positive_samples(regex, num_samples)
        if len(positive_samples) < num_samples:
            positive_samples.extend([random.choice(positive_samples) for _ in range(num_samples-len(positive_samples))])

        negative_samples = get_negative_samples(regex, regex_set, num_samples)
        positive_samples = preprocess_source(positive_samples)
        negative_samples = preprocess_source(negative_samples)
        regex = preprocess_target(regex)
        pair_data = '\t'.join(positive_samples) + '\t<sep>\t' +\
                    '\t'.join(negative_samples) + '\t<sep>\t' + regex
        dataset.append(pair_data)

    file_write('data/pair_data.txt', dataset)


if __name__ == "__main__":
    main()

