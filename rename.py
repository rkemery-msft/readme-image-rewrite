import re
import urllib.request
import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

readme = 'scribehow.md'
new_readme = 'scribehow_new.md'
clean_readme = 'scribehow_clean.md'
dest_folder = 'images'
container_name = 'scribehow'

# Open file and read contents
with open(readme, 'r') as f:
    contents = f.read()

# Use regular expression to find all URLs in the file
urls = re.findall('https://ajeuwbhvhr\.cloudimg\.io/colony-recorder\.s3\.amazonaws\.com/files/\d{4}-\d{2}-\d{2}/[\w\d]+-[\w\d]+-[\w\d]+-[\w\d]+-[\w\d]+/[\w\d-]+.jpeg', contents)
count = len(urls)
print("The number of urls in the readme:", count)

# Create the destination folder if it doesn't exist
if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

# Loop over the list of URLs and download each file
for i, url in enumerate(urls):
    # Get the filename from the URL
    filename = url.split("/")[-1]
    
    # Add a number prefix to the filename
    new_filename = f"{i+1:02d}_{filename}"
    
    # Download the file
    urllib.request.urlretrieve(url, os.path.join(dest_folder, new_filename))
    
    print(f"Downloaded {url} to {new_filename}")

# Azure Storage account credentials
connect_str = ""

# Create a BlobServiceClient object using the connection string
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# Create a ContainerClient object for the destination container
container_client = blob_service_client.get_container_client(container_name)

# Get a list of all blobs in the container
blob_list = container_client.list_blobs()

# Loop through each blob and delete it
for blob in blob_list:
    container_client.delete_blob(blob.name)

# Loop over each file in the source folder and upload it to the container
for filename in os.listdir(dest_folder):
    # Get the full path to the file
    file_path = os.path.join(dest_folder, filename)
    
    # Create a BlobClient object for the destination blob
    blob_client = container_client.get_blob_client(filename)
    
    # Upload the file to the blob
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
        
    print(f"Uploaded {file_path} to {container_name}")

# Initialize an empty list to store the URLs
url_list = []

# List all blobs in the container and append their URLs to the list
for blob in container_client.list_blobs():
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob.name)
    url = blob_client.url
    url_list.append(url)

# Print the list of URLs
print(url_list)

# Using a dictionary comprehension to generate a new dictionary
new_dict = {k: v for k, v in zip(urls, url_list)}

print(new_dict)

# Open the file for reading and create a new file for writing the modified content
with open(readme, 'r') as f_in, open(new_readme, 'w') as f_out:
    # Iterate over each line in the input file
    for line in f_in:
        # Iterate over each old URL in the URL mapping
        for k, v in new_dict.items():
            # Replace the old URL with the new URL
            line = line.replace(k, v)
        # Write the modified line to the output file
        f_out.write(line)

# Open the input file for reading and output file for writing
with open(new_readme, 'r') as input_file, open(clean_readme, 'w') as output_file:
    # Read the input file line by line
    for line in input_file:
        # Check if the line contains the word "jpeg"
        if 'jpeg' in line:
            # Find the index of the word "jpeg"
            index = line.find('jpeg')
            # Remove the text after the word "jpeg" to the end of the line
            new_line = line[:index+4] + ')' + '\n'
            # Write the modified line to the output file
            output_file.write(new_line)
        else:
            # Write the original line to the output file
            output_file.write(line)