import docusign_esign as docusign
from docusign_esign import EnvelopesApi, EnvelopeDefinition, Signer, SignHere, Document

# Initialize DocuSign API client
api_client = docusign.ApiClient()
api_client.host = "https://demo.docusign.net/restapi"

# Obtain OAuth access token
access_token = 'c4b834ef-1007-4403-8e8e-bf8fe58eebc7'
api_client.set_default_header("Authorization", "Bearer " + access_token)

# Create envelope definition
envelope_definition = EnvelopeDefinition(
    email_subject='Please sign this document',
    documents=[Document(document_base64='YOUR_DOCUMENT_CONTENT', name='Document.pdf')],
    recipients=Signer(
        email='recipient@example.com',
        name='Recipient Name',
        recipient_id='1',
        tabs={
            'sign_here_tabs': [SignHere(anchor_string='SIGN_HERE', anchor_units='pixels', anchor_x_offset='10', anchor_y_offset='20')]
        }
    ),
    status='sent'
)

# Send envelope
envelopes_api = EnvelopesApi(api_client)
envelope_summary = envelopes_api.create_envelope('YOUR_ACCOUNT_ID', envelope_definition=envelope_definition)
print(envelope_summary)
