## Lab 09c - Implement Azure Kubernetes Service <br /> Student lab manual

### Lab scenario  
Contoso has a number of multi-tier applications that are not suitable to run by using Azure Container Instances. In order to determine whether they can be run as containerized workloads, you want to evaluate using Kubernetes as the container orchestrator. To further minimize management overhead, you want to test Azure Kubernetes Service, including its simplified deployment experience and scaling capabilities.

### Objectives  
In this lab, you will:
* Task 1: Register the Microsoft.Kubernetes and Microsoft.KubernetesConfiguration resource providers  
* Task 2: Deploy an Azure Kubernetes Service cluster  
* Task 3: Deploy pods into the Azure Kubernetes Service cluster  
* Task 4: Scale containerized workloads in the Azure Kubernetes service cluster  
* [Detailed explanation and actions required for each step](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_09c-Implement_Azure_Kubernetes_Service.html)  

#### Task 4: Scale containerized workloads in the Azure Kubernetes service cluster  
In this task, you will scale horizontally the number of pods and then number of cluster nodes.

1. From the Cloud Shell pane, and run the following to scale the deployment by increasing of the number of pods to 2:  
    
    ```shell
    kubectl scale --replicas=2 deployment/nginx-deployment
    ```  

    ![step1](./assets/t4_s1.png)

2. From the Cloud Shell pane, run the following to verify the outcome of scaling the deployment:  
    
    ```shell
    kubectl get pods
    ```  

    ![step2](./assets/t4_s2.png)  

3. From the Cloud Shell pane, run the following to scale out the cluster by increasing the number of nodes to 2:  
    
    ```shell
    RESOURCE_GROUP='az104-09c-rg1'

    AKS_CLUSTER='az104-9c-aks1'

    az aks scale --resource-group $RESOURCE_GROUP --name $AKS_CLUSTER --node-count 2
    ```  

    ![step3](./assets/t4_s3.png)  

4. From the Cloud Shell pane, run the following to verify the outcome of scaling the cluster:  
    
    ```shell
    kubectl get nodes
    ```  

    ![step4](./assets/t4_s4.png)  

5. From the Cloud Shell pane, run the following to scale the deployment:  
    
    ```shell
    kubectl scale --replicas=10 deployment/nginx-deployment
    ```  

    ![step5](./assets/t4_s5.png)  

6. From the Cloud Shell pane, run the following to verify the outcome of scaling the deployment:  
    
    ```shell
    kubectl get pods
    ```  

    ![step6](./assets/t4_s6.png)  

7. From the Cloud Shell pane, run the following to review the pods distribution across cluster nodes:  
    
    ```shell
    kubectl get pod -o=custom-columns=NODE:.spec.nodeName,POD:.metadata.name
    ```  

    ![step7](./assets/t4_s7.png)  

8. From the Cloud Shell pane, run the following to delete the deployment:  
    
    ```shell
    kubectl delete deployment nginx-deployment
    ```  

    ![step8](./assets/t4_s8.png)  
