# Research Concepts for Text Summarization


## Generation Way
* `gen-ext`: Extractive Summarization 
* `gen-abs`: Abstractive Summarizatin
* `gen-2stage` Two-stage Summarization (compressive, hybrid)

## Regressive Way
* `regr-auto`:  Autoregressive Decoder (Pointer network) 
* `regr-nonauto`: Non-autoregressive Decoder (Sequence labeling)

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
* `task-video`: Video-based Summarization
* `task-code`: Source Code Summarization
* `task-control`: Controllable Summarization
* `task-event`: Event-based Summarization
* `task-longtext`: Summarization for Long Text
* `task-knowledge`: Text Summarization with External Knowledge
* `task-highlight`: Pick out important content and emphasize
* `task-analysis`: Model Understanding or Interpretability


## Architecture (Mechanism)
* `arch-rnn`: Recurrent Neural Networks (LSTM, GRU)
* `arch-cnn`: Convolutional Neural Networks (CNN)
* `arch-transformer`: Transformer
* `arch-graph`: Graph Neural Networks or Statistic Graph Models
* `arch-gnn`: Graph Neural Networks
* `arch-att`: Attention Mechanism
* `arch-pointer`: Pointer Layer
* `arch-coverage`: Coverage Mechanism


## Training
* `train-multitask`: Multi-task Learning
* `train-multilingual`: multi-lingual Learning
* `train-multimodal`: Multi-modal Learning
* `train-auxiliary`: Joint Training
* `train-transfer`: Cross-domain Learning, Transfer Learning, Domian Adaptation
* `train-active`: Active Learning, Boostrapping
* `train-adver`: Adversarial Learning
* `train-template`: Template-based Summarization
* `train-augment`: Data Augmentation
* `train-curriculum`: Curriculum Learning
* `train-lowresource`: Low-resource Summarization
* `train-retrieval`: Retrieval-based Summarization
* `train-meta`: Meta-learning


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


## Relaxation/Training Methods for Non-differentiable Functions
* `nondif-straightthrough`: Straight-through Estimator
* `nondif-gumbelsoftmax`: Gumbel Softmax
* `nondif-minrisk`: Minimum Risk Training
* `nondif-reinforce`: REINFORCE

## Adversarial Methods
* `adv-gan`: Generative	Adversarial Networks
* `adv-feat`: Adversarial Feature Learning
* `adv-examp`: Adversarial Examples
* `adv-train`: Adversarial Training


## Latent Variable Models
* `latent-vae`: Variational Auto-encoder
* `latent-topic`: Topic Model

## Dataset
* `data-new`: Constructing a new dataset


## Evaluation
* `eval-metric-rouge`: ROUGE
* `eval-metric-bertscore`: BERTScore
* `eval-aspect-coherence`: Coherence
* `eval-aspect-redundancy`: Redundancy of Summary 
* `eval-aspect-factuality`: Factuality
* `eval-aspect-abstractness`: Abstractness