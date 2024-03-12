provider "aws" {
  # shared_credentials_file = "$HOME/.aws/credentials"
  access_key = var.access_key
  secret_key = var.secret_key
  region = var.region
}

# random string for fast-api secret-key env variable
resource "random_string" "fast-api-secret-key" {
  length = 16
  special = true
  override_special = "/@\" "
}