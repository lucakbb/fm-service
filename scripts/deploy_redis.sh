#!/bin/bash
# Deploy Redis and update backend service

set -e

echo "Deploying Redis to Kubernetes..."

# Apply Redis deployment
kubectl apply -f meta/k8s/redis.yaml

# Wait for Redis to be ready
echo "Waiting for Redis deployment to be ready..."
kubectl wait --for=condition=available --timeout=300s deployment/redis-deployment -n swiss-ai

# Update backend service
echo "Updating backend service..."
kubectl apply -f meta/k8s/backend.service.yaml

# Wait for backend to be ready
echo "Waiting for backend deployment to be ready..."
kubectl wait --for=condition=available --timeout=300s deployment/serving-backend -n swiss-ai

echo "✅ Deployment completed successfully!"

# Show status
echo -e "\n📊 Deployment Status:"
kubectl get pods -n swiss-ai -l app=redis
kubectl get pods -n swiss-ai -l app=serving-backend

echo -e "\n🔧 Redis Service:"
kubectl get svc redis-service -n swiss-ai

echo -e "\n📈 To check Redis logs:"
echo "kubectl logs -f deployment/redis-deployment -n swiss-ai"

echo -e "\n📈 To check backend logs:"
echo "kubectl logs -f deployment/serving-backend -n swiss-ai"
