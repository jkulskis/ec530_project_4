# ec530_project_4

## Summary

There is a simple framework to handle speech to text with a queue system in place. When the function to interpret the audio is called, rather than blocking and converting the audio to text, it adds the job to a queue, and then handles them accordingly.

The queue jobs are handled with multithreading in batches. For example, if we define the max threads to be 3, then 3 jobs will execute at the same time, and once they finish the next 3 (or however many are left if there are not 3) will start executing.

## Use Case Example
We first initialize an audio queue and define how many threads we are willing to have running at the same time.
```
audio_queue = AudioQueue(max_threads=3)
```
Then, we simply add our audio files to it that we want to interpret. If we are receiving audio files periodically, we can add these as we receive them, but for this example we already have all of our audio files available, so we add all of them to the queue right away.
```
audio_queue.add_audio("audios/1.mp3")
audio_queue.add_audio("audios/2.mp3")
audio_queue.add_audio("audios/3.mp3")
audio_queue.add_audio("audios/4.mp3")
audio_queue.add_audio("audios/5.mp3")
```
Finally, we decide to do work on the queue by calling `interpret_audios()`. When this finishes, the audio jobs will reside in `audio_queue.processed_audios()`, which is another queue for the audios that have already been processed.
```
audio_queue.interpret_audios()
```
Note: Results will also be printed to the console.
