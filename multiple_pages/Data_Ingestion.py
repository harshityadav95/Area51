import streamlit as st
from lib_azure.azure_storage import get_blob_service_client, list_blob_containers, file_user_upload
import lib_custom.lib_config

def app():
    st.title('Data Ingestion')
    tab1, tab2 = st.tabs(["Preset", "Manual"])

    with tab1:
        storage_account = st.selectbox(
            'Storage Account',
            ['-_-', 'area51databank'],
            index=0,
            format_func=lambda x: x if x != '-_-' else 'Select an option'
        )

        if storage_account != '-_-':
            account_name = storage_account
            account_key = st.secrets["azure"]["storage"].get(account_name)

            if account_key:
                blob_service_client = get_blob_service_client(account_name, account_key)
                if blob_service_client:
                    container_names = list_blob_containers(blob_service_client)
                    container_names.insert(0, "-_-")  # Add a blank option at the beginning
                    selected_container = st.selectbox("Select a container", container_names)
                    if selected_container != '-_-':
                        file_user_upload(blob_service_client, selected_container)
                else:
                    st.error("Connection could not be established.")
            else:
                st.error("Account key is missing in the secrets configuration.")
        else:
            st.error("Please select a valid storage account.")

    with tab2:
        config_data = lib_custom.lib_config.config_ingest()
        
        if config_data and isinstance(config_data, list) and len(config_data) > 0:
            account_name = None
            account_key = None
            
            for item in config_data:
                if item[0] == "account_name":
                    account_name = item[1]
                elif item[0] == "account_key":
                    account_key = item[1]
            
            if account_name and account_key:
                blob_service_client = get_blob_service_client(account_name, account_key)
                if blob_service_client:
                    container_names = list_blob_containers(blob_service_client)
                    container_names.insert(0, "-_-")  # Add a blank option at the beginning
                    selected_container = st.selectbox("Select a container", container_names)
                    if selected_container != '-_-':
                        file_user_upload(blob_service_client, selected_container)
                else:
                    st.error("Connection could not be established.")
            else:
                st.error("Account name or account key is missing in the configuration.")
        else:
            st.error("Configuration data is missing or invalid.")