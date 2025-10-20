#!/bin/bash

dataset=CW

for percent in {20..100..10}
do
    echo "==== Running test for ${percent}% traffic ===="
    
    python -u exp/dataset_process/gen_tam.py \
        --dataset ${dataset} \
        --seq_len 10000 \
        --in_file test_p${percent}
    
    python -u exp/test.py \
        --dataset ${dataset} \
        --model RF \
        --device cuda:0 \
        --test_file tam_test_p${percent} \
        --feature TAM \
        --seq_len 2000 \
        --batch_size 256 \
        --eval_metrics Accuracy Precision Recall F1-score \
        --load_name max_f1 \
        --result_file test_p${percent}
done
