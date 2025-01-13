# Byte Pair Encoding for Kannada Text

## Overview
This project implements Byte Pair Encoding (BPE) for text processing, specifically tailored for Kannada language text. BPE is a simple and effective data compression technique that can also be used for subword tokenization in natural language processing (NLP) tasks.

## What is Byte Pair Encoding?
Byte Pair Encoding is a form of data compression that iteratively replaces the most frequent pair of bytes in a sequence with a single, unused byte. This process continues until a specified number of pairs have been replaced or no more pairs can be found. 
In the context of NLP, BPE is used for tokenization, which helps in handling out-of-vocabulary words by breaking them down into smaller, more manageable subword units. This is particularly useful for languages with rich morphology, such as Kannada, where words can have many forms.

#### Dataset: https://www.kaggle.com/datasets/disisbig/kannada-wikipedia-articles/data

## Train logs
```
Loading files: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2706/2706 [00:02<00:00, 1155.16it/s]
Loaded 2,565 files
Total text length: 9,009,546 characters

Training BPE encoder...
Encoding byte pairs:  14%|██████████████████████████████▌                                                                                                                                                                                         | 496/3500 [12:59<5:34:19,  6.68s/it]
Iteration 100
Current vocabulary size: 496
Current data size: 5,559,825
Current compression ratio: 1.62
--------------------------------------------------------------------------------
Encoding byte pairs:  17%|████████████████████████████████████▊                                                                                                                                                                                   | 596/3500 [23:35<4:46:16,  5.91s/it]
Iteration 200
Current vocabulary size: 596
Current data size: 4,892,953
Current compression ratio: 1.84
--------------------------------------------------------------------------------
Encoding byte pairs:  20%|██████████████████████████████████████████▉                                                                                                                                                                             | 696/3500 [33:13<4:32:59,  5.84s/it]
Iteration 300
Current vocabulary size: 696
Current data size: 4,533,221
Current compression ratio: 1.99
--------------------------------------------------------------------------------
Encoding byte pairs:  23%|█████████████████████████████████████████████████                                                                                                                                                                       | 796/3500 [42:17<4:17:56,  5.72s/it]
Iteration 400
Current vocabulary size: 796
Current data size: 4,279,612
Current compression ratio: 2.11
--------------------------------------------------------------------------------
Encoding byte pairs:  26%|███████████████████████████████████████████████████████▎                                                                                                                                                                | 896/3500 [51:00<3:44:16,  5.17s/it]
Iteration 500
Current vocabulary size: 896
Current data size: 4,083,173
Current compression ratio: 2.21
--------------------------------------------------------------------------------
Encoding byte pairs:  28%|████████████████████████████████████████████████████████████▉                                                                                                                                                         | 996/3500 [1:00:13<3:24:04,  4.89s/it]
Iteration 600
Current vocabulary size: 996
Current data size: 3,927,914
Current compression ratio: 2.29
--------------------------------------------------------------------------------
Encoding byte pairs:  31%|██████████████████████████████████████████████████████████████████▋                                                                                                                                                  | 1096/3500 [1:08:26<3:16:16,  4.90s/it]
Iteration 700
Current vocabulary size: 1,096
Current data size: 3,799,892
Current compression ratio: 2.37
--------------------------------------------------------------------------------
Encoding byte pairs:  34%|████████████████████████████████████████████████████████████████████████▊                                                                                                                                            | 1196/3500 [1:16:17<2:59:51,  4.68s/it]
Iteration 800
Current vocabulary size: 1,196
Current data size: 3,691,514
Current compression ratio: 2.44
--------------------------------------------------------------------------------
Encoding byte pairs:  37%|██████████████████████████████████████████████████████████████████████████████▊                                                                                                                                      | 1296/3500 [1:24:17<3:02:27,  4.97s/it]
Iteration 900
Current vocabulary size: 1,296
Current data size: 3,598,570
Current compression ratio: 2.50
--------------------------------------------------------------------------------
Encoding byte pairs:  40%|████████████████████████████████████████████████████████████████████████████████████▉                                                                                                                                | 1396/3500 [1:32:10<2:56:04,  5.02s/it]
Iteration 1,000
Current vocabulary size: 1,396
Current data size: 3,515,731
Current compression ratio: 2.56
--------------------------------------------------------------------------------
Encoding byte pairs:  43%|███████████████████████████████████████████████████████████████████████████████████████████                                                                                                                          | 1496/3500 [1:39:18<2:14:46,  4.04s/it]
Iteration 1,100
Current vocabulary size: 1,496
Current data size: 3,442,339
Current compression ratio: 2.62
--------------------------------------------------------------------------------
Encoding byte pairs:  46%|█████████████████████████████████████████████████████████████████████████████████████████████████▏                                                                                                                   | 1596/3500 [1:46:07<2:07:41,  4.02s/it]
Iteration 1,200
Current vocabulary size: 1,596
Current data size: 3,376,627
Current compression ratio: 2.67
--------------------------------------------------------------------------------
Encoding byte pairs:  48%|███████████████████████████████████████████████████████████████████████████████████████████████████████▏                                                                                                             | 1696/3500 [1:52:56<1:59:18,  3.97s/it]
Iteration 1,300
Current vocabulary size: 1,696
Current data size: 3,317,516
Current compression ratio: 2.72
--------------------------------------------------------------------------------
Encoding byte pairs:  51%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████▎                                                                                                       | 1796/3500 [1:59:34<1:50:55,  3.91s/it]
Iteration 1,400
Current vocabulary size: 1,796
Current data size: 3,263,502
Current compression ratio: 2.76
--------------------------------------------------------------------------------
Encoding byte pairs:  54%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████▊                                                                                                 | 1896/3500 [10:05:20<1:40:29,  3.76s/it]
Iteration 1,500
Current vocabulary size: 1,896
Current data size: 3,214,057
Current compression ratio: 2.80
--------------------------------------------------------------------------------
Encoding byte pairs:  57%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▉                                                                                           | 1996/3500 [10:12:07<1:38:13,  3.92s/it]
Iteration 1,600
Current vocabulary size: 1,996
Current data size: 3,168,521
Current compression ratio: 2.84
--------------------------------------------------------------------------------
Encoding byte pairs:  60%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▉                                                                                     | 2096/3500 [10:18:29<1:40:10,  4.28s/it]
Iteration 1,700
Current vocabulary size: 2,096
Current data size: 3,126,381
Current compression ratio: 2.88
--------------------------------------------------------------------------------
Encoding byte pairs:  63%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████                                                                               | 2196/3500 [10:24:48<1:21:38,  3.76s/it]
Iteration 1,800
Current vocabulary size: 2,196
Current data size: 3,087,141
Current compression ratio: 2.92
--------------------------------------------------------------------------------
Encoding byte pairs:  66%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████                                                                         | 2296/3500 [10:31:12<1:16:14,  3.80s/it]
Iteration 1,900
Current vocabulary size: 2,296
Current data size: 3,050,290
Current compression ratio: 2.95
--------------------------------------------------------------------------------
Encoding byte pairs:  68%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▏                                                                  | 2396/3500 [10:37:32<1:08:06,  3.70s/it]
Iteration 2,000
Current vocabulary size: 2,396
Current data size: 3,015,531
Current compression ratio: 2.99
--------------------------------------------------------------------------------
Encoding byte pairs:  71%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▏                                                            | 2496/3500 [10:43:38<1:02:38,  3.74s/it]
Iteration 2,100
Current vocabulary size: 2,496
Current data size: 2,983,036
Current compression ratio: 3.02
--------------------------------------------------------------------------------
Encoding byte pairs:  74%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▋                                                       | 2596/3500 [10:50:34<54:31,  3.62s/it]
Iteration 2,200
Current vocabulary size: 2,596
Current data size: 2,952,262
Current compression ratio: 3.05
--------------------------------------------------------------------------------
Encoding byte pairs:  77%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▊                                                 | 2696/3500 [10:56:45<57:09,  4.27s/it]
Iteration 2,300
Current vocabulary size: 2,696
Current data size: 2,922,821
Current compression ratio: 3.08
--------------------------------------------------------------------------------
Encoding byte pairs:  80%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▉                                           | 2796/3500 [11:02:56<42:46,  3.65s/it]
Iteration 2,400
Current vocabulary size: 2,796
Current data size: 2,894,951
Current compression ratio: 3.11
--------------------------------------------------------------------------------
Encoding byte pairs:  83%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████                                     | 2896/3500 [11:08:54<36:04,  3.58s/it]
Iteration 2,500
Current vocabulary size: 2,896
Current data size: 2,868,689
Current compression ratio: 3.14
--------------------------------------------------------------------------------
Encoding byte pairs:  86%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▏                              | 2996/3500 [11:14:52<35:33,  4.23s/it]
Iteration 2,600
Current vocabulary size: 2,996
Current data size: 2,843,597
Current compression ratio: 3.17
--------------------------------------------------------------------------------
Encoding byte pairs:  88%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▎                        | 3096/3500 [11:21:04<23:52,  3.54s/it]
Iteration 2,700
Current vocabulary size: 3,096
Current data size: 2,819,500
Current compression ratio: 3.20
--------------------------------------------------------------------------------
Encoding byte pairs:  91%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▍                  | 3196/3500 [11:26:58<17:47,  3.51s/it]
Iteration 2,800
Current vocabulary size: 3,196
Current data size: 2,796,453
Current compression ratio: 3.22
--------------------------------------------------------------------------------
Encoding byte pairs:  94%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▌            | 3296/3500 [11:32:56<11:49,  3.48s/it]
Iteration 2,900
Current vocabulary size: 3,296
Current data size: 2,774,484
Current compression ratio: 3.25
--------------------------------------------------------------------------------
Encoding byte pairs:  97%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▋      | 3396/3500 [11:39:10<06:46,  3.91s/it]
Iteration 3,000
Current vocabulary size: 3,396
Current data size: 2,753,423
Current compression ratio: 3.27
--------------------------------------------------------------------------------
Encoding byte pairs: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▊| 3496/3500 [11:45:13<00:13,  3.46s/it]
Iteration 3,100
Current vocabulary size: 3,496
Current data size: 2,733,183
Current compression ratio: 3.30
--------------------------------------------------------------------------------
Encoding byte pairs: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3500/3500 [11:45:27<00:00, 13.64s/it]

Training completed after 3,104 iterations
Final vocabulary size: 3,500

Saving encoder...
Encoder saved to ./encoding/kannada_tokenizer.json
```

##### Huggingface Space: https://huggingface.co/spaces/jasonjoshi/KannadaBPE

## Conclusion
Byte Pair Encoding is a powerful technique for text processing in NLP, especially for languages with complex word structures like Kannada. This implementation provides a straightforward way to train a BPE model, enabling better handling of text data for various applications.