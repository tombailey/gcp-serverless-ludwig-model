# gcp-serverless-ludwig-model

An example serverless ludwig ML model for determining which movie a particular excerpt is from.

## Training

* specify your data in data.csv
* change the example model ludwig definition in ludwig-model.yml
* ```ludwig experiment --data_csv data.csv --model_definition_file ludwig-model.yml```

If you change the ludwig model, you will need to update the python code to reflect your features and outputs.

## Deployment

Deploy to GCP with:

* Move your ludwig model to ./model
* Ignore irrelevant files using .gcloudignore (see below)
* ```gcloud config set project my-project```
* ```gcloud beta functions deploy predict --runtime python37 --memory=1024MB --trigger-http```

Due to GCP size limitations, you may need to remove or ignore unnecessary ludwig model files before deploying to GCP. You should only need to keep the following files:

- model_hyperparameters.json
- model_weights.data-00000-of-00001
- model_weights.index
- model_weights.meta
- train_set_metadata.json

## Credit

With thanks to Gilbert Tanner's post about [hosting a ludwig model using Flask](https://towardsdatascience.com/productionizing-your-machine-learning-model-221468b0726d).
