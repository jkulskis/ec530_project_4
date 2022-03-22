# ec530_project_4

## Speech To Text

There is a simple API to handle speech to text with a queue system in place. When the function to interpret the audio is called, rather than blocking and converting the audio to text, it adds the job to a queue, and then handles them accordingly.

Multiprocessing is not yet added for the queue, but it will be in future updates