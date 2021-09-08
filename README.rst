
# Deploy:

docker-compose up --build

docker tag cloud-run-demo_app europe-west1-docker.pkg.dev/quick-tag-2/quick-tag-2-repo/cloud-run-demo_app
docker push europe-west1-docker.pkg.dev/quick-tag-2/quick-tag-2-repo/cloud-run-demo_app