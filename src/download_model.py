import os
import argparse

import wandb

from src.utils import BASE_DIR

parser = argparse.ArgumentParser()
parser.add_argument('wandb_key')
args = parser.parse_args()
wandb.login(key=args.wandb_key)
artifact = wandb.Api().artifact(
    f"model-registry/capitalbikeshare-dv-model-pipeline:{os.getenv('ENVIRONMENT', 'staging')}",
    type="model",
)

artifact.download(root=BASE_DIR)
