# Explain how the kubernetes work, and when we need to have kubernetes?

Kubernetes is a container orchestration platform. But before we dive deep on kubernetes, we need to understand first what is containers and how it differs from other deployment model

## Deployment Model
Looking back at the history, i think there are 3 kind of deployment model that exist
1. Traditional Deployment 
Traditionanal deployment means that people run appliation on top of physical server, so the hierarchial steps is an Application is on top of the Operating system, which lies on a hardware. While this is the simplest type of deployment, there are a few problems that rose. For example, there are no way of limiting resource consumption of an app, meaning that running multiple applicatins inside on server will create a resource "war" between them, which results on some application may not get the resource that it needs. The solution for this is running an application in single server, but this may be costly to manage
2. Virutalized Deployment
Virtualized deployment comes as a solution to the previous problem. It puts a hypervisor on top of the operating system, which means that we can run "multiple computer" inside one physical machine, which translates to the ability to isolate application in single CPU core, which limits the resource consumption. 
3. Containerized Deployment
Containerized deployment is similar to Virtualized deployment, even to the point that containerized deployment is run in a virtual machine also. The difference between them is after the hypervisor abstraction, it runs a container runtime, which able to create multiple "containerized application". A containerized application may have completely seperate OS, and have the ability to limit the resource to smaller sizes. A containerized app may only need 10m CPU and 50Mi Memory, which virtualized deployment arent able since its limited to the core of the machines. 

## Kubernetes
While containerized deployment are great to run your application, there are a lot of things that aren't supported in default container runtime (For example Docker). The simplest thing is rollout and rollbacks, and horizontal scaling, it is hard to done it at docker. Therefore Kubernetes comes in, it is a container orchestrating engine. Its the most popular right now, compared to the competitor such as Nomad and Docker Swarm

Actually, Kubernetes runs in a container runtime, it used to run in Docker Runtime, until 1.24 it switch to Containerd. Kubernetes have 2 main grouping of parts
1. Control Plane
Control plane consist of the main parts to get the kubernetes working, there are parts like API server, etcd, scheduler and etc. This part is usually the part that is managed in some cloud services, since with scale, sometime it gets harder to manage this part, so sometimes its better to pass on the control plane to the Cloud Provider, so we can focus on managing our apps. 
2. Worker Node
Worker node, as the name suggest, its the worker part of kubernetes. Here is where we put our apps. In the worker node we need kubelet and kube proxy, to be able to to communicate with the control plane.

## When we need to Have Kubernetes?

Kubernetes is all powerful, but not for all occasions. In my opinion, the most determintal factor is the presence of someone that can manage the kubernetes infrastructure. While powerful, there are a lot of things in kubernetes that may be hard when there are no resources to manage the infrastructure. Starting from big things like networking, service mesh until small things like rollout strategy and defining resource may be crucial in production environment. If the need is for developing an MVP for an application, a PaaS like Google App Engine or Amazon ECS/Beanstalk may be better. 
