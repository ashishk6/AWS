# Creating a ECS cluster using AWS Console 
> Elastic container service(ECS) is a services which ensure that the container is remains up/live and also, auto-scale the container parallelly based on the CPU threshold value of load. This process will help the Applicaiton which is running inside the containers remains live and healthy.

--Normally when we use a standalone containers hosting any application, at anypoint it can goes down and the entire application which is hosted via container will be unavaialable.Also, it doesn't have the capability to auto-scale based on the demand.
-- To encounter this we have container management services like Kubernetes, Docker Swarm, AWS ECS, Etc. where this services runs on the top of the container and form a master slave architecture where the master keep on watching the slave node where all the application containers are deployed. Also, it makes sure that none of the Application goes down at any point along with the on-demand scaling tecnhique.

Steps to create ECS cluster:
- Step1: Create a Task Defenition which will define Application container that woould be running in that cluster. We can have multiple task definetion.Here we have to specify the container image and configure the task. 
- Step2: Create a Cluster under which we will be running all the task. 
- Step3: Create the services under the cluster for each task. Under service tab we will configure below few things:
 -- Type of Services: 
  1. Replica Type: Here the ECS will make sure the repliction will be maintained. Enventhough, any containers goes down, ECS will bring up the new ones.
  2. Daemon Type: This will maintain one replica per node. 

    -- Deplotment Type:
    1. Rolling Update
    2. BLue/Green Deployment

    -- There are auto-scaling form to fill the scaling scenerio and the the VPC and the security group detais like (inbound and outbound port)details under which we need to lauch the EC2 services.

    -- Enable other monitoring services for the ECS like cloud watch, etc.
    
  > Run the service and use the application with zero down time and auto-scaling.

-- WE have 2 types of ECS: 
>  1.    Fargate 
>  2.  EC2

 - [Elastic Container Service(ECS)](https://docs.aws.amazon.com/ecs/index.html)


> Note: Try to grab the understanding via hands-on. This will no only help you getting the concept but also help you to understand the flow and process.
 

