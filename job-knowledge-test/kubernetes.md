# Explain how the kubernetes work, and when we need to have kubernetes?

Kubernetes is a container orchestration platform. But before we dive deep on kubernetes, we need to understand first what is containers and how it differs from other deployment model

## Deployment Model

Looking back at the history, i think there are 3 kind of deployment model that exist

1. Traditional Deployment
   Traditionanal deployment means that people run appliation on top of physical server, so the hierarchial steps is an Application is on top of the Operating system, which lies on a hardware. While this is the simplest type of deployment, there are a few problems that rose. For example, there are no way of limiting resource consumption of an app, meaning that running multiple applicatins inside on server will create a resource "war" between them, which results on some application may not get the resource that it needs. The solution for this is running an application in single server, but this may be costly to manage
2. Virutalized Deployment
   Virtualized deployment comes as a solution to the previous problem. It puts a hypervisor on top of the operating system, allowing us to create virtualized machines on a single machine, so we can run machines on a single CPU of a server.
3. Container Deployment
