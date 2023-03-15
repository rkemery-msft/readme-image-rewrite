#!/bin/bash

README="scribehow.md"
URLS="urls.txt"
AZURE_STORAGE_ACCOUNT=''
AZURE_STORAGE_ACCESS_KEY=''
CONTAINER_NAME=""
SOURCE_FOLDER="images/*"
CONNECTION_STRING=""
RG=""

cat $README | grep -Eo "(http|https)://[a-zA-Z0-9./?=_%:-]*.jpeg" | sort -u > $URLS
cut -d ' ' -f 3 < $URLS | wget -P images -i -

echo "Creating the container..."
az storage container create --connection-string $CONNECTION_STRING --name $CONTAINER_NAME --public-access blob

for f in $source_folder
do
  echo "Uploading $f file..."
  az storage blob upload --account-name $AZURE_STORAGE_ACCOUNT --account-key $AZURE_STORAGE_ACCESS_KEY --container-name $CONTAINER_NAME --file $f
done

echo "Listing the blobs..."
az storage account show --name $AZURE_STORAGE_ACCOUNT --resource-group $RG --query "primaryEndpoints.blob"

echo "Done"

