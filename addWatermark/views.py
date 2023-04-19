from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import BaseDataSerializer
from addWatermark.ffmpegConversions.conversions import Conversions

@api_view(['POST'])
def simpleConversion(request, position=None, size=None):
    baseDataSerializer = BaseDataSerializer(data=request.data)

    if baseDataSerializer.is_valid():
        baseDataSerializer.save()

        videoPath = baseDataSerializer.data.get('video')
        waterMarkPath = baseDataSerializer.data.get('waterMark')

        ffmpegConversion = Conversions(str(videoPath)[1:], str(waterMarkPath)[1:])
        simpleFfmpegConversion = ffmpegConversion.simple(position, size)

        return Response({ 
            'convertedVideoPath': simpleFfmpegConversion
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
            'convertedVideoPath': advancedFfmpegConversion
        })

    return Response({ 'convertedVideoPath': 'error' })

@api_view(['GET'])
def download(request):
    # download converted file
    return Response('dwonload')