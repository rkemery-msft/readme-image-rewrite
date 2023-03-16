# Step-by-Step AKS Workflow - EKS to AKS Considerations
#### [Made by Rick Kemery with Scribe](https://scribehow.com/shared/Step-by-Step_AKS_Workflow_-_EKS_to_AKS_Considerations__O2mSEOO4Q0mPy_VWTijcBw)
Create an AKS cluster in Azure and learn more about the workflow from start to finish - along with considerations when migrating from EKS workloads to AKS!

**1. Navigate to https://portal.azure.com/#home**

**2. Click the "Search resources, services, and docs (G+/)" field.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/01_ascreenshot.jpeg)

**3. Type "aks"**

**4. Click "Kubernetes services"**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/02_ascreenshot.jpeg)

**5. Click this icon to begin creating a Kubernetes service deployment.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/03_ascreenshot.jpeg)

**6. Click "Create a Kubernetes cluster" to begin the workflow.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/04_ascreenshot.jpeg)

**7. Click "(New) Resource group" for the AKS deployment; both AWS and Azure have the concept of Resource Groups; some key items are that one Azure resource is always associated with one resource group and it can be organized via tags. You can also manage them with the Web Interface (Azure Portal), REST API, Command Line, PowerShell, or ARM Templates.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/05_user_cropped_screenshot.jpeg)

**8. I have an example Resource Group created named "rk-aks-demo" that I will use.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/06_user_cropped_screenshot.jpeg)

**9. For demo purposes, we will use the "Dev/Test" Cluster preset configuration. One advantage in this workflow compared to AWS is that we offer several presets. These are 5 levels of presets that offer different advantages for cost and features/workloads that can get you started quick.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/07_user_cropped_screenshot.jpeg)

**10. For demo purposes and Dev/Test environment, click "Best for experimenting with AKS or deploying a test app." Dev/Test will set system node pool size to B4ms shape with Cluster Autoscaling and 99.5% API server availability.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/08_user_cropped_screenshot.jpeg)

**11. Create a name for your cluster - click the "Kubernetes cluster name" field and enter it.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/09_user_cropped_screenshot.jpeg)

**12. Since am I close to the Central US Azure datacenter, I chose it as my Region. Click "(US) Central US"**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/10_user_cropped_screenshot.jpeg)

**13. During setup of AKS, it is important to understand production workloads and plan for resilience against datacenter failures. AKS clusters that are deployed using availability zones can distribute nodes across multiple zones within a single region - improving cluster availability. This is also the recommended approach when considering migrating from Amazon EKS to AKS.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/11_user_cropped_screenshot.jpeg)

**14. Description of Availability Zones during setup.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/12_user_cropped_screenshot.jpeg)

**15. We will use the default k8s version selected. Note this may be different depending on the time you create the cluster as these options change as new versions get released. Click the version with "(default)" in it. You have the option to move to older and new (preview) releases right from the start. When migrating from EKS to AKS it is important to ensure your target k8s version is within the supported window for AKS.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/13_user_cropped_screenshot.jpeg)

**16. Since this is a demo, we can select 99.5% API server availability.  API server availability is an uptime service level agreement that guarantees a Kubernetes API server uptime of 99.95% clusters with one or more availability zones and 99.9% for all other clusters.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/14_user_cropped_screenshot.jpeg)

**17. In continuation of selecting an appropriate k8s version in line with our considerations from EKS to AKS, we can also select automatic upgrades. "Enabled with path (recommended)" will update the cluster to the latest patch version within the set minor version. We also have the option to select stable, rapid, node image, and disabled - depending on our workloads on EKS we might select stable for production workloads.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/15_user_cropped_screenshot.jpeg)

**18. Sizing the k8s nodes is important when considering EKS to AKS. The types of workloads and their usage will influence the choice of how many nodes and what node size we use for the cluster. It is also important to consider valid quotas for the migration. You should verify that your quotas and limits are sufficient for these resources and if necessary, request and increase in vCPU quota.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/16_user_cropped_screenshot.jpeg)

**19. We can also select the min and max of nodes to use for autoscaling. If your EKS cluster uses autoscaling and was engineered for high availability and business continuity with respect to elasticity - then the number of nodes is important.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/17_user_cropped_screenshot.jpeg)

**20. Go to the next page and click "Next: Node pools >" Here we can configure additional node pools to handle a variety of workloads and in contrast to some of the obscurity in EKS, we can enable "virtual nodes" right from the start for Azure Container Instance fast burst scaling. We can also select the type of node pool OS disk encryption - important if you are planning to migrate from EKS with your own keys.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/18_user_cropped_screenshot.jpeg)

**21. Next, we can move to Access. Click "Next : Access >"**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/19_user_cropped_screenshot.jpeg)

**22. AKS setup allows for 3 types of authentication and authorization: Local accounts with k8s RBAC, Azure AD authentication with k8s RBAC, and Azure AD authentication with Azure RBAC. One strength of AKS is its tight coupling with Azure AD to use Azure role assignments for authorization checks on the cluster.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/20_user_cropped_screenshot.jpeg)

**23. Next, we will go to the Networking overview. Click "Next : Networking >"**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/21_user_cropped_screenshot.jpeg)

**24. Networking is very important when considering migrating from EKS to AKS. It is important to inventory the range of services and applications that uses them in the EKS cluster and then follow best practices for downtime handling. You might typically migrate over time rather than all at once, meaning old and new enviroments might need to communicate over the network. If an application previously used ClusterIP services to communicate might need to be exposed as LoadBalancer type and secured appropriately after the migration. Ideally, you want to point clients to new services that are running on AKS and we recommend that you redirect traffic by updating DNS to point to the Load Balancing sitting in front of your AKS cluster - Azure Traffic Manager can direct customers to the desired k8s cluster and application instance.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/22_user_cropped_screenshot.jpeg)

**25. In the network section, we can define and create a new virtual network. Both Azure VNet and AWS VPC segregate networks with subnets. Azure VNet assigns resources connected and deployed to the VNet a private IP address for the CIDR block specified and the smallest subnet supported is /29 and largest is a /8. Record the CIDR block range you need when migrating from EKS to AKS for k8s services and and the cluster as you do not want to experience IP exhaustion and also want to be able to scale accordingly.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/23_user_cropped_screenshot.jpeg)

**26. The k8s service address range description.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/24_user_cropped_screenshot.jpeg)

**27. The k8s DNS service IP address description.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/25_user_cropped_screenshot.jpeg)

**28. You can also change the network for the Docker Bridge address - Click "Docker Bridge address"**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/26_user_cropped_screenshot.jpeg)

**29. Description for DNS name prefix for the hosted k8s API server FQDN - important to consider when migrating as this will be used to connect to when managing containers after creating the cluster.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/27_user_cropped_screenshot.jpeg)

**30. Enabling "HTTP Application Routing" will configure an ingress controller in your AKS cluster and as applications are deployed, the ingress controller will create publicly accessible DNS names for your application endpoints. Consider what this might mean for your applications as your migrate over - how many and what needs to be publicly available via ingress and what type of configurations are currently in place that need to be done in the new cluster.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/28_user_cropped_screenshot.jpeg)

**31. In this section, we can select the type of network policy structure for the k8s cluster. We can use Calico or Azure - Azure being one of the key differentiators out of the box vs EKS. Azure allows for Azure Network Policies via Azure Network Policy Manager (NPM) which uses IPTables for Linux and Host Network Service (HNS) ACLPolicies for Windows.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/29_user_cropped_screenshot.jpeg)

**32. Click "Next : Integrations >"**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/30_user_cropped_screenshot.jpeg)

**33. Out of the box, we can enable Microsoft Defender for Cloud which provides unified security management and threat protection across the workloads - importantly when migrating production workloads we want to consider the security policies and protection against threats as we build in AKS. Using Defender backed with Azure Monitor and Azure Policy allows for threat protection, container insights, and at-scale enforcements and safeguards for AKS clusters in a centralized, consistent manner through Azure Policy.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/31_user_cropped_screenshot.jpeg)

**34. When migrating from EKS to AKS, we likely will have a set of images that are pre-built or need built for the new cluster; we can use tools like Azure Migrate to help with that along with connecting the AKS cluster to Azure Container Registry to store and use these images.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/32_user_cropped_screenshot.jpeg)

**35. Click "Next : Advanced >"**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/33_user_cropped_screenshot.jpeg)

**36. When migrating from EKS to AKS, it is important to know the type of data persistence and where the new data will be stored. When we create AKS cluster we have the option to enable secret store CSI driver which also allows us to integrate Azure Key Vault secrets. Ideally, when we migrate persistent volumes, we want to quiesce writes to the application, take snapshosts of the disks, create new managed disks from the snapshots, create persistent volumes in AKS, update the pod spec to use existing volumes rather than static provisioning, then deploy the application to AKS, validate it and point live traffic to the new cluster. You can use tools like Azure CLI Disk Copy extension and Azure Kube CLI extension to migrate volumes between k8s clusters.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/34_user_cropped_screenshot.jpeg)

**37. Click "Next : Tags >" here we can tag the AKS cluster for certain things like environment.**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/35_user_cropped_screenshot.jpeg)

**38. We're ready to create our AKS cluster! Click "Next : Review + create >"**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/36_user_cropped_screenshot.jpeg)

**39. After the cluster has been provisioned, we can connect to it by clicking "Connect to cluster"**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/37_user_cropped_screenshot.jpeg)

**40. We can quickly get a snapshot of the current environment using Cloud Shell - Click "Open Cloud Shell" - from here it gives us all the commands to run and even sets the accout and credentials for us when we open Cloud Shell - then from here we can get deployments and list namespaces and being our EKS to AKS migration!**

![](https://rkscribehowsa.blob.core.windows.net/scribehow/38_user_cropped_screenshot.jpeg)
#### [Made with Scribe](https://scribehow.com/shared/Step-by-Step_AKS_Workflow_-_EKS_to_AKS_Considerations__O2mSEOO4Q0mPy_VWTijcBw)
