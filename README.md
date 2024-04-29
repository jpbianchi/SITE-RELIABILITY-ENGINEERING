# Kubernetes monitoring with Prometheus and Grafana

This repo shows how to manage alerts from a simple website deployed in a container with Kubernetes.  
Everything is running locally on macOS.

Some setup files are missing because they hold secrets (to be implemented later using Kubernetes secrets).  

Deployment_local_image.yml uses a container created directly inside Kubernetes rather than from dockerhub. 

See the file `allcommands.md` for the followed procedure to set it all up and comments.  

A series of alerts are declared in prometheus.yml.  
The alerts.yml files are not shown since they contain secrets. 

The state of Kubernetes was monitored using k9s.

<p align="left">
  <img src="images/k9s_terminal.png"  width="700px" />
</p>

## LowMemory alert
The memory provided is too low which triggers the `LowMemory` alert 

Here's a screenshot taken from the Prometheus server running locally on `localhost:9090`
The AlertManager runs on `localhost:9093`

<p align="left">
  <img src="images/lowmemory.png" width="700px" />
</p>

The AlertManager sends a message to Slack every 2 minutes.

<p align="left">
  <img src="images/slack_alert.png"  width="700px" />
</p>

## KubePodNotReady alert
If we increase 'cpu' in deployment to 10, Prometheus triggers a `KubePodNotReady` alert.

<p align="left">
  <img src="images/kubepodnotready.png"  width="700px" />
</p>

'cpu' was set back to 1 to be able to continue.  

