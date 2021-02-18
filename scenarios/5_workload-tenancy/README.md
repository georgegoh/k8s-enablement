Scenario 5
==========

An administrator wants to understand how multiple projects can run effectively on the same Kubernetes cluster. After monitoring the workloads over a period of time, you have noted the following information about workloads running on the cluster:

| Name | Namespace | Replicas | Avg CPU(Peak) | Avg Mem(Peak) |
| ---- | --------- | -------- | ------------- | ------------- |
| Account Service | accounts | 2 | 100m(400m) | 100Mi(200Mi) |
| Inventory Service | inventory | 2 | 500m(800m) | 50Mi(75Mi) |
| Shipping Service | shipping | 2 | 300m(700m) | 80Mi(80Mi) |
| Storefront Web App | storefront | 4 | 200m(500m) | 90Mi(100Mi) |
| API Gateway | apigw | 6 | 200m(500m) | 100Mi(105Mi) |

You decide to use the LimitRange mechanism to enforce consumption restrictions.

Tasks
-----
- Write LimitRange objects that apply for the `Account Service` namespace.
- Write a simple test case that validates that the LimitRange object is applied correctly.
- Will the new LimitRanges be applied to the currently running pods? If not, what is your strategy for applying them?