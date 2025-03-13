#!/usr/bin/env python3
import os

import aws_cdk as cdk

from infra.infra_stack import Ec2BookingStack

app = cdk.App()

# Specify the environment (account and region)
env = cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'),
    region=os.getenv('CDK_DEFAULT_REGION'))

Ec2BookingStack(app,
    "Ec2-Booking-Management-Stack",
    env=env,
    description="Stack for deploying Ec2 Instance"
)

app.synth()