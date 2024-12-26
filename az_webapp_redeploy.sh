## Script to retrigger the deployment of an Azure Web App using az cli
# Variables
RESOURCE_GROUP=weekendmarathon
WEBAPP_NAME=imagetestplayground
# Redeploy
az webapp restart --name $WEBAPP_NAME --resource-group $RESOURCE_GROUP
# End of script