# -*- coding: utf-8 -*-

def process_data_file(file,target_path,name):
    tmp_path = target_path+name
    label,seq_in,seq_out = tmp_path+'.label',tmp_path+'.seq.in',tmp_path+'.seq.out'
    with open(file,'r') as read_file,open(label,'w') as label_file,open(seq_in,'w') as seq_in_file,open(seq_out,'w') as seq_out_file:
        for line in read_file:
            print line
            if 'EOS' in line:
                array = line.split('EOS')
                print array
                if 'BOS' in array[0]:
                    seq_in_file.write((array[0].replace('BOS','').strip())+'\n')
                if array[1] == "" or array[1] == '\n':
                    continue
                else:
                    print array[1],array[1] != "" or array[1] != '\n'
                    eos_str,label = splilt_last_word(array[1])
                    label_file.write(label + "\n")
                    seq_out_file.write(eos_str + "\n")
    return

def process_data_test_file(file,traget_path,name):
    pass
def splilt_last_word(sentence):
    word_array = sentence.split()
    print word_array
    if len(word_array) >= 2:
        return ' '.join(word_array[:-1]),word_array[-1]
    else:
        return "",""

def main():
    source_data_path = "../data/ATIS_samples/"
    # process_data_file('atis.test.iob','test/','test')
    process_data_file('atis.train.w-intent.iob', 'train/', 'train')

if __name__ == "__main__":
    main()