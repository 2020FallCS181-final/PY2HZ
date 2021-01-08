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

    in this folder, use the following command to test/train
    ```
    bash trainpart2.sh              % train the 2nd part
    ```

    ```
    bash trainpart3.sh              % train the 3rd part
    ```

    ```
    python interpret.py             % test a single sentence
    ```

    ```
    python test.py                  % test a batch of sentence
    ```

* ***test_dataset***

    data used to test 

* ***train_dataset***

    data used to train

***

## Numerical Results

```{=latex}
    \begin{table}[H]\centering
        \begin{tabular}{ccccc}\toprule
        \multirow{2}{*}{\quad Stage\quad} & \multirow{2}{*}{\quad Acc Type\quad} & \multicolumn{3}{c}{Accuracy (\%)}                              \\ \cline{3-5} 
                        &   &\, 3-5 \,& \,6-8\, & $\,\ge$9\, \\ \hline

        \multirow{2}{*}{Seg} & W &  0.999   &  0.998   &  0.992   \\
                        & S &  0.995   &  0.980   &   0.935  \\ \hline
        \multirow{2}{*}{Tok} & W &  0.623   &  0.653   &  0.655   \\
                        & S &  0.265   &  0.140   &   0.060  \\ \hline
        \multirow{2}{*}{Trs} & W &  0.924 &  0.938  &  0.957   \\
                        & S &  0.770 &  0.700  &  0.655  \\ \bottomrule
        \end{tabular}
        \caption{Accuracy of single stage}
        \label{tab:my-table1}
    \end{table}
               
```







