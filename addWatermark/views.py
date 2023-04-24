from django.http import HttpResponse
from wsgiref.util import FileWrapper

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import BaseDataSerializer
from addWatermark.ffmpegConversions.conversions import Conversions
from addWatermark.utils.generateId import generateRandomString

import os

@api_view(['POST'])
def simpleConversion(request, position=None, size=None):
    baseDataSerializer = BaseDataSerializer(data=request.data)

    if baseDataSerializer.is_valid():
        baseDataSerializer.save()

        videoPath = baseDataSerializer.data.get('video')
        waterMarkPath = baseDataSerializer.data.get('waterMark')

        ffmpegConversion = Conversions(str(videoPath)[1:], str(waterMarkPath)[1:])
        simpleFfmpegConversion = ffmpegConversion.simple(position, size)

        os.remove(str(videoPath)[1:])

        return Response({ 
            'convertedVideoPath': simpleFfmpegConversion['convertedVideoPath']
        })

    return Response({ 'convertedVideoPath': 'error' })


@api_view(['POST'])
def advancedConversion(request, xPos=None, yPos=None, size=None):
    baseDataSerializer = BaseDataSerializer(data=request.data)

    if baseDataSerializer.is_valid():
        baseDataSerializer.save()

        videoPath = baseDataSerializer.data.get('video')
        waterMarkPath = baseDataSerializer.data.get('waterMark')

        ffmpegConversion = Conversions(str(videoPath)[1:], str(waterMarkPath)[1:])
        advancedFfmpegConversion = ffmpegConversion.advanced(xPos, yPos, size)

        return Response({ 
            'convertedVideoPath': advancedFfmpegConversion['convertedVideoPath']
        })

    return Response({ 'convertedVideoPath': 'error' })


@api_view(['GET'])
def download(request, path: str):
    ##download converted file
    convertedVideo = open(path.replace('_', '/'), 'rb')
    responseId = generateRandomString(5)

    response = HttpResponse(FileWrapper(convertedVideo), content_type='video/*')
    response['Content-Disposition'] = 'attachment; filename="%s"' % responseId

    return response