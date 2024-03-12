# create the ECS cluster
resource "aws_ecs_cluster" "fp-ecs-cluster" {
  name = "fast-api-app"

  tags = {
    Name = "fast-api-app"
  }
}