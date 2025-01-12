import streamlit as st
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


def file_user_upload(blob_service_client, container_name):

    # List of accepted file formats
    accepted_formats = [
        'csv', 'eml', 'epub', 'gz', 'html', 'json', 'kml', 'docx', 'doc', 'docm', 'xlsx', 'xls', 'xlsm',
        'pptx', 'ppt', 'pptm', 'msg', 'xml', 'odt', 'ods', 'odp', 'pdf', 'txt', 'rtf', 'zip'
    ]

    # Streamlit file uploader for multiple files
    uploaded_files = st.file_uploader("Upload files", type=accepted_formats, accept_multiple_files=True)

    if uploaded_files:
        file_container_push(blob_service_client, container_name, uploaded_files)
    else:
        st.write("Please upload files with one of the supported formats")



def get_blob_service_client(account_name, account_key):
    try:
        # Create the BlobServiceClient object using the account name and key
        blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)

        #st.write("BlobServiceClient created successfully!")
        return blob_service_client

    except Exception as ex:
        st.error(f"An error occurred: {ex}")
        return None

def file_container_push(blob_service_client, container_name, uploaded_files):
    if blob_service_client is None:
        return

    try:
        for uploaded_file in uploaded_files:
            # Create a blob client using the local file name as the name for the blob
            blob_client = blob_service_client.get_blob_client(container=container_name, blob=uploaded_file.name)

            # Upload the file to Azure Blob Storage and overwrite if it already exists
            blob_client.upload_blob(uploaded_file, overwrite=True)

            st.success(f"Files pushed to Azure Storage successfully!")

    except Exception as ex:
        st.error(f"An error occurred: {ex}")


def list_blob_containers(blob_service_client):
    try:
        # List all containers in the storage account
        containers = blob_service_client.list_containers()
        container_names = [container['name'] for container in containers]
        
        st.success("Connected to Storage Account")
        return container_names

    except Exception as ex:
        st.error(f"An error occurred: {ex}")
        return None