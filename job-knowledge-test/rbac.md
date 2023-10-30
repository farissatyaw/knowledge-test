# Behaviour Control in Kubernetes

In kubernetes, we can use RBAC (Role based access control) to limit the kubernetes API usage. RBAC binds a user / serviceAccount with assigned roles.

There are multilpe CRDS that are used in this, but mainly divided into 2 part

1. Role
   This part defines the permissions that the role have, for example we can assign like this example below, that this allows to get, watch and list pods on default namespace. Role are namespaced, if we want to use cluster wide, we need to use CLusterRole

```
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: pod-reader
rules:
- apiGroups: [""] # "" indicates the core API group
  resources: ["pods"]
  verbs: ["get", "watch", "list"]
```

2. Binding
   Binding is the part where we bind the subject with the permission assigned by the role. This permission below allows jane to do the action defined above. RoleBinding are namsepaced object, if we want to use CLusterWide, we need to use ClusterRoleBinding

```
apiVersion: rbac.authorization.k8s.io/v1
# This role binding allows "jane" to read pods in the "default" namespace.
# You need to already have a Role named "pod-reader" in that namespace.
kind: RoleBinding
metadata:
  name: read-pods
  namespace: default
subjects:
# You can specify more than one "subject"
- kind: User
  name: jane # "name" is case sensitive
  apiGroup: rbac.authorization.k8s.io
roleRef:
  # "roleRef" specifies the binding to a Role / ClusterRole
  kind: Role #this must be Role or ClusterRole
  name: pod-reader # this must match the name of the Role or ClusterRole you wish to bind to
  apiGroup: rbac.authorization.k8s.io
```
