## Hyperparameter optimization
command:
```
export ATTEMPT=0 && nohup python run_scripts/train.py --config-file  configs_hyperparam/$ATTEMPT/strategy_qa/5_STAR_IR-ORA-D.jsonnet -s ./output_ir-ora-d_hyper$ATTEMPT -g "0" -w output_roberta-star/model.tar.gz > ./ir-ora-d_hyper$ATTEMPT.log 2>&1 &
```
| ATTEMPT | WD    | LR   | cut_frac  | Accuracy | Loss | Best epoch |
| ------- | ---   | ---- | --------- | -------- | ---- | ---------- |
| base    | 0.1   | 1e-5 | 0.06      | 0.668122270742358 | 0.923827588639181 | 3 |
| 1       | 0.05  | 1e-5 | 0.06      |  |  |
| 2       | 0.075 | 1e-5 | 0.06      |  |  |
| 3       | 0.1   | 2e-5 | 0.06      |  |  |
| 4       | 0.1   | 5e-6 | 0.06      | 0.6637554585152838 |  1.566425569042685 | 8 |
| 5       | 0.1   | 1e-6 | 0.06      |    |  |
| 6       | 0.1   | 1e-5 | 0.12      |  |  |
| 7       | 0.1   | 5e-6 | 0.12  |  |
| 8       | 0.075 | 5e-6 | 0.12  |  |
| 9       | 0.15  | 1e-5 | 0.12  |  |
| 10      | 0.2   | 1e-5 | 0.12  |  |


Changes:
 - 0,1,2: WD only
 - 3,4,5: LR only
 - 6: cut_frac
 - 7: LT + cut_frac
