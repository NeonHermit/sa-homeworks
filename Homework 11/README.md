## Homework 11 - Lab 06 - Implement Traffic Management  

<br />

### Lab scenario  
You were tasked with testing managing network traffic targeting Azure virtual machines in the hub and spoke network topology, which Contoso considers implementing in its Azure environment (instead of creating the mesh topology, which you tested in the previous lab). This testing needs to include implementing connectivity between spokes by relying on user defined routes that force traffic to flow via the hub, as well as traffic distribution across virtual machines by using layer 4 and layer 7 load balancers. For this purpose, you intend to use Azure Load Balancer (layer 4) and Azure Application Gateway (layer 7).

### Objectives 
In this lab, you will:

* Task 1: Provision the lab environment  
* Task 2: Configure the hub and spoke network topology  
* Task 3: Test transitivity of virtual network peering  
* Task 4: Configure routing in the hub and spoke topology  
* Task 5: Implement Azure Load Balancer  
* Task 6: Implement Azure Application Gateway  

### Review
In this lab, you have:

1. Provisioned the lab environment:  
    * Created a virtual network with subnets
    * Created virtual machines in each subnet
    
2. Configured the hub and spoke network topology:  
    * Create a central hub network and spoke networks that are connected to it  
    * Configured the subnets in each spoke network to use the hub network as the default route
    
3. Tested transitivity of virtual network peering   
    * Created virtual network peering connections between the hub network and spoke networks
    * Tested if the traffic can flow between them through the hub  
    
4. Configure routing in the hub and spoke topology  
    * Created user defined routes that tell traffic how to get from one subnet to another 
    * Ensured that traffic between spokes is forced to flow through the hub network 
    
5. Implemented Azure Load Balancer    
    * Configured the (layer 4) load balancer to distribute traffic across virtual machines in different subnets  
    
6. Implemented Azure Application Gateway  
    * Configured the gateway to manage traffic based on the content of the traffic
