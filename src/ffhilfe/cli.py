from .main import build_params, execute, ffmpeg_bin, parse_args


def cli():
    args = parse_args()
    params = build_params(args)
    for param in params:
        execute(ffmpeg_bin, param, args)
