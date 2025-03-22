# infrastructure/terraform/outputs.tf
output "backend_url" {
  description = "URL of the backend API"
  value       = "https://${azurerm_container_app.backend.ingress[0].fqdn}"
}

output "frontend_url" {
  description = "URL of the frontend application"
  value       = "https://${azurerm_container_app.frontend.ingress[0].fqdn}"
}

output "container_registry_url" {
  description = "URL of the container registry"
  value       = azurerm_container_registry.acr.login_server
}

output "cosmos_db_connection_string" {
  description = "Connection string for Cosmos DB"
  value       = azurerm_cosmosdb_account.db.connection_strings[0]
  sensitive   = true
}
