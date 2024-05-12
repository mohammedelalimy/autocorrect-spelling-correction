# autocorrect-spelling-correction
# first 
-- this project inspired from this repo : https://github.com/oliverguhr/spelling 
# how to use this code ?
## generate dataset use dataset that be suitable for your task in directory called data as txt file 
run 2 scripts for dataset :
-- convert_leipzig_data.sh
-- generate_dataset.py
## now you can run fine tuning script 
-- fine-tuning script

## all this steps i do it in colab notebook 
-- spelling_correction.ipynb

note:
in notebook i used script called run_summarization.py , don't worry this and fine-tuning script are same only names changed

final models pushed on hugging face hub here :
https://huggingface.co/Elalimy/english_spelling_correction

to deploy model you can use flask app: 
-- app.py

this is deployment for testing :
https://huggingface.co/spaces/Elalimy/autocorrect_english_spelling_sentence
