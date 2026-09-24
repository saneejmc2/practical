
2. Pull the Floci image
docker pull floci/floci:latest

3. Create a docker-compose.yml

services:
  floci:
    image: floci/floci:latest
    ports:
      - "4566:4566"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock



4. Start Floci
docker compose up -d

To stop: docker compose down

Floci will now be running locally at: http://localhost:4566

5. Configure AWS CLI (Dummy Credentials Allowed)

export AWS_ENDPOINT_URL=http://localhost:4566
export AWS_DEFAULT_REGION=us-east-1
export AWS_ACCESS_KEY_ID=test
export AWS_SECRET_ACCESS_KEY=test


6. Test It Works
aws s3 mb s3://my-bucket --endpoint-url $AWS_ENDPOINT_URL
aws s3 ls --endpoint-url $AWS_ENDPOINT_URL

Web Console UI: http://localhost:4566/_floci/ui

