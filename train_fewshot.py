import numpy as np
import os
import getopt
import sys
# If it causes an error you can change it
sys.path.insert(1,'configs')
sys.path.insert(0,'models')

import wandb
import torch
from torch import cuda
from sklearn.metrics import f1_score
from statistics import mean
from visualization import plots

def validate(config, model,validation_dataloader):

	for support_batch,query_batch,every_class_present in validation_dataloader:
		if every_class_present:
			logits,pred = model.forward(support_batch,query_batch)


def train(config, model,optimizer_func,scheduler,train_dataloader,validation_dataloader):
	metrics = {}
	wandb.init(project=config["project_name"])
	
	print (model)

	curr_iter = 0
	curr_train_loss = 0.0
	best_f1 = 0.0

	f1_scores = []
	losses = []
	accuracies = []

	for curr_epoch in range(0,config["max_epochs"]):
		print ("Epoch number : ",(curr_epoch+1))

		prediction = []
		ground_truth = []
		loss_per_batch = []
		accuracy_per_batch = []

		for support_batch,query_batch,every_class_present in train_dataloader:      
			if every_class_present:
				# training dataloader
				curr_iter += 1

				model.train()
				pred,logits = model.forward(support_batch,query_batch)
				ylabel      = model.onehot_encoder(query_batch["label_ids"])
				#print ("logits : ",logits)
				#print ("ylabel : ",ylabel)
				#print ("pred :",pred)
				loss = model.custom_loss(logits,ylabel.long()) / config["grad_iter"]
				loss.backward()

				mask = pred.long() == ylabel.long()
				accuracy = (torch.sum(mask) *100)/ len(pred)

				prediction.append(pred.data)
				ground_truth.append(ylabel.data)
				loss_per_batch.append(loss.item())
				accuracy_per_batch.append(accuracy.item())
				wandb.log({"loss": loss,'accuracy':accuracy})


				if curr_iter % config["grad_iter"] == 0:
					optimizer_func.step()
					scheduler.step()
					optimizer_func.zero_grad()
					#validation(config,model,validation_dataloader) 

		prediction = np.concatenate(prediction)
		ground_truth = np.concatenate(ground_truth)
		f1 = f1_score(prediction, ground_truth)
		print("F1 Score for epoch ", curr_epoch+1, ": ", f1)
		f1_scores.append(f1)
		losses.append(mean(loss_per_batch))
		accuracies.append(mean(accuracy_per_batch))
	print("F1 Scores: ", f1_scores)
	print("Losses: ", losses)
	print("Accuracies: ", accuracies)
	plots.plot_f1_score(f1_scores, config["max_epochs"])
	plots.plot_acc_loss(accuracies, losses, config["max_epochs"])
	
def train_standard(config,model,dataloader_fold,optimizer,epoch_scheduler):
	metrics = []




	for curr_epoch in range(0,config["max_epochs"]):
		print("Epoch number : ",(curr_epoch+1))
		for fold_num, fold in enumerate(dataloader_fold.get_folds()):
			# we use folds for pubmet(pubmed is a bit larger so we need this workaround)
			

			train_batches,train_dev = fold.train, fold.dev

			model.train()
			for batch_num, batch in enumerate(train_batches):

				output = model.forward(batch)
				




	return metrics,model



	print ("Finished training model.....")
	return model,metrics

