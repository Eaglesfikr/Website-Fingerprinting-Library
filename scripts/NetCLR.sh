dataset=DF18

python -u exp/pre_train.py \
  --dataset ${dataset} \
  --model NetCLR \
  --device cuda:6 \
  --feature DIR \
  --seq_len 5000 \
  --train_epochs 30 \
  --batch_size 256 \
  --learning_rate 3e-4 \
  --optimizer Adam \
  --eval_metrics Accuracy Precision Recall F1-score \
  --save_metric Accuracy \
  --save_name max_f1

python -u exp/train.py \
  --dataset ${dataset} \
  --model NetCLR \
  --device cuda:6 \
  --feature DIR \
  --seq_len 5000 \
  --train_epochs 30 \
  --batch_size 256 \
  --learning_rate 3e-4 \
  --optimizer Adam \
  --eval_metrics Accuracy Precision Recall F1-score \
  --save_metric Accuracy \
  --save_name max_f1

python -u exp/test.py \
  --dataset ${dataset} \
  --model NetCLR \
  --device cuda:6 \
  --feature DIR \
  --seq_len 5000 \
  --batch_size 256 \
  --eval_metrics Accuracy Precision Recall F1-score P@min \
  --save_name max_f1