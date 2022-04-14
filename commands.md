```nohup python run_scripts/train_RoBERTa_STAR.py -s ./output_roberta-star -g "0" > ./roberta-star_0.log 2>&1 &```

```tail -f ./roberta-star_0.log```


```nohup python run_scripts/train.py --config-file  configs/strategy_qa/5_STAR_IR-ORA-D.jsonnet -s ./output_ir-ora-d_hyper0 -g "0" -w downloaded/2_boolq_github.tar.gz > ./ir-ora-d_0.log 2>&1 &```

```tail -f ./ir-ora-d_0.log```

modified down here
```nohup python run_scripts/train.py --config-file  configs/strategy_qa/5_STAR_IR-ORA-D.jsonnet -s ./output_ir-ora-d -g "0" -w output_roberta-star/model.tar.gz > ./ir-ora-d_0.log 2>&1 &```


BART Decomposition model
```
nohup python run_scripts/train.py --config-file configs/decomposition/bart_decomp_strategy_qa.jsonnet -s ./output_decomposition -g "0" > ./bart_decomposition_0.log 2>&1 &
```

```tail -f ./bart_decomposition_0.log```


To generate decompositions

```
python run_scripts/predict.py --model output_decomposition/model.tar.gz --data data/strategyqa/dev.json -g "0" --output-file data/strategyqa/generated/bart_decomp_dev_predictions.jsonl
```

TO generate testable with decompositions 5-ir-ora-d convert to 4-ir-d

```
python tools/tar_to_tar.py output_ir-ora-d/model.tar.gz configs/4_STAR_IR-D.jsonnet 4_STAR_IR-D.tar.gz
```

TO calculate accuracy
```
python run_scripts/evaluate.py --model 4_STAR_IR-D.tar.gz --data data/strategyqa/dev.json -g "0" > ./accuracy_4_STAR_IR-D_0.log 2>&1 &
```

```tail -f ./accuracy_4_STAR_IR-D_0.log```


For predictions
```
python run_scripts/predict.py --model ./output_ir-ora-d/model.tar.gz --data data/strategyqa/dev.json -g "0" --output-file pred_ir-ora-d_0.jsonl

--IGNORE
python run_scripts/predict.py --model ./output_ir-ora-d/model.tar.gz --data data/strategyqa/dev.json -g "0" --output-file pred_ir-ora-d_0_test.jsonl
```

For Recall
```
python ir_evaluation/get_paragraphs_by_config.py --config-file configs/strategy_qa/5_STAR_IR-ORA-D.jsonnet --output-file ./recall-support/recall_5_STAR_IR-ORA-D_0 --data data/strategyqa/dev.json

```

STEP2
```
python ir_evaluation/recall@10.py --data data/strategyqa/dev.json --retrieved-paragraphs ./recall-support/recall_5_STAR_IR-ORA-D_0

```
