# Research Concepts for Text Summarization


## Generation Way
* `gen-ext`: Extractive Summarization 
* `gen-abs`: Abstractive Summarization
* `gen-2stage` Two-stage Summarization (compressive, hybrid)

## Regressive Way
* `regr-auto`:  Autoregressive Decoder (Pointer network) 
* `regr-nonauto`: Non-autoregressive Decoder (Sequence labeling)


## Task Settings
* `task-singleDoc`: Single-document Summarization
* `task-multiDoc`: Multi-document Summarization
* `task-senCompre:` Sentence Compression
* `task-sci`: Scientific Paper
* `task-radiologyReport`: Radiology Reports
* `task-multimodal`: Multi-modal Summarization
* `task-aspect`: Aspect-based Summarization
* `task-opinion`: Opinion Summarization
* `task-review`: Review Summarization
* `task-meeting`: Meeting-based Summarization
* `task-conversation`: Consersation-based Summarization
* `task-medical`: Medical text-related Summarization
* `task-covid`: COVID-19 related Summarization
* `task-query`: query-based Summarization
* `task-question`: question-based Summarization
* `task-video`: Video-based Summarization
* `task-code`: Source Code Summarization
* `task-control`: Controllable Summarization
* `task-event`: Event-based Summarization
* `task-longtext`: Summarization for Long Text
* `task-knowledge`: Text Summarization with External Knowledge
* `task-highlight`: Pick out important content and emphasize
* `task-analysis`: Model Understanding or Interpretability
* `task-novel`: Novel Chapter Generation
* `task-argument`: Automatic Argument Summarization


## Architecture (Mechanism)
* `arch-rnn`: Recurrent Neural Networks (LSTM, GRU)
* `arch-cnn`: Convolutional Neural Networks (CNN)
* `arch-transformer`: Transformer
* `arch-graph`: Graph Neural Networks or Statistic Graph Models
* `arch-gnn`: Graph Neural Networks
* `arch-textrank`: TextRank
* `arch-att`: Attention Mechanism
* `arch-pointer`: Pointer Layer
* `arch-coverage`: Coverage Mechanism


## Training
* `train-sup`: Supervised Learning
* `train-unsup`: Unsupervised Learning
* `train-weak`:  (implies `train-sup`): Weakly Supervised Learning
* `train-multitask`: Multi-task Learning
* `train-multilingual`: Multi-lingual Learning
* `train-multimodal`: Multi-modal Learning
* `train-auxiliary`: Joint Training
* `train-transfer`: Cross-domain Learning, Transfer Learning, Domain Adaptation
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
* `pre-T5`: Text-to-Text Transfer Transformer
* `pre-S2ORC`: Pretrained model on semantic scholar open research corpus
* `pre-sciBERT`: Scientific paper based pre-trained model
* `pre-SPECTER`: Scientific Paper Embeddings using Citationinformed TransformERs


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
* `data-annotation`: Annotation Methodology


## Evaluation
* `eval-human`: Human Evaluation
* `eval-metric-rouge`: ROUGE
* `eval-metric-bertscore`: BERTScore
* `eval-aspect-coherence`: Coherence
* `eval-aspect-redundancy`: Redundancy of Summary 
* `eval-aspect-factuality`: Factuality
* `eval-aspect-abstractness`: Abstractness
* `eval-referenceQuality`: Reference Quality
* `eval-metric-learnable`: Metrics are Learnable
* `eval-optimize-humanJudgement`: Optimization towards human judgement
* `eval-reference-less`: Reference-less Approach to Automatic Evaluation
* `eval-metric-unsupervised`: Unsupervised Automatic Evaluation

## Survey
* `survey-2020`: A survey paper in 2020