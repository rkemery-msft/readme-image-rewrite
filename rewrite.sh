#!/bin/bash

README="scribehow.md"
URLS="urls.txt"
AZURE_STORAGE_ACCOUNT='rkscribehow'
AZURE_STORAGE_ACCESS_KEY=''
CONTAINER_NAME="scribehow03"
SOURCE_FOLDER="images/*"
CONNECTION_STRING=""
RG="scribehow"
BLOB_BASE_URL=$(az storage account show --name $AZURE_STORAGE_ACCOUNT --resource-group $RG --query "primaryEndpoints.blob")

# old way
#cat $README | grep -Eo "(http|https)://[a-zA-Z0-9./?=_%:-]*.jpeg" | sort -u > $URLS
#xargs -n 1 curl -O < $URLS
#cut -d ' ' -f 3 < $URLS | wget -P images -i -

i=1
URLS_FORMATTED=$(grep -oP '[^"]+\.jpeg' $URLS)

for url in $URLS_FORMATTED
do
  # Save the zeropadded number to a variable named "zeropadded".
  # The number 02 says you want to pad with 0, to make the string 2 characters long.
  printf -v zeropadded "%02d" $i

  # Output the contents of the URL to e.g. "1-etc"
  curl -o "${zeropadded}-$(basename "$url")" -L "$url" --output-dir images

  # Increment the counter
  i=$(( i + 1 ))
done

echo "Creating the container..."
az storage container create --connection-string $CONNECTION_STRING --name $CONTAINER_NAME --public-access blob

for f in $SOURCE_FOLDER
do
  echo "Uploading $f file..."
  az storage blob upload --account-name $AZURE_STORAGE_ACCOUNT --account-key $AZURE_STORAGE_ACCESS_KEY --container-name $CONTAINER_NAME --file $f
done

echo "Listing the blobs..."
az storage account show --name $AZURE_STORAGE_ACCOUNT --resource-group $RG --query "primaryEndpoints.blob"

# not working :(
#echo "Edit the file..."
#for fileName in $(ls images/); do
#    sed -i /'https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com'/c\$BLOB_BASE_URL' $README
#done

echo "Done"

