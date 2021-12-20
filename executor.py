from jina import Executor, DocumentArray, requests


class ImageUriToBlob(Executor):
    @requests
    def convert_image_uri_to_blob(self, docs: DocumentArray, **kwargs):
        for doc in docs:
            doc.tags["uri"] = doc.uri # So we don't lose access to uri
            doc.convert_uri_to_image_blob()
