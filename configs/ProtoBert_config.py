import task_def
##### configs for protobert


config_bert_2_way = {
	"project_name"		:	"ProtoBert_2_way_5_shot",
	"bert_model"        :   "bert-base-uncased",
	"model"             :   "ProtoBert",
	"dataloader"        :   "FewShotDataset_per_doc",
	"Labels"            :   ["ANALYSIS","FAC"],
	'num_class'         :   2,
	'max_sent'          :   5,
	'min_sent'          :   1,
	'max_epochs'        :   1,
	"lr"                :   1e-02,
	"lr_epoch_decay"    :   0.9,
	"batch_size"        :   32,
	"max_seq_length"    :   128,
	"max_epochs"        :   20,
	"early_stopping"    :   5,
	"dot"               :   False,
	"dropout"           :   True,
	"train_dataset"     :   'datasets/kalamkar/inter/train_format.txt',
	"val_dataset"       :   'datasets/kalamkar/inter/dev_format.txt',
	"batch_size"        :   1,
	"num_warmup_steps"	: 	30,
	"num_training_steps":	30000,
	"token_padding"		:	128,
	"grad_iter"			:	1
}

config_bert_4_way = {
	"project_name"		:	"ProtoBert_4_way_5_shot",
	"bert_model"        :   "bert-base-uncased",
	"model"             :   "ProtoBert",
	"dataloader"        :   "FewShotDataset_per_doc",
	"Labels"            :   ["ANALYSIS","FAC","PREAMBLE","PRE_RELIED"],
	'num_class'         :   4,
	'max_sent'          :   5,
	'min_sent'          :   1,
	'max_epochs'        :   1,
	"lr"                :   3e-05,
	"lr_epoch_decay"    :   0.9,
	"batch_size"        :   32,
	"max_seq_length"    :   128,
	"max_epochs"        :   20,
	"early_stopping"    :   5,
	"dot"               :   False,
	"dropout"           :   True,
	"train_dataset"     :   'datasets/kalamkar/inter/train_format.txt',
	"val_dataset"       :   'datasets/kalamkar/inter/dev_format.txt',
	"batch_size"        :   1,
	"num_warmup_steps"	: 	30,
	"num_training_steps":	30000,
	"token_padding"		:	128,
	"grad_iter"			:	1
}

config_bert_6_way = {
	"project_name"		:	"ProtoBert_6_way_5_shot",
	"bert_model"        :   "bert-base-uncased",
	"model"             :   "ProtoBert",
	"dataloader"        :   "FewShotDataset_per_doc",
	"Labels"            :   ["ANALYSIS","FAC","PREAMBLE","PRE_RELIED","ARG_PETITIONER","RPC"],
	'num_class'         :   6,
	'max_sent'          :   5,
	'min_sent'          :   1,
	'max_epochs'        :   1,
	"lr"                :   1e-1,
	"lr_epoch_decay"    :   0.9,
	"batch_size"        :   32,
	"max_seq_length"    :   128,
	"max_epochs"        :   20,
	"early_stopping"    :   5,
	"dot"               :   False,
	"dropout"           :   True,
	"train_dataset"     :   'datasets/kalamkar/inter/train_format.txt',
	"val_dataset"       :   'datasets/kalamkar/inter/dev_format.txt',
	"batch_size"        :   1,
	"num_warmup_steps"	: 	30,
	"num_training_steps":	30000,
	"token_padding"		:	128,
	"grad_iter"			:	1
}


config_bert_12_way = {
	"project_name"		:	"ProtoBert_12_way_5_shot",
	"bert_model"        :   "bert-base-uncased",
	"model"             :   "ProtoBert",
	"dataloader"        :   "FewShotDataset_per_doc",
	"Labels"            :   task_def.KALAMKAR_LABELS,
	'num_class'         :   12,
	'max_sent'          :   5,
	'min_sent'          :   1,
	'max_epochs'        :   1,
	"lr"                :   3e-05,
	"lr_epoch_decay"    :   0.9,
	"batch_size"        :   32,
	"max_seq_length"    :   128,
	"max_epochs"        :   20,
	"early_stopping"    :   5,
	"dot"               :   False,
	"dropout"           :   True,
	"train_dataset"     :   'datasets/kalamkar/inter/train_format.txt',
	"val_dataset"       :   'datasets/kalamkar/inter/dev_format.txt',
	"batch_size"        :   1,
	"num_warmup_steps"	: 	30,
	"num_training_steps":	30000,
	"token_padding"		:	128,
	"grad_iter"			:	1
}



#####################################################
#####################################################
#####################################################
#####################################################



config_bert_hier_12_way = {
	"project_name"		:	"ProtoBert_12_way_5_shot",
	"bert_model"        :   "bert-base-uncased",
	"model"             :   "ProtoBert_hier",
	"dataloader"        :   "FewShotDataset_per_doc",
	"Labels"            :   task_def.KALAMKAR_LABELS,
	'num_class'         :   12,
	'max_sent'          :   5,
	'min_sent'          :   1,
	'max_epochs'        :   1,
	"max_seq_length"    :   128,
	"max_epochs"        :   20,
	"early_stopping"    :   5,
	"dot"               :   False,
	"dropout"           :   True,
	"train_dataset"     :   'datasets/kalamkar/inter/train_format.txt',
	"val_dataset"       :   'datasets/kalamkar/inter/dev_format.txt',
	"batch_size"		:  	1,
	"num_warmup_steps"	: 	30,
	"num_training_steps":	30000,
	"token_padding"		:	128,
	"grad_iter"			:	1,
	"MAX_DOCS" 			:	-1,

	"bert_trainable"	:	True,
	"cacheable_tasks"	:	[],

	"dropout"			:	0.5,
	"word_lstm_hs"		:	758,
	"att_pooling_dim_ctx":	200,
	"att_pooling_num_ctx":	15,

	"lr"				:	3e-05,
	"lr_epoch_decay"	:	0.9,
	"max_seq_length"	:	128,
	"max_epochs"		:	20
}