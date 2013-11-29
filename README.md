## Python Django Example CRUD App for Deis

Usage:
There are 3 clickable icons at the bottom of the left-hand sidebar.
* The `+` sign adds a new empty entry, but you can only add one empty entry at a time.
* The `-` sign will delete the current entry
* The **disk** icon will update any changes to the current entry

Goals:
This app will adhere to the standards of the [Twelve-Factor](http://12factor.net/) app methodology.

The main aim of this app is to show potential PaaS users how to hook up a Django app to a 3rd-party database, such as [Amazon RDS](http://aws.amazon.com/rds/), then deploy it to a public cloud such as [Amazon EC2](http://aws.amazon.com/ec2/) using a PaaS, noteably [Deis](http://deis.io).

A future edition to this app will explore how to store static assets in [Amazon S3](http://aws.amazon.com/s3/).