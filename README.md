# SOME
SOME: Reference-less Sub-Metrics Optimized for Manual Evaluations of Grammatical Error Correction  
Paper: https://www.aclweb.org/anthology/2020.coling-main.573.pdf

# Dependencies
- Python >= 3.6.0
- Pytorch >= 1.3.1
- transformers >= 3.0.2

# Trained models and Dataset
- Download trained model [here](https://drive.google.com/file/d/1uoAReQK3f5g9CEy8rV4haSzXll8NqVHW/view?usp=sharing).
- These model are trained on [TMU-GFM-Dataset](https://github.com/tmu-nlp/TMU-GFM-Dataset).

These models can be downloaded by:

```bash
S1="1uoAReQK3f5g9CEy8rV4haSzXll8NqVHW";
S2="gfm-models.zip";
CONFIRM=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate "https://drive.google.com/uc?export=download&id=$S1" -O- | sed -En 's/.*confirm=([0-9A-Za-z_]+).*/\1/p');
wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$CONFIRM&id=$S1" -O $S2;
rm -f /tmp/cookies.txt

unzip gfm-models.zip
tree gfm-models
# gfm-models
# ├── fluency
# │   ├── config.json
# │   ├── pytorch_model.bin
# │   ├── special_tokens_map.json
# │   ├── tokenizer_config.json
# │   ├── training_args.bin
# │   └── vocab.txt
# ├── grammer
# │   ├── config.json
# │   ├── pytorch_model.bin
# │   ├── special_tokens_map.json
# │   ├── tokenizer_config.json
# │   ├── training_args.bin
# │   └── vocab.txt
# └── meaning
#     ├── config.json
#     ├── pytorch_model.bin
#     ├── special_tokens_map.json
#     ├── tokenizer_config.json
#     ├── training_args.bin
#     └── vocab.txt
```



# How to use

```
python some.py [hypothesis file] [source file] \
    --g-dir [directry path of grammar model] \
    --f-dir [directry path of fluency model] \
    --m-dir [directry path of meaning model] > predict_score
```
More option can be found ```python some.py -h```.  
The default weight of each model are tuned with Kendall tau on [Grundkiewicz et al. (2015).](https://www.aclweb.org/anthology/D15-1)
Details can be found the paper.