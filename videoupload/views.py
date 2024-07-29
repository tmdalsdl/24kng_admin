from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import VideoForm
from .models import Video
from django.utils import timezone
import boto3
import os
import logging
import requests  # 추가된 부분

logger = logging.getLogger(__name__)

def upload_to_s3(file, bucket_name, s3_path):
    try:
        s3 = boto3.client('s3')
        s3.upload_fileobj(file, bucket_name, s3_path)
    except Exception as e:
        logger.error(f"S3 upload failed: {str(e)}")
        raise

def admin_page(request):
    return render(request, 'videoupload/AdminPage.html')

def video_upload(request):
    if request.method == 'POST':
        try:
            video_bucket_name = os.getenv('AWS_STORAGE_BUCKET_NAME')
            thumbnail_bucket_name = os.getenv('AWS_THUMBNAIL_BUCKET_NAME')
            cloudfront_url = os.getenv('AWS_CLOUDFRONT_URL')

            if not all([video_bucket_name, thumbnail_bucket_name, cloudfront_url]):
                raise ValueError("Missing required environment variables")

            rows = len([key for key in request.POST.keys() if key.startswith('file_name-')])
            
            for i in range(rows):
                file_name_key = f'file_name-{i}'
                if file_name_key in request.POST:
                    file_name = request.POST[file_name_key]
                    category = request.POST.get(f'category-{i}')
                    if category == 'custom':
                        category = request.POST.get(f'custom_category-{i}')
                    title = file_name
                    country = request.POST.get(f'country-{i}')
                    description = request.POST.get(f'description-{i}', '')
                    date = timezone.now().strftime('%Y-%m-%d')
                    
                    video_file = request.FILES.get(f'video-{i}')
                    thumbnail_file = request.FILES.get(f'thumbnail-{i}')
                    
                    if not video_file or not thumbnail_file:
                        raise ValueError(f"Missing video or thumbnail file for row {i}")

                    video_extension = os.path.splitext(video_file.name)[1]
                    thumbnail_extension = os.path.splitext(thumbnail_file.name)[1]
                    
                    video_s3_path = f'vod/{category}/{date}/{file_name}'
                    thumbnail_s3_path = f'thumbnail/{category}/{date}/{file_name}'
                    
                    upload_to_s3(video_file, video_bucket_name, f'{video_s3_path}{video_extension}')
                    upload_to_s3(thumbnail_file, thumbnail_bucket_name, f'{thumbnail_s3_path}{thumbnail_extension}')
                    
                    video_url = f'{cloudfront_url}{video_s3_path}/{file_name}.m3u8'
                    thumbnail_url = f'{cloudfront_url}{thumbnail_s3_path}{thumbnail_extension}'
                    
                    Video.objects.create(
                        title=title,
                        description=description,
                        country=country,
                        video_url=video_url,
                        thumbnail_url=thumbnail_url
                    )
            return redirect('admin_page')
        except Exception as e:
            logger.error(f"Video upload failed: {str(e)}")
            return JsonResponse({'error': str(e)}, status=500)
    else:
        form = VideoForm()
    return render(request, 'videoupload/VideoUpload.html', {'form': form})

def dashboard(request):
    return render(request, 'videoupload/Dashboard.html')

# EKS 관련 추가된 부분 시작
def get_eks_service_url(service_name, namespace='default'):
    try:
        client = boto3.client('eks')
        response = client.describe_cluster(name=os.getenv('EKS_CLUSTER_NAME'))
        endpoint = response['cluster']['endpoint']
        token = boto3.client('sts').get_caller_identity().get('Arn')
        
        headers = {
            'Authorization': f'Bearer {token}'
        }
        
        api_response = requests.get(f'{endpoint}/api/v1/namespaces/{namespace}/services/{service_name}', headers=headers, verify=False)
        if api_response.status_code == 200:
            service_info = api_response.json()
            ip = service_info['status']['loadBalancer']['ingress'][0]['hostname']
            return ip
        else:
            logger.error(f"Failed to get service URL from EKS: {api_response.text}")
            return None
    except Exception as e:
        logger.error(f"Error fetching EKS service URL: {e}")
        return None

def get_public_ip(request):
    service_name = 'monitoring-cluster'  # 여기에 특정할 EKS 서비스 이름을 지정하세요.
    public_ip = get_eks_service_url(service_name)

    if public_ip:
        return JsonResponse({'public_ip': public_ip})
    else:
        return JsonResponse({'error': 'Failed to fetch public IP or no running service found'}, status=500)
# EKS 관련 추가된 부분 끝
