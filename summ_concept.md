# Research Concepts for Text Summarization


## Generation Way
* `gen-ext`: Extractive Summarization 
* `gen-abs`: Abstractive Summarizatin
* `gen-2stage` Two-stage Summarization (compressive, hybrid)

## Regressive Way
* `regr-auto`:  Autoregressive (Pointer network) 
* `regr-nonauto`: Non-autoregressive (Sequence labeling)

## Supervision
* `sup-sup`: Supervised Learning
* `sup-weak`  (implies `sup-sup`): Weakly Supervised Learning
* `sup-unsup`: Unsupervised Learning

## Task Settings
* `task-single`: Single-document Summarization
* `task-multi`: Multi-document Summarization
* `task-senCompre:` Sentence Compression
* `task-sci`: Scientific Paper
* `task-multimodal`: Multi-modal Summarization
* `task-aspect`: Aspect-based Summarization
* `task-opinion`: Opinion Summarization
* `task-questoin`: Question-based Summarization
* `task-code`: Source Code Summarization
* `task-control`: Controllable summarization
* `task-longtext`: Summarization for Long Text
* `task-knowledge`: Text Summarization with External Knowledge
* `task-interpret`: Model Understanding or Interpretability


## Architecture (Mechanism)
* `arch-rnn`: Recurrent Neural Networks (LSTM, GRU)
* `arch-cnn`: Convolutional Neural Networks (CNN)
* `arch-transformer`: Transformer
* `arch-graph`: Graph Neural Networks or Statistic Graph Models
* `arch-att`: Attention Mechanism
* `arch-pointer`: Pointer Layer
* `arch-coverage`: Coverage Mechanism


## Training
* `train-multitask`: Multi-task Learning
* `train-multimodal`: Multi-modal Learning
* `train-auxiliary`: Joint Training
* `train-transfer`: Cross-domain Learning, Transfer Learning, Domian Adaptation
* `train-multiling`: Bi-lingual, Multi-lingual Learning
* `train-active`: Active Learning, Boostrapping
* `train-adver`: Adversarial Learning
* `train-template`: Template-based Summarization


## Pre-trained Models
* `pre-word2vec`: word2vec
* `pre-glove`: GLoVe
* `pre-bert`: BERT
* `pre-elmo`: ELMo
* `pre-hibert`: HiBERT
* `pre-bart`: BART
* `pre-pegasus`: PEGASUS
* `pre-unilm`: UNILM
* `pre-mass`: MASS


## Dataset
* `data-new`: Constructing a new dataset


## Evaluation
* `eval-metric-rouge`: ROUGE
* `eval-metric-bertscore`: BERTScore
* `eval-aspect-coherence`: Coherence
* `eval-aspect-redundancy`: Redundancy of Summary 
* `eval-aspect-factuality`: Factuality
* `eval-aspect-abstractness`: Abstractness