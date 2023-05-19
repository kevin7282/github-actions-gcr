# Use Github Action workflow

## Table of contents

- [1. QuickStart](#1-quickstart)
- [2. Github Actons with GCR](#2-githubactons)
- [3. Docker](#3-docker)
- [4. Deploy apps with kubectl](#4-kubectl)
  - [4.1 Check Google Console](#41-gconsole)
- [5. Apps Up](#5-appsup)

## 1. QuickStart

```
https://github.com/kevin7282/github-actions-gcr

```

## 2. Github Actons with GCR

1. Create a new Google Cloud Project (or select an existing project) and enable the Container Registry and Kubernetes Engine APIs.
2. Create a new GKE cluster or select an existing GKE cluster.
3. Create or reuse a GitHub repository for the example workflow:
4. Create a repository.
5. Setup IAM roles to your service account:
6. Create a JSON service account key for the service account.
7. Add the following secrets to your repository's secrets:

GKE_PROJECT: Google Cloud project ID
GKE_SA_KEY: the content of the service account JSON file
Update .github/workflows/gke.yml to match the values corresponding to the VM

gcloud container clusters get-credentials gke-cluster1 —-region=us-central1 -—project=sincere-actor-377315
gcloud auth activate-service-account --key-file=D:\devops\sincere-actor-377315-c1f7b863241e.json

**TODO**: Make more features for Falsk website

## 3. Docker

Build image and run local:
```

docker image build -t nginx-deployment:1.1.0 .
docker container run -p 80:80 --rm nginx-deployment:1.1.0
docker stop $(docker ps -q)

```
Upload to GCR:
```
  docker tag nginx-deployment:blue nginx-deployment:1.1.0 gcr.io/sincere-actor-377315/nginx-deployment:1.1.0
  docker tag nginx-deployment:1.1.0 gcr.io/sincere-actor-377315/nginx-deployment:1.1.0
  docker push gcr.io/sincere-actor-377315/nginx-deployment:1.1.0

```
but as you are already here (github) you can try:

```
  docker image build -t nginx-deployment:1.1.1 .
  docker tag nginx-deployment:1.1.1 gcr.io/sincere-actor-377315/nginx-deployment:1.1.1
  docker push gcr.io/sincere-actor-377315/nginx-deployment:1.1.1
```

## 4. Deploy apps with kubectl

1. Clone the repository
2. Go to dockers folder

```
kubectl apply -f blue.yaml
kubectl apply greenserice.yaml
```

### 4.1 Check Google Console

- Deployment and service should be available
```
https://console.cloud.google.com/kubernetes/workload/overview?project=sincere-actor-377315
```

gcr.io reposity:

```
https://console.cloud.google.com/artifacts/docker/sincere-actor-377315/us/gcr.io/nginx-deployment?project=sincere-actor-377315


```

**TODO** use the handler after install to run the application

### 5. Apps Up 
Kubernetes Engine > Services > External endpoints

```
https://console.cloud.google.com/kubernetes/service/us-central1/gke-cluster1/default/nginx-service/overview?project=sincere-actor-377315
```
