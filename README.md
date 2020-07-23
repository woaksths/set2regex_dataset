# set2regex_dataset


## Install 
    $git clone https://github.com/0xnurl/fado-python3.git
    $python3 -m venv venv
    $source venv/bin/activate
    $pip install -r requirements.txt
    $python fado-python3/setup.py install

## Usage 
    # It takes a lot of times, so you had better download the file 
    $python generate_regex.py
    $python main.py


## Downloads
    [downloads] https://drive.google.com/file/d/1BdOuBAjYpiJNezzf3IQYGFIJIxg7LA2K/view?usp=sharing
    # After download the files(default set_size=50), you can define the set size of dataset 
    $ python make_dataset.py --dataset_path $dataset_path --set_size $set_Size
