from addWatermark.utils.generateId import generateRandomString

import subprocess

class Conversions:
    def __init__(self, videoPath, waterMarkPath):
        self.videoPath = videoPath
        self.waterMarkPath = waterMarkPath
        self.ffmpegCommand = 'ffmpeg -y -i {videoPath} -i {waterMarkPath} -filter_complex "[1]lut=a=val*{size}[a];[0][a]{position}" -c:v libx264 {convertedVideoPath}'

    def simple(self, position: str, size: str):
        waterMarkPositions = {
            'tl': 'overlay=25:25',
            'tr': 'overlay=W-w-25:25',
            'bl': 'overlay=25:H-h-25',
            'br': 'overlay=W-w-25:H-h-25'
        }

        waterMarkPosition = waterMarkPositions[position]

        simpleConversionId = generateRandomString(5)
        convertedVideoPath = f'storage/convertedVideos/simpleConv{simpleConversionId}.mp4'

        simpleFfmpegCommand = self.ffmpegCommand.format(
            videoPath=self.videoPath, 
            waterMarkPath=self.waterMarkPath, 
            size=size, 
            position=waterMarkPosition, 
            convertedVideoPath=convertedVideoPath
        )

        subprocess.call(simpleFfmpegCommand)

        return { 'convertedVideoPath': convertedVideoPath.replace('/', '_') }


    def advanced(self, xPos: int, yPos: int, size: str):
        advancedConversionId = generateRandomString(5)
        convertedVideoPath = f'storage/convertedVideos/advancedConv{advancedConversionId}.mp4'

        advnacedFfmpegCommand = self.ffmpegCommand.format(
            videoPath=self.videoPath,
            waterMarkPath=self.waterMarkPath,
            size=size,
            position=f'overlay={xPos}:{yPos}',
            convertedVideoPath=convertedVideoPath
        )

        subprocess.call(advnacedFfmpegCommand)

        return { 'convertedVideoPath': convertedVideoPath.replace('/', '_') }