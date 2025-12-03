# utils/gcs_client.py
import logging
from typing import BinaryIO, Optional
import datetime
from google.cloud import storage
from google.oauth2 import service_account
from utils.config import GCS_BUCKET_NAME, get_gcs_credentials

logger = logging.getLogger(__name__)

class GCSClient:
    """Singleton Google Cloud Storage client with proper lifecycle management."""
    
    _instance = None
    _client = None
    _bucket_name = None
    
    def __new__(cls):
        """Ensure only one instance exists (Singleton pattern)."""
        if cls._instance is None:
            cls._instance = super(GCSClient, cls).__new__(cls)
        return cls._instance
    
    @classmethod
    def initialize(cls):
        """Initialize GCS client - call this once during app startup."""
        if cls._client is not None:
            logger.warning("GCS client already initialized")
            return
        
        try:
            credentials_dict = get_gcs_credentials()
            credentials = service_account.Credentials.from_service_account_info(credentials_dict)
            cls._client = storage.Client(credentials=credentials)
            cls._bucket_name = GCS_BUCKET_NAME
            
            if not cls._bucket_name:
                raise ValueError("GCS_BUCKET_NAME is required")
            
            logger.info("GCS client initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize GCS client: {e}")
            raise ConnectionError(f"GCS authentication failed: {e}")
    
    @classmethod
    def close(cls):
        """Close GCS client - call this during app shutdown."""
        if cls._client is not None:
            cls._client.close()
            cls._client = None
            logger.info("GCS client closed")
    
    @property
    def client(self):
        """Get the storage client instance."""
        if self._client is None:
            raise RuntimeError("GCS client not initialized. Call GCSClient.initialize() first.")
        return self._client
    
    @property
    def bucket_name(self):
        """Get the configured bucket name."""
        if self._bucket_name is None:
            raise RuntimeError("GCS client not initialized")
        return self._bucket_name
    
    def upload_file(self, file_data: BinaryIO, file_path: str, content_type: str = None) -> dict:
        """Upload file to GCS bucket."""
        try:
            bucket = self.client.bucket(self.bucket_name)
            blob = bucket.blob(file_path)
            blob.upload_from_file(file_data, content_type=content_type)
            
            return {
                'success': True,
                'path': file_path,
                'bucket': self.bucket_name,
                'url': f"gs://{self.bucket_name}/{file_path}"
            }
        except Exception as e:
            logger.error(f"Failed to upload file {file_path}: {e}")
            return {
                'success': False,
                'message': "Failed to upload file",
            }
    
    def get_signed_url(
        self, 
        file_path: str, 
        expiration_minutes: int = 60,
        response_disposition: Optional[str] = None
    ) -> Optional[str]:
        """
        Generate signed URL for temporary file access.
        
        Args:
            file_path: Path to the file in GCS bucket
            expiration_minutes: URL expiration time in minutes
            response_disposition: Content-Disposition header value (e.g., 'attachment; filename="report.pdf"')
        """
        try:
            bucket = self.client.bucket(self.bucket_name)
            blob = bucket.blob(file_path)
            
            query_parameters = None
            if response_disposition:
                query_parameters = {
                    'response-content-disposition': response_disposition
                }
            
            url = blob.generate_signed_url(
                version="v4",
                expiration=datetime.timedelta(seconds=expiration_minutes * 60),
                method="GET",
                query_parameters=query_parameters
            )
            return url
        except Exception as e:
            logger.error(f"Failed to generate signed URL for {file_path}: {e}")
            return None
    
    def download_file(self, gcs_path: str, local_path: str) -> bool:
        """
        Download file from GCS to local path.
        
        Args:
            gcs_path: Path in GCS bucket
            local_path: Local file path to save to
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            bucket = self.client.bucket(self.bucket_name)
            blob = bucket.blob(gcs_path)
            
            # Check if blob exists
            if not blob.exists():
                logger.error(f"File does not exist in GCS: {gcs_path}")
                return False
            
            # Download to local file
            blob.download_to_filename(local_path)
            return True
        except Exception as e:
            logger.error(f"Failed to download file {gcs_path} to {local_path}: {e}")
            return False
    
    def file_exists(self, file_path: str) -> bool:
        """Check if file exists in GCS bucket."""
        try:
            bucket = self.client.bucket(self.bucket_name)
            blob = bucket.blob(file_path)
            return blob.exists()
        except Exception as e:
            logger.error(f"Failed to check if file exists {file_path}: {e}")
            return False

# Singleton instance
gcs_client = GCSClient()
