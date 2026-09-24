helm repo add apache-airflow https://airflow.apache.org
helm repo update
kubectl create namespace airflow
helm install airflow apache-airflow/airflow --namespace airflow
kubectl port-forward svc/airflow-webserver 8086:8080 -n airflow

http://localhost:8086/