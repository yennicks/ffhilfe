# ffmpeg-helper
A simple ffmpeg helper script. Requires Python 3.13 or higher.

# Usage
```
usage: convert.py [-h] [-d] -t TEMPLATE input [input ...]

An opinionated command line ffmpeg script.

positional arguments:
  input                 One or more input files

optional arguments:
  -h, --help            show this help message and exit
  -d, --dry-run         Show commands to be executed without executing them.
  -t TEMPLATE, --template TEMPLATE
                        The name of a predefined template
```

# Example ffhilfe files

Transcode video, keep original audio - for example, compress smartphone recording.
```yaml
parameters: '-c:a copy -c:v libx264 -profile:v high -preset:v veryslow -crf:v 32 -level:v 4.2'
output_format: 'mp4'
```
