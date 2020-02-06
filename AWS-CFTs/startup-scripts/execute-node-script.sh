#!/bin/bash

# This script is for executing a node script

PACKAGE_ROOT=s3://s3-bucket/weekly-export

# Install node and npm
curl -sL https://rpm.nodesource.com/setup_11.x | sudo bash -
sudo yum install -y nodejs

# Copy over our package, install dependencies, and run the package
aws s3 cp --recursive $PACKAGE_ROOT node_package
cd node_package
npm install
npm start
