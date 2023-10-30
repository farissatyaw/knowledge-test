from unicodedata import name
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
from minio import Minio
from minio.error import S3Error
from django.http import FileResponse

from kafka import KafkaProducer
from datetime import datetime
import json
import requests
from io import BytesIO
# Create your views here.

@csrf_exempt
def generate(request):
    if(request.method == "POST"):
        minio_client = Minio(
            os.getenv("MINIO_SERVER"),
            access_key=os.getenv('MINIO_ACCESS_KEY'),
            secret_key= os.getenv('MINIO_SECRET_KEY'),
            secure=False        
    )

        csv_url = "https://github.com/farissatyaw/knowledge-test/blob/master/data-dummy.csv"

        try:
            response = requests.get(csv_url)
            if(response.status_code == 200):
                csv_content = response.content

                file_name = "data-dummy.csv"

                # Create a BytesIO object to work with the file content
                csv_stream = BytesIO(csv_content)
                csv_stream.seek(0)

                minio_client.put_object(os.getenv("MINIO_BUCKET"), file_name, csv_stream, len(csv_content))

                return HttpResponse("CSV file saved to MinIO with filename: " + file_name)
            else:
                return HttpResponse("Failed to fetch CSV. Status code: " + str(response.status_code), status=500)
        except S3Error as e:
            return HttpResponse("Failed to save CSV to MinIO: " + str(e), status=500)
        except requests.RequestException as e:
            return HttpResponse("Failed to fetch CSV: " + str(e), status=500)

def download(request):
    if(request.method == "GET"):
        minio_client = Minio(
            os.getenv("MINIO_SERVER"),
            access_key=os.getenv('MINIO_ACCESS_KEY'),
            secret_key= os.getenv('MINIO_SECRET_KEY'),
            secure=False
        )
        object_name = "data-dummy.csv"
    try:
        response = minio_client.get_object(os.getenv("MINIO_BUCKET"), object_name)    
        return FileResponse(response, content_type='application/octet-stream')
    except S3Error as e:
        return HttpResponse("Failed to fetch object from MinIO: " + str(e), status=500)
    
def send_mq(request):
    if(request.method == "GET"):
        minio_client = Minio(
            os.getenv("MINIO_SERVER"),
            access_key=os.getenv('MINIO_ACCESS_KEY'),
            secret_key= os.getenv('MINIO_SECRET_KEY'),
            secure=False 
        )
        object_name = "data-dummy.csv"
    try:
        object_info = minio_client.stat_object(os.getenv("MINIO_BUCKET"), object_name)
        fileSize = object_info.size
        producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        producer.send("csv.fileSize", {'csvName': object_name, 'size': fileSize, 'created_at': datetime.now().isoformat()})

        return HttpResponse(f"Metric of {object_name} has been published succesfully")
    except S3Error as e:
            return HttpResponse("Failed to fetch object from MinIO: " + str(e), status=500)