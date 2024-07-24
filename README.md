
Replace `pikachu` with any Pokemon name to fetch its data.

## Kubernetes Deployment

### Deployment Files

The Kubernetes deployment files are located in the `k8s` directory:

- `k8s/server-deployment.yaml`: Deployment configuration
- `k8s/server-service.yaml`: Service configuration
- `k8s/server-scaledobject.yaml`: KEDA ScaledObject configuration

### Deploying to Kubernetes

1. **Install KEDA:**

    ```bash
    helm repo add kedacore https://kedacore.github.io/charts
    helm repo update
    helm install keda kedacore/keda --namespace keda --create-namespace
    ```

2. **Apply the Kubernetes resources:**

    ```bash
    kubectl apply -f k8s/server-deployment.yaml
    kubectl apply -f k8s/server-service.yaml
    kubectl apply -f k8s/server-scaledobject.yaml
    ```

### Monitoring

To monitor the application, we use Prometheus and Grafana.

1. **Install Prometheus:**

    ```bash
    helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
    helm repo update
    helm install prometheus prometheus-community/prometheus --namespace monitoring
    ```

2. **Install Grafana:**

    ```bash
    helm repo add grafana https://grafana.github.io/helm-charts
    helm repo update
    helm install grafana grafana/grafana --namespace monitoring
    ```

3. **Access Grafana:**

    ```bash
    kubectl port-forward --namespace monitoring svc/grafana 3000:80
    ```

    Access Grafana at [http://localhost:3000](http://localhost:3000) using the default credentials.

### Setting Up Grafana Dashboards

Configure Grafana to use Prometheus as a data source and create dashboards to monitor:

- Number of API requests
- Query parameters passed to the Python app
- App's CPU load

## CI/CD Pipeline

The CI/CD pipeline is configured using GitHub Actions. It automates the build and deployment process.

### GitHub Actions Workflow

The workflow is defined in `.github/workflows/deploy.yaml`. It performs the following steps:

1. **Build the Docker image and push it to Docker Hub.**
2. **Deploy the application to the Kubernetes cluster.**

### Setting Up GitHub Secrets


Ensure the following secrets are set in your GitHub repository:

- `DOCKER_HUB_USERNAME`: Your Docker Hub username
- `DOCKER_HUB_PASSWORD`: Your Docker Hub password
- `KUBECONFIG`: The kubeconfig file content to connect to your Kubernetes cluster
## (Sally  please add the kube config variable by yourself :here is the commnad to get it :`cat ~/.kube/config`)
## Bonus

### KEDA ScaledObject

The `server-scaledobject.yaml` uses KEDA for scaling the application based on CPU utilization.

### CI/CD

Automated deployment workflow using GitHub Actions is provided to streamline the deployment process.

## Acknowledgements

- [PokeAPI](https://pokeapi.co/) for providing the Pokemon data.
- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [KEDA](https://keda.sh/) for event-driven autoscaling.
- [Prometheus](https://prometheus.io/) and [Grafana](https://grafana.com/) for monitoring.

---

This README file provides detailed instructions on setting up, deploying, and monitoring the Flask Pokemon App. If you have any questions or need further assistance, feel free to open an issue in the repository.
