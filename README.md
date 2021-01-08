# AI Final - PY2HZ


## Datasets, References and Results record
### Record Document

> [Tencent Document](https://docs.qq.com/doc/DTEhqUHR1ck1Tak9s)

### Links

> [THUOCL](http://thuocl.thunlp.org) dataset

> [icwb](http://sighan.cs.uchicago.edu/bakeoff2005/) dataset

> [news and novel](https://github.com/letiantian/Pinyin2Hanzi/tree/master/train/hmm/article) dataset

> [我爱自然语言处理](https://www.52nlp.cn/itenyh%e7%89%88-%e7%94%a8hmm%e5%81%9a%e4%b8%ad%e6%96%87%e5%88%86%e8%af%8d%e5%9b%9b%ef%bc%9aa-pure-hmm-%e5%88%86%e8%af%8d%e5%99%a8) reference

> [HMM Framework](https://github.com/guyz/HMM/blob/d089cbe9dc99f7c2e279d82ea3840cf8d4a2f6a0/hmm/_BaseHMM.py#L13) reference

***
## Pre-requirement

Before test the project, use the following command to install the required python packages. Note that we are using python 3.7.0 and above.
```
pip3 install requirement.txt
```

***
## Code

* ***Part1***: segmentation, e.g.

    ```
    'woaibeijingtiananmen' --> ['wo', 'ai', 'bei', 'jing', 'tian', 'an','men']
    ```


* ***Part2***: tokenization, e.g.

    ```
    ['wo', 'ai', 'bei', 'jing', 'tian', 'an','men'] --> ['wo', 'ai', 'beijing', 'tiananmen']
    ```

* ***Part3***: translation, e.g.

    ```
    ['wo', 'ai', 'beijing', 'tiananmen'] --> ['我', '爱', '北京', '天安门']

    ```
* ***test***:
    in folder **part2**
    ```
    bash train.sh              % train the 2nd part
    
    ```
    in folder **part3**
    ```
    bash train.sh              % train the 3rd part

    ```
    in folder **combination**

    ```
    bash singlesentence.sh             
    
    % test a single sentence; alternatively, use

    python ./test/interpret.py

    ```
    in folder **combination**
    ```
    bash accuracytest.sh                
    
    % test a batch of sentence, to get the accuracy on words / sentences; note that this may cost long time, and some relative path problem may occur on different PCs, so if you need to run the accuracy test, please contact yuzy@shanghaitech.edu.cn. Alternatively, use the following code

    python ./test/test.py 
    ```

    for accuracy test of part1 and part3, please refer to branch 'zheng_dev' and 'main' respectively

* ***test_dataset***

    data used to test 

* ***train_dataset***

    data used to train

***

## Numerical Results
Through out the experiments, we have the following notations:

### Stage
> **Seg**: Segmentation, i.e. part 1

> **Tok**: Tokenaization, i.e. part 2

> **Trs**: Translation, i.e. part 3

### Acc Type
> **W**: accuracy per word, i.e. # of correct words / # of total words

> **S**: accuracy per sentence, i.e. # of correct sentences / # of total sentences

### Test data set:
> **3-5**: a sentence with 3-5 tokens

> **6-8**: a sentence with 3-5 tokens

> **>=9**: a sentence with >=9 tokens

### Result 

> **top1**: accuracy of the highest scored sentence

> **top3**: accuracy of top 3 highest scored sentences

> **top5**: accuracy of top 5 highest scored sentences

| Stage |  Acc Type | Accuracy (\%) |         |            |
|:----------------:|:-------------------:|:-------------:|:-------:|:----------:|
|                  |                     |    3-5    | 6-8 | >= 9 |
|        Seg       |          W          |     0.999     |  0.998  |    0.992   |
|                  |          S          |     0.995     |  0.980  |    0.935   |
|        Tok       |          W          |     0.623     |  0.653  |    0.655   |
|                  |          S          |     0.265     |  0.140  |    0.060   |
|        Trs       |          W          |     0.924     |  0.938  |    0.957   |
|                  |          S          |     0.770     |  0.700  |    0.655   |


| Stages |  Acc Type | Accuracy (\%) |          |              |
|:-----------------:|:-------------------:|:-------------:|:--------:|:------------:|
|                   |                     |    3-5    |  6-8 | >=9   |
|    Seg+Tok+Trs    |          W          |     0.782     |   0.827  |     0.824    |
|                   |          S          |     0.310     |   0.230  |     0.085    |
|      Seg+Trs      |          W          |     0.786     |   0.793  |     0.801    |
|                   |          S          |     0.365     |   0.220  |     0.095    |

|  Stages | Acc Type | Accuracy (\%) |          |              |
|:-----------------:|:-------------------:|:-------------:|:--------:|:------------:|
|                   |                     |    3-5    | 6-8 | >= 9   |
|    Seg+Tok+Trs    |          W          |     0.782     |   0.827  |     0.824    |
|                   |          S          |     0.310     |   0.230  |     0.085    |
|      Seg+Trs      |          W          |     0.786     |   0.793  |     0.801    |
|                   |          S          |     0.365     |   0.220  |     0.095    |

| Number of tokens | Accuracy Type |   Accuracy (\%)   |                   |                   |
|:---------------------------:|:------------------------:|:-----------------:|:-----------------:|:-----------------:|
|                             |                          | Top1 | Top3 | Top5 |
|             3-5             |             W            |       0.782       |       0.826       |       0.837       |
|                             |             S            |       0.310       |       0.375       |       0.395       |
|             6-8             |             W            |       0.827       |       0.855       |       0.863       |
|                             |             S            |       0.230       |       0.285       |       0.295       |
|            >=9           |             W            |       0.824       |       0.854       |       0.864       |
|                             |             S            |       0.085       |       0.115       |       0.135       |




