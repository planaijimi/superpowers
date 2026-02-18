---
name: openai-whisper
description: Use when local audio transcription or translation is needed via Whisper CLI, especially for offline/private processing without API keys.
---

# openai-whisper

Use `whisper` for local speech-to-text and subtitle generation.

## Quick start
- `whisper /path/audio.mp3 --model medium --output_format txt --output_dir .`
- `whisper /path/audio.m4a --task translate --output_format srt`

## Common options
- `--model tiny|base|small|medium|large|turbo`
- `--task transcribe|translate`
- `--output_format txt|srt|vtt|json|tsv|all`
- `--output_dir /path/to/out`
- `--language de` (optional, helps accuracy/speed)

## Notes
- First run downloads model files to `~/.cache/whisper`.
- Smaller models are faster; larger models are usually more accurate.
- Use `translate` to produce English output from non-English audio.
- For long media, prefer pre-extracted audio (e.g. wav/m4a) for faster iteration.

## Install hints
- macOS (Homebrew): `brew install openai-whisper`
- Python/pip fallback: `pip install -U openai-whisper`
- ffmpeg may be required by your audio pipeline: `brew install ffmpeg` (or distro equivalent)
