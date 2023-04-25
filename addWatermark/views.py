from django.http import HttpResponse
from django.db import transaction
from wsgiref.util import FileWrapper

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import BaseDataSerializer
from addWatermark.ffmpegConversions.conversions import Conversions
from addWatermark.utils.generateId import generateRandomString

import os, threading
from threading import Lock

@transaction.atomic
@api_view(['POST'])
def simpleConversion(request, position: str, size: str):
    baseDataSerializer = BaseDataSerializer(data=request.data)

    if baseDataSerializer.is_valid():
        baseDataSerializer.save()

        videoPath = str(baseDataSerializer.data.get('video'))[1:]
        waterMarkPath = str(baseDataSerializer.data.get('waterMark'))[1:]

        ffmpegConversion = Conversions(videoPath, waterMarkPath)
        simpleFfmpegConversion = ffmpegConversion.simple(position, size)

        os.remove(videoPath)
        os.remove(waterMarkPath)

        return Response({
            'convertedVideoPath': simpleFfmpegConversion['convertedVideoPath']
        })

    return Response({ 'convertedVideoPath': 'error' })


@transaction.atomic
@api_view(['POST'])
def advancedConversion(request, xPos: int, yPos: int, size: str):
    baseDataSerializer = BaseDataSerializer(data=request.data)

    if baseDataSerializer.is_valid():
        baseDataSerializer.save()

        videoPath = str(baseDataSerializer.data.get('video'))[1:]
        waterMarkPath = str(baseDataSerializer.data.get('waterMark'))[1:]

        ffmpegConversion = Conversions(videoPath, waterMarkPath)
        advancedFfmpegConversion = ffmpegConversion.advanced(xPos, yPos, size)

        os.remove(videoPath)
        os.remove(waterMarkPath)

        return Response({
            'convertedVideoPath': advancedFfmpegConversion['convertedVideoPath']
        })

    return Response({ 'convertedVideoPath': 'error' })


@api_view(['GET'])
def download(request, path: str):
    convertedVideoPath = path.replace('_', '/')

    convertedVideo = open(convertedVideoPath, 'rb')
    responseId = generateRandomString(5)

    response = HttpResponse(FileWrapper(convertedVideo), content_type='video/*')
    response['Content-Disposition'] = 'attachment; filename="%s"' % responseId

    os.remove(convertedVideoPath)

    return response