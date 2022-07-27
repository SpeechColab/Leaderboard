#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import asyncio
import aiofile
import sys

from amazon_transcribe.client import TranscribeStreamingClient
from amazon_transcribe.handlers import TranscriptResultStreamHandler
from amazon_transcribe.model import TranscriptEvent, TranscriptResultStream

'''
The code is base on official documentation at:
    https://github.com/awslabs/amazon-transcribe-streaming-sdk
'''


class MyEventHandler(TranscriptResultStreamHandler):
    def __init__(self, transcript_result_stream: TranscriptResultStream, outfile, key):
        self._transcript_result_stream = transcript_result_stream
        self.outfile = outfile
        self.key = key

    async def handle_transcript_event(self, transcript_event: TranscriptEvent):
        # This handler can be implemented to handle transcriptions as needed.
        res_str = ''
        results = transcript_event.transcript.results       
        for result in results:
            if result.is_partial == False:              
                for alt in result.alternatives:
                    self.outfile.write(self.key + '\t' + alt.transcript.strip() + '\n')
                    self.outfile.flush()
        
                    



async def basic_transcribe(audio, outfile, key):
    # Setup up our client with our chosen AWS region
    client = TranscribeStreamingClient(region="us-west-2")

    # Start transcription to generate our async stream
    stream = await client.start_stream_transcription(
        language_code="en-US",
        media_sample_rate_hz=16000,
        media_encoding="pcm",
    )

    async def write_chunks():
        # An example file can be found at tests/integration/assets/test.wav
        # NOTE: For pre-recorded files longer than 5 minutes, the sent audio
        # chunks should be rate limited to match the realtime bitrate of the
        # audio stream to avoid signing issues.
        async with aiofile.AIOFile(audio, 'rb') as afp:
            reader = aiofile.Reader(afp, chunk_size=1024 * 16)
            async for chunk in reader:
                await stream.input_stream.send_audio_event(audio_chunk=chunk)
        await stream.input_stream.end_stream()

    # Instantiate our handler and start processing events
    handler = MyEventHandler(stream.output_stream, outfile, key)
    await asyncio.gather(write_chunks(), handler.handle_events())



if __name__ == '__main__':

    if len(sys.argv) != 3:
        sys.stderr.write("rest_api.py <in_scp> <out_trans>\n")
        exit(-1)

    SCP = sys.argv[1]
    TRANS = sys.argv[2]

    scp_file = open(SCP, 'r', encoding='utf8')
    trans_file = open(TRANS, 'w+', encoding='utf8')

    n = 0
    for l in scp_file:
        l = l.strip()
        if l == '':
            continue

        key, audio = l.split('\t')
        sys.stderr.write(str(n) + '\tkey:' + key + '\taudio:' + audio + '\n')
        sys.stderr.flush()

        loop = asyncio.get_event_loop()
        loop.run_until_complete(basic_transcribe(audio,trans_file,key))

        
        n += 1
    loop.close()
    scp_file.close()
    trans_file.close()
    
    trans_r_file = open(TRANS, 'r', encoding='utf8')
    res_dict = {}
    for l in trans_r_file:
        key, text = l.split('\t')
        text =text.strip()
        if key in res_dict.keys():
            res_dict[key] += ' ' + text
        else:
            res_dict[key] = text
    trans_r_file.close()

    trans_w_file = open(TRANS, 'w+', encoding='utf8')
    for key in res_dict.keys():
        trans_w_file.write(key + '\t' + res_dict[key].strip() + '\n')

    trans_w_file.close()


