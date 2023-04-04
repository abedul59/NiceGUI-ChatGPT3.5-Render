#!/usr/bin/env python3
#import asyncio
#import functools
#import io
#from typing import Callable

from nicegui import ui


'''
async def io_bound(callback: Callable, *args: any, **kwargs: any):

    return await asyncio.get_event_loop().run_in_executor(None, functools.partial(callback, *args, **kwargs))


async def transcribe(e: UploadEventArguments):
    transcription.text = 'Transcribing...'
    model = replicate.models.get('openai/whisper')
    version = model.versions.get('30414ee7c4fffc37e260fcab7842b5be470b9b840f2b608f5baa9bbef9a259ed')
    prediction = await io_bound(version.predict, audio=io.BytesIO(e.content))
    text = prediction.get('transcription', 'no transcription')
    transcription.set_text(f'result: "{text}"')


async def generate_image():
    image.source = 'https://dummyimage.com/600x400/ccc/000000.png&text=building+image...'
    model = replicate.models.get('stability-ai/stable-diffusion')
    version = model.versions.get('db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf')
    prediction = await io_bound(version.predict, prompt=prompt.value)
    image.source = prediction[0]
    '''
'''
# User Interface
with ui.row().style('gap:10em'):
    with ui.column():
        ui.label('OpenAI Whisper (voice transcription)').classes('text-2xl')
        ui.upload(on_upload=transcribe).style('width: 20em')
        transcription = ui.label().classes('text-xl')
    with ui.column():
        ui.label('Stable Diffusion (image generator)').classes('text-2xl')
        prompt = ui.input('prompt').style('width: 20em')
        ui.button('Generate', on_click=generate_image).style('width: 15em')
        image = ui.image().style('width: 60em')
        '''



#async def generate_response():

ui.textarea(label='Text', placeholder='start typing', on_change=lambda e: result2.set_text('you typed: ' + e.value))
ui.button('Generate', on_click=lambda: result.set_text('you typed: ' + e.value)).style('width: 15em')
result = ui.label()
result2 = ui.label()
ui.run()
