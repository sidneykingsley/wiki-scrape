import re
import os

input_file_name = 'musician-wiki-os'
input_dir = 'musician-names/'+input_file_name+'.txt'
output_folder_name = 'musician-names/'
output_file_name = 'musician-wiki-gn.txt'

if not os.path.exists(output_folder_name):
    os.makedirs(output_folder_name)
main_file = open(output_folder_name+output_file_name, 'a')

with open(input_dir) as f:
    for l in f:
        rpl = {'he':'they','she':'they','He':'They','She':'They',
                'his':'their','hers':'their','His':'Their','Hers':'Their',
                'him':'them','her':'their','Him':'Them','Her':'Their',}
        def replace(match):
            return rpl[match.group(0)]
        x = re.sub('|'.join(r'\b%s\b' % re.escape(s) for s in rpl), replace, l) 
        main_file.write(x)
        main_file = open(output_folder_name+output_file_name, 'a')